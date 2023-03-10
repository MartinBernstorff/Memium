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
import tempfile
from datetime import datetime
from pathlib import Path
from shutil import copyfile
from time import sleep

import genanki
import misaka
import yaml
from docopt import docopt
from personal_mnemonic_medium.globals import *
from tqdm import tqdm
from wasabi import msg


def simple_hash(text):
    """MD5 of text, mod 2^63. Probably not a great hash function."""
    hash = int(hashlib.sha256(text.encode("utf-8")).hexdigest(), 16) % 10**10

    return hash


import json
import typing as t
import urllib.request
from pathlib import Path

from genanki import Model

anki_connect_url = "http://localhost:8765"

# helper for creating anki connect requests
def request(action, **params):
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
    global anki_connect_url
    requestJson = json.dumps(request(action, **params)).encode("utf-8")
    response = json.load(
        urllib.request.urlopen(urllib.request.Request(anki_connect_url, requestJson))
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
    global anki_connect_url
    try:
        if urllib.request.urlopen(anki_connect_url).getcode() == 200:
            return True
        else:
            raise Exception()
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
                f"{i}: Anki connect is not live, sleeping for {sleep_length} seconds"
            )
            sleep(sleep_length)


class Card(object):
    """A single anki card."""

    def __init__(self, filepath):
        self.fields = []
        self.source_markdown = []
        self.filepath = filepath
        self.tags = []

    def append_tags(self, tags):
        self.tags.extend(tags)

    def deckdir(self):
        return os.path.dirname(self.filepath)

    def set_deck(self, subdeck):
        self.subdeck = subdeck

    def set_model(self, model_type="Cloze"):
        self.model_type = model_type

        if model_type == "Cloze":
            self.model = genanki.Model(
                model_id=simple_hash(CONFIG["card_model_name_cloze"]),
                name=CONFIG["card_model_name_cloze"],
                fields=CONFIG["card_model_fields_cloze"],
                templates=CONFIG["card_model_template_cloze"],
                css=CONFIG["card_model_css"],
                model_type=1,  # This is the model_type number for genanki, takes 0 for QA or 1 for cloze
            )
        elif model_type == "QA":
            self.model = genanki.Model(
                model_id=simple_hash(CONFIG["card_model_name_qa"]),
                name=CONFIG["card_model_name_qa"],
                fields=CONFIG["card_model_fields_qa"],
                templates=CONFIG["card_model_template_qa"],
                css=CONFIG["card_model_css"],
                model_type=0,
            )
        elif model_type == "QA_DA":
            self.model = genanki.Model(
                model_id=simple_hash(CONFIG["card_model_name_qa_da"]),
                name=CONFIG["card_model_name_qa_da"],
                fields=CONFIG["card_model_fields_qa"],
                templates=CONFIG["card_model_template_qa_da"],
                css=CONFIG["card_model_css"],
                model_type=0,
            )
        else:
            raise ValueError("model_type must be either Cloze or QA")

    def deckname(self):
        try:
            if len(self.subdeck) > 0:
                return (
                    "0. Don't click me::1. Active::Personal Mnemonic Medium::"
                    + self.subdeck
                )
            else:
                raise ValueError(
                    "Subdeck length is 0"
                )  # This is purposefully non-valid code
        except:
            return "0. Don't click me::1. Active::Personal Mnemonic Medium"

    def basename(self):
        with open(self.filepath, "r", encoding="utf8") as file:
            full_string = ""

            for line in file.readlines():
                full_string += line

            uid = re.findall(r"<!-- {BearID:.+} -->", full_string)[0]
            return uid

    def card_id(self):  # The identifier for cards
        if len(re.findall(r"{(?!BearID).[^}]*}", self.fields[0])) > 0:
            # Excludes bearID. We don't want clozes to update just because the surrounding information did.
            cloze = re.findall(r"{(?!BearID).[^}]*}", self.fields[0])[0]
            basename = self.basename()
            hash_value = simple_hash(f"{cloze}{basename}")

            return hash_value

        else:  # If not cloze
            # Q/A cards should be unique from their phrasing. Now it's not tied to a given note.
            hash_string = self.source_markdown[0]

            hash = simple_hash(f"{hash_string}")
            return hash

    def guid(self):  # The identifier for notes
        return (
            self.card_id()
        )  # This is now the hash of the BearID and the cloze or question side

    def add_field(self, field, is_markdown=True):
        self.fields.append(compile_field(field, is_markdown))
        self.source_markdown.append(field)

    def has_cloze(self):
        return len(self.fields) > 0 and any("{" in s for s in self.fields)

    def has_front_and_back(self):
        return len(self.fields) >= 2

    def finalize(self):
        """Ensure proper shape, for extraction into result formats."""
        if len(self.fields) > 3:
            self.fields = self.fields[:3]
        else:
            while len(self.fields) < 3:
                self.fields.append("")

    def to_genanki_note(self):
        """Produce a genanki.Note with the specified guid."""
        return genanki.Note(
            model=self.model, fields=self.fields, guid=self.guid(), tags=self.tags
        )

    def make_ref_pair(self, filename):
        """Take a filename relative to the card, and make it absolute."""
        newname = "%".join(filename.split(os.sep))

        if os.path.isabs(filename):
            abspath = filename
        else:
            abspath = os.path.normpath(os.path.join(self.deckdir(), filename))
        return (abspath, newname)

    def determine_media_references(self):
        """Find all media references in a card"""
        for i, field in enumerate(self.fields):
            current_stage = field
            for regex in [
                r'src="([^"]*?)"'
            ]:  # TODO not sure how this should work:, r'\[sound:(.*?)\]']:
                results = []

                def process_match(m):
                    initial_contents = m.group(1)
                    abspath, newpath = self.make_ref_pair(initial_contents)
                    results.append((abspath, newpath))
                    return r'src="' + newpath + '"'

                current_stage = re.sub(regex, process_match, current_stage)

                for r in results:
                    yield r

            # Anki seems to hate alt tags :(
            self.fields[i] = re.sub(r'alt="[^"]*?"', "", current_stage)


