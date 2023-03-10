#!/usr/bin/env python3
"""Ankdown: Convert Markdown files into anki decks.

Usage:
    ankdown.py [-r DIR] [-p PACKAGENAME] [--updatedOnly] [--config CONFIG_STRING] [--configFile CONFIG_FILE_PATH]

Options:
    -h --help     Show this help message
    --version     Show version

    -r DIR        Recursively visit DIR, accumulating cards from `.md` files.

    -p PACKAGE    Instead of a .txt file, produce a .apkg file. recommended.

    --updatedOnly  Only generate cards from updated `.md` files

    --config CONFIG_STRING  ankdown configuration as YAML string

    --configFile CONFIG_FILE_PATH   path to ankdown configuration as YAML file
"""

import hashlib
import json
import os
import re
import urllib.request
from datetime import datetime
from pathlib import Path
from time import sleep
from typing import Any, Dict

import misaka
import yaml
from docopt import docopt
from personal_mnemonic_medium.exporters.anki.globals import (
    CONFIG,
    Q_TYPE_TAG,
    VERSION_LOG,
)
from personal_mnemonic_medium.exporters.anki.package_generator import PackageGenerator
from personal_mnemonic_medium.markdown_to_ankicard import markdown_to_ankicard
from personal_mnemonic_medium.prompt_extractors.cloze_extractor import (
    ClozePromptExtractor,
)
from personal_mnemonic_medium.prompt_extractors.qa_extractor import QAPromptExtractor
from wasabi import msg

ANKI_CONNECT_URL = "http://localhost:8765"

# helper for creating anki connect requests
def request(action: Any, **params: Any) -> dict[str, Any]:
    return {"action": action, "params": params, "version": 6}


# helper for invoking actions with anki-connect
def invoke(action, **params):
    """Helper for invoking actions with anki-connect
    Args:
        action (string): the action to invoke
    Raises:
        Exception: invalid fields provided
    Returns:
        Any: the response from anki connect
    """
    global ANKI_CONNECT_URL
    requestJson = json.dumps(request(action, **params)).encode("utf-8")
    response = json.load(
        urllib.request.urlopen(urllib.request.Request(ANKI_CONNECT_URL, requestJson)),
    )
    if len(response) != 2:
        raise Exception("response has an unexpected number of fields")
    if "error" not in response:
        raise Exception("response is missing required error field")
    if "result" not in response:
        raise Exception("response is missing required result field")
    if response["error"] is not None:
        raise Exception(response["error"])
    return response["result"]


def anki_connect_is_live():
    global ANKI_CONNECT_URL
    try:
        if urllib.request.urlopen(ANKI_CONNECT_URL).getcode() == 200:
            return True
        else:
            raise Exception
    except Exception:
        return False


# synchronize the deck with markdown
# Borrowed from https://github.com/lukesmurray/markdown-anki-decks/blob/de6556d7ecd2d39335607c05171f8a9c39c8f422/markdown_anki_decks/sync.py#L64
def sync_package(pathToDeckPackage: Path):
    sleep_length = 1

    for i in range(300):
        if anki_connect_is_live():
            sleep(1)  # Sleep for a second to allow ankiconnect to fully start

            pathToDeckPackage = pathToDeckPackage.resolve()
            try:
                invoke("importPackage", path=str(pathToDeckPackage))
                msg.good(f"Imported {pathToDeckPackage}!")
                break
            except Exception as e:
                msg.warn(f"Unable to import {pathToDeckPackage} to anki")
                msg.warn(f"\t{e}")
        else:
            msg.warn(
                f"{i}: Anki connect is not live, sleeping for {sleep_length} seconds",
            )
            sleep(sleep_length)


def field_to_html(field):
    # Math processing
    """
    Need to extract the math in brackets so that it doesn't get markdowned.
    If math is separated with dollar sign it is converted to brackets.
    """
    if CONFIG["dollar"]:
        for (sep, (op, cl)) in [("$$", (r"\\[", r"\\]")), ("$", (r"\\(", r"\\)"))]:
            escaped_sep = sep.replace(r"$", r"\$")
            # ignore escaped dollar signs when splitting the field
            field = re.split(rf"(?<!\\){escaped_sep}", field)
            # add op(en) and cl(osing) brackets to every second element of the list
            field[1::2] = [op + e + cl for e in field[1::2]]
            field = "".join(field)
    else:
        for bracket in ["(", ")", "[", "]"]:
            field = field.replace(rf"\{bracket}", rf"\\{bracket}")
            # backslashes, man.

    for token in ["*", "/"]:
        if token == "/":
            replacement = "*"
        elif token == "*":
            replacement = "**"

        pattern = f"\\{token}[^<>\\-\n]+\\{token}"

        token_instances = re.findall(pattern, field)

        for instance in token_instances:
            field = field.replace(instance, replacement + instance[1:-1] + replacement)

    # Make sure every \n converts into a newline
    field = field.replace("\n", "  \n")

    return misaka.html(field, extensions=("fenced-code", "math"))


