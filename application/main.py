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
from typing import Any, Dict, Union

import misaka
import yaml  # type: ignore
from docopt import docopt
from personal_mnemonic_medium.exporters.anki.globals import (
    CONFIG,
    Q_TYPE_TAG,
    VERSION,
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
def invoke(action: Any, **params: Any) -> Any:
    """Helper for invoking actions with anki-connect
    Args:
        action (string: str): the action to invoke
    Raises:
        Exception: invalid fields provided
    Returns:
        Any: the response from anki connect
    """
    global ANKI_CONNECT_URL  # noqa
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


def anki_connect_is_live() -> bool:
    global ANKI_CONNECT_URL  # noqa
    try:
        if urllib.request.urlopen(ANKI_CONNECT_URL).getcode() == 200:
            return True
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


def apply_arguments(arguments: Any) -> None:
    global CONFIG  # noqa
    if arguments.get("--configFile") is not None:
        config_file_path = Path.resolve(
            Path.expanduser(arguments.get("--configFile")),
        )
        with Path(config_file_path).open() as config_file:
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
    initial_dir = Path.getcwd()
    recur_dir = Path.resolve(Path.expanduser(CONFIG["recur_dir"]))
    pkg_arg = Path.resolve(Path.expanduser(CONFIG["pkg_arg"]))
    version_log = Path.resolve(Path.expanduser(CONFIG["version_log"]))

    global IMPORT_TIME  # noqa
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

    json.dump(VERSION_LOG, Path(version_log).open("w"))


if __name__ == "__main__":
    main()
