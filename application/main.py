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

import json
import os
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict

from docopt import docopt
from personal_mnemonic_medium.exporters.anki.globals import (
    CONFIG,
    VERSION,
    VERSION_LOG,
)
from personal_mnemonic_medium.exporters.anki.package_generator import PackageGenerator
from personal_mnemonic_medium.exporters.anki.sync import sync_deck
from personal_mnemonic_medium.markdown_to_ankicard import markdown_to_ankicard
from personal_mnemonic_medium.prompt_extractors.cloze_extractor import (
    ClozePromptExtractor,
)
from personal_mnemonic_medium.prompt_extractors.qa_extractor import QAPromptExtractor

ANKI_CONNECT_URL = "http://localhost:8765"

from wasabi import Printer

msg = Printer(timestamp=True)


# helper for creating anki connect requests
def request(action: Any, **params: Any) -> Dict[str, Any]:
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


def apply_arguments(arguments: Any) -> None:
    global CONFIG  # noqa
    if arguments.get("-p") is not None:
        CONFIG["pkg_arg"] = arguments.get("-p")
    if arguments.get("-r") is not None:
        CONFIG["recur_dir"] = arguments.get("-r")
    if arguments.get("--updatedOnly"):
        CONFIG["updated_only"] = True


def main():
    """Run the thing."""
    apply_arguments(docopt(__doc__, version=VERSION))
    initial_dir = Path(__file__).parent
    recur_dir = Path(CONFIG["recur_dir"])
    version_log = Path(CONFIG["version_log"])

    cards = markdown_to_ankicard(
        dir_path=recur_dir,
        extractors=[QAPromptExtractor(), ClozePromptExtractor()],
    )

    decks = defaultdict(list)

    for card in cards:
        decks[card.deckname] += [card]

    for deck in decks:
        deck_bundle = PackageGenerator().cards_to_deck_bundle(cards=decks[deck])
        sync_deck(deck_bundle=deck_bundle, dir_path=initial_dir)

    os.chdir(initial_dir)
    json.dump(VERSION_LOG, Path(version_log).open("w"))


if __name__ == "__main__":
    main()