class DeckCollection(dict):
    """Defaultdict for decks, but with stored name."""

    def __getitem__(self, deckname):
        if deckname not in self:
            deck_id = simple_hash(deckname)
            self[deckname] = genanki.Deck(deck_id, deckname)
        return super(DeckCollection, self).__getitem__(deckname)


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
            field = re.split(r"(?<!\\){}".format(escaped_sep), field)
            # add op(en) and cl(osing) brackets to every second element of the list
            field[1::2] = [op + e + cl for e in field[1::2]]
            field = "".join(field)
    else:
        for bracket in ["(", ")", "[", "]"]:
            field = field.replace(r"\{}".format(bracket), r"\\{}".format(bracket))
            # backslashes, man.

    for token in ["*", "/"]:
        if token == "/":
            replacement = "*"
        elif token == "*":
            replacement = "**"

        pattern = "\{}[^<>\-\n]+\{}".format(token, token)

        token_instances = re.findall(pattern, field)

        for instance in token_instances:
            field = field.replace(instance, replacement + instance[1:-1] + replacement)

    # Make sure every \n converts into a newline
    field = field.replace("\n", "  \n")

    return misaka.html(field, extensions=("fenced-code", "math"))


def replace_cloze_id_with_unique(string, selected_cloze=None):
    if selected_cloze is not None:
        selected_clozes = [selected_cloze]
    else:
        selected_clozes = re.findall(r"{(?!BearID).[^}]*}", string)

    for cloze in selected_clozes:
        hash = int(hashlib.sha256(cloze.encode("utf-8")).hexdigest(), 16) % 10**3

        new_cloze = f"{{{{c{hash}::{cloze[1:-1]}}}}}"

        string = string.replace(cloze, new_cloze)

    return string


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