def strip_header(string):
    """Strip first occurrence of a markdown level 1 header"""
    return re.sub(r"^#.*\n", "", string)


def compile_field(fieldtext, is_markdown):
    """Turn source markdown into an HTML field suitable for Anki."""
    fieldtext_sans_wiki = fieldtext.replace("[[", "<u>").replace("]]", "</u>")

    fieldtext_sans_headers = strip_header(fieldtext_sans_wiki)

    if is_markdown == 0:
        return fieldtext
    else:
        return field_to_html(fieldtext_sans_headers)


def string_has_cloze(string):
    if (
        len(re.findall(r"{.*}", string)) > 0
        and "BearID" not in string
        and "$$" not in string
    ):
        return True
    return False


def has_qa(string):
    if len(re.findall(r"^(?![:>]).*Q.{0,1}\. ", string, flags=re.DOTALL)) != 0:
        return True
    return False


def is_md_list(string):
    return bool(re.search(r"\d+\.", string))


def encode_string(string):
    return string.replace(" ", "%20").replace("/", "%2F")


def has_subdeck_tag(string):
    return len(re.findall(r"#anki\/deck\/\S+", string)) != 0


def get_first_question(string) -> str:
    """
    Find the Anki question in a string.

    """
    question = re.findall(r"Q.{0,1}\.(?:(?!A\.).)*", string, flags=re.DOTALL)[0]

    return question


def get_first_answer(string) -> str:
    """
    Find the Anki answer in a string.

    Returns:
        String
    """
    # I have to use positive lookahead to match code-blocks - to ensure the last answer is matched as well, I add 2 newlines to string. A little hacky.

    string_padded = f"{string.rstrip()}\n\n"

    answer = re.findall(r"\nA\.[ \n]+\n*.+", string_padded, re.DOTALL)[0]

    return answer


def gen_bear_button_html(filepath):
    bear_base = "bear://x-callback-url/open-note?title="

    filename = os.path.basename(filepath)[:-3]
    file_url = urllib.parse.quote(filename)

    bear_extension = "&show_window=yes&new_window=yes&edit=yes"

    href = bear_base + file_url + bear_extension

    return f'<h4 class="right"><a href="{href}">Bear</a></h4>'


def get_q_type_tag(question_string):
    q_type_letter = re.findall(r"Q\w{0,1}\.", question_string)[0][1]
    return Q_TYPE_TAG[q_type_letter]


def get_content_only(string):
    string_stripped = strip_header(strip_backlinks(string))

    return string_stripped


def complex_hash(text):
    """MD5 of text, mod 2^63. Probably not a great hash function."""
    return int(hashlib.sha256(text.encode("utf-8")).hexdigest(), 16) % 10**15


def line_prepender(filename, line):
    with open(filename, "r+") as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip("\r\n") + "\n" + content)


def add_uid(filepath):
    with open(filepath, encoding="utf8") as f:
        prefix = f.readline()[0:5]
        if prefix != "#####":
            file_id = complex_hash(filepath)
            line_prepender(filepath, "###### " + str(file_id))
            return


def apply_arguments(arguments):
    global CONFIG
    if arguments.get("--configFile") is not None:
        config_file_path = os.path.abspath(
            os.path.expanduser(arguments.get("--configFile")),
        )
        with open(config_file_path) as config_file:
            CONFIG.update(yaml.load(config_file))
    if arguments.get("--config") is not None:
        CONFIG.update(yaml.load(arguments.get("--config")))
    if arguments.get("-p") is not None:
        CONFIG["pkg_arg"] = arguments.get("-p")
    if arguments.get("-r") is not None:
        CONFIG["recur_dir"] = arguments.get("-r")
    if arguments.get("--updatedOnly"):
        CONFIG["updated_only"] = True


def main():
    """Run the thing."""
    apply_arguments(docopt(__doc__, version=VERSION))
    # print(yaml.dump(CONFIG))
    initial_dir = os.getcwd()
    recur_dir = os.path.abspath(os.path.expanduser(CONFIG["recur_dir"]))
    pkg_arg = os.path.abspath(os.path.expanduser(CONFIG["pkg_arg"]))
    version_log = os.path.abspath(os.path.expanduser(CONFIG["version_log"]))

    global IMPORT_TIME
    IMPORT_TIME = "{}".format(
        datetime.now().strftime("%Y.%m/%d_%H:%M"),
    )  # Init as global to avoid each card getting separate times

    cards = markdown_to_ankicard(
        dir_path=recur_dir,
        extractors=[QAPromptExtractor(), ClozePromptExtractor()],
    )
    package_path = PackageGenerator().cards_to_package(cards=cards, output_path=pkg_arg)

    sync_package(package_path)
    os.chdir(initial_dir)

    json.dump(VERSION_LOG, open(version_log, "w"))


if __name__ == "__main__":
    main()