def get_subdeck_name(string):
    return (
        re.findall(r"#anki\/deck\/\S+", string)[0][11:]
        .replace("/", "::")
        .replace("#", "")
    )


def has_supplementary_tags(string):
    return len(re.findall(r"#anki\/tag\/\S+", string)) != 0


def gen_file_tags(string, import_time):
    file_tags = [import_time]

    if has_supplementary_tags(string):
        for tag in re.findall(r"#anki\/tag\/\S+", string):
            file_tags.append(tag[10:])

    return file_tags


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
    # I have to use positive lookahead to match code-blocks – to ensure the last answer is matched as well, I add 2 newlines to string. A little hacky.

    string_padded = f"{string.rstrip()}\n\n"

    answer = re.findall(r"\nA\.[ \n]+\n*.+", string_padded, re.DOTALL)[0]

    return answer


def break_string_by_two_or_more_newlines(string):
    """
    Break string into a list every time there are at least two newlines in a row.
    """
    return re.split(r"(\n\n)+", string)


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


def produce_qa_card_from_block(
    filepath, subdeck, file_tags: list, block_string, extra_string
):
    current_card = Card(filepath)

    question_string = get_first_question(block_string)
    answer_string = get_first_answer(block_string)

    # Metadata handling
    current_card.set_deck(subdeck)

    question_type_tag = get_q_type_tag(question_string)

    file_tags.append(question_type_tag)  # Handle the "I" in "QI."

    current_card.append_tags(file_tags)

    # Content handling
    question_content = re.sub(r"Q.{0,1}\.", "", question_string)
    answer_content = answer_string[4:]

    for field_content in [question_content, answer_content]:
        current_card.add_field(field_content)

    current_card.add_field(extra_string, is_markdown=False)

    if subdeck == "Medicine" or subdeck == "Danish":
        current_card.set_model("QA_DA")
    else:
        current_card.set_model("QA")

    return current_card


def produce_cloze_cards_from_block(
    filepath: str, subdeck: str, file_tags: list, block_string: str, extra_string: str
) -> list:
    clozes = re.findall(r"{(?!BearID).[^}]*}", block_string)

    cards = []

    for selected_cloze in clozes:
        current_card = Card(filepath)

        # Metadata handling
        current_card.set_model("Cloze")
        current_card.set_deck(subdeck)
        current_card.append_tags(file_tags)

        # Content handling
        """Create one note for each cloze to only updates note if the cloze itself has changed, not its surrounding clozes"""
        card_string = replace_cloze_id_with_unique(
            block_string, selected_cloze=selected_cloze
        )

        # Remove the unused-clozes from the card
        non_selected_clozes = re.findall(r"{(?!BearID)(?!{)(?!c\d).[^}]*}", card_string)

        for non_selected_cloze in non_selected_clozes:
            card_string = card_string.replace(
                non_selected_cloze, non_selected_cloze[1:-1]
            )

        current_card.add_field(card_string)
        current_card.add_field(extra_string, is_markdown=False)

        cards.append(current_card)

    return cards


def strip_header(string):
    """Strip first occurrence of a markdown level 1 header"""
    return re.sub(r"^#.*\n", "", string)


def strip_backlinks(string):
    """Strip anything showing up after ## Backlinks"""

    return re.sub(r"## Backlinks.*", "", string, flags=re.DOTALL)


def get_content_only(string):
    string_stripped = strip_header(strip_backlinks(string))

    return string_stripped


def produce_cards_from_file(filepath: str, import_time):
    """
    Parameters:
        Filename as a string
    Returns:
        A generator yielding genanki cards
    """

    with open(filepath, "r", encoding="utf8") as f:
        file_string = f.read()

        # Metadata handling
        if has_subdeck_tag(file_string):
            subdeck = get_subdeck_name(file_string)
        else:
            subdeck = "Default"

        file_tags = gen_file_tags(file_string, import_time)

        extra_string = gen_bear_button_html(filepath)

        # Content
        content_string = get_content_only(file_string)

        blocks = break_string_by_two_or_more_newlines(content_string)

        for block_string in blocks:
            # QA processing
            if has_qa(block_string):
                card = produce_qa_card_from_block(
                    filepath, subdeck, file_tags, block_string, extra_string
                )
                yield card

            elif string_has_cloze(block_string):
                cards = produce_cloze_cards_from_block(
                    filepath, subdeck, file_tags, block_string, extra_string
                )

                for card in cards:
                    yield card


def complex_hash(text):
    """MD5 of text, mod 2^63. Probably not a great hash function."""
    return int(hashlib.sha256(text.encode("utf-8")).hexdigest(), 16) % 10**15


def add_uid(filepath):
    with open(filepath, "r", encoding="utf8") as f:
        prefix = f.readline()[0:5]
        if prefix != "#####":
            file_id = complex_hash(filepath)
            line_prepender(filepath, "###### " + str(file_id))
            return


def line_prepender(filename, line):
    with open(filename, "r+") as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip("\r\n") + "\n" + content)


def produce_cards_from_dir(dirname):
    """Walk a directory and produce the cards found there, one by one."""
    global VERSION_LOG
    global CONFIG

    for parent_dir, _, files in os.walk(dirname):
        with tqdm(total=len(files)) as pbar:
            for file_name in sorted(files):
                if file_name.endswith(".md") or file_name.endswith(".markdown"):
                    filepath = os.path.join(parent_dir, file_name)

                    try:
                        for card in produce_cards_from_file(
                            filepath, import_time=IMPORT_TIME
                        ):
                            yield card
                        pbar.update(1)
                    except:
                        # Didn't yield any cards
                        pbar.update(1)
                        continue


def cards_to_package(cards, output_name):
    """Take an iterable of the cards, and put a .apkg in a file called output_name.

    NOTE: We _must_ be in a temp directory.
    """
    decks = DeckCollection()

    media = set()

    for card in cards:
        card.finalize()
        for abspath, newpath in card.determine_media_references():
            copyfile(
                abspath, newpath
            )  # This is inefficient but definitely works on all platforms.
            media.add(newpath)
        decks[card.deckname()].add_note(card.to_genanki_note())

    if len(decks) == 0:
        msg.warn("No decks generated")

    package = genanki.Package(deck_or_decks=decks.values(), media_files=list(media))

    if output_name:
        package.write_to_file(output_name)

    return package


def apply_arguments(arguments):
    global CONFIG
    if arguments.get("--configFile") is not None:
        config_file_path = os.path.abspath(
            os.path.expanduser(arguments.get("--configFile"))
        )
        with open(config_file_path, "r") as config_file:
            CONFIG.update(yaml.load(config_file))
    if arguments.get("--config") is not None:
        CONFIG.update(yaml.load(arguments.get("--config")))
    if arguments.get("-p") is not None:
        CONFIG["pkg_arg"] = arguments.get("-p")
    if arguments.get("-r") is not None:
        CONFIG["recur_dir"] = arguments.get("-r")
    if arguments.get("--updatedOnly"):
        CONFIG["updated_only"] = True


def load_version_log(version_log):
    global VERSION_LOG
    if os.path.exists(version_log):
        VERSION_LOG = json.load(open(version_log, "r"))


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
        datetime.now().strftime("%Y.%m/%d_%H:%M")
    )  # Init as global to avoid each card getting separate times

    load_version_log(version_log)

    with tempfile.TemporaryDirectory() as tmpdirname:
        os.chdir(tmpdirname)  # genanki is very opinionated about where we are.

        card_iterator = produce_cards_from_dir(recur_dir)
        package = cards_to_package(card_iterator, output_name=pkg_arg)

        sync_package(Path(pkg_arg))

        os.chdir(initial_dir)

    json.dump(VERSION_LOG, open(version_log, "w"))


if __name__ == "__main__":
    exit(main())
