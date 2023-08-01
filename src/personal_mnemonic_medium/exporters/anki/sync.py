import json
import traceback
import urllib.request
from pathlib import Path
from time import sleep
from typing import Any, Dict, List

from genanki import Model, Note

from personal_mnemonic_medium.exporters.anki.package_generator import DeckBundle

anki_connect_url = "http://localhost:8765"

from wasabi import Printer

msg = Printer(timestamp=True)


# helper for creating anki connect requests
def request(action: Any, **params: Any) -> Dict[str, Any]:
    return {"action": action, "params": params, "version": 6}


# helper for invoking actions with anki-connect
def invoke(action: Any, **params: Any) -> Any:
    """Helper for invoking actions with anki-connect
    Args:
        action (string): the action to invoke
    Raises:
        Exception: invalid fields provided
    Returns:
        Any: the response from anki connect
    """
    requestJson = json.dumps(request(action, **params)).encode("utf-8")
    response = json.load(
        urllib.request.urlopen(urllib.request.Request(anki_connect_url, requestJson)),
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
    try:
        if urllib.request.urlopen(anki_connect_url).getcode() == 200:
            return True
        raise Exception
    except Exception:
        msg.good(
            "Unable to reach anki connect. Make sure anki is running and the Anki Connect addon is installed.",
        )

    return False


# synchronize the deck with markdown
# Borrowed from https://github.com/lukesmurray/markdown-anki-decks/blob/de6556d7ecd2d39335607c05171f8a9c39c8f422/markdown_anki_decks/sync.py#L64
def sync_deck(deck_bundle: DeckBundle, dir_path: Path, delete_cards: bool = True):
    for _ in range(600):
        if anki_connect_is_live():
            break
        print("Waiting for anki connect to start...")
        sleep(0.5)

    package_path = deck_bundle.save_deck_to_file(dir_path / "deck.apkg")

    try:
        invoke("importPackage", path=str(package_path))
        print(f"Imported {package_path}!")

        if delete_cards:
            # delete removed cards
            try:
                # get a list of anki cards in the deck
                anki_card_ids: List[int] = invoke(
                    "findCards",
                    query=f'"deck:{deck_bundle.deck.name}"',
                )

                # get a list of anki notes in the deck
                anki_note_ids: List[int] = invoke("cardsToNotes", cards=anki_card_ids)

                # get the note info for the notes in the deck
                anki_notes_info = invoke("notesInfo", notes=anki_note_ids)

                # convert the note info into a dictionary of guid to note info
                anki_note_info_by_guid = {
                    n["fields"]["UUID"]["value"]
                    .replace("<p>", "")
                    .replace("</p>", "")
                    .strip(): n
                    for n in anki_notes_info
                }

                # get the unique guids of the anki notes
                anki_note_guids = anki_note_info_by_guid.keys()

                # get the unique guids of the md notes
                md_notes: List[Note] = deck_bundle.deck.notes
                md_note_guids = {str(n.guid) for n in md_notes}

                # find the guids to delete
                guids_to_delete = anki_note_guids - md_note_guids

                if guids_to_delete:
                    invoke(
                        "deleteNotes",
                        notes=[
                            anki_note_info_by_guid[g]["noteId"] for g in guids_to_delete
                        ],
                    )
                    msg.good(f"Deleted {len(guids_to_delete)} notes")
            except Exception:
                msg.fail(f"Unable to delete cards in {deck_bundle.deck.name}")
                # Print full stack trace
                traceback.print_exc()

    except Exception as e:
        print(f"Unable to import {package_path} to anki")
        print(f"\t{e}")


# synchronize the model and styling in the deck
def sync_model(model: Model):
    model_names_to_ids = {}
    try:
        model_names_to_ids = invoke("modelNamesAndIds")
        if model.name not in model_names_to_ids:
            return
    except Exception as e:
        msg.good("\tUnable to fetch existing model names and ids from anki")
        msg.good(f"\t\t{e}")

    if anki_connect_is_live():
        try:
            invoke(
                "updateModelTemplates",
                model={
                    "name": model.name,
                    "templates": {
                        t["name"]: {
                            "qfmt": t["qfmt"],
                            "afmt": t["afmt"],
                        }
                        for t in model.templates
                    },
                },
            )
            msg.good(f"\tUpdated model {model.name} template")
        except Exception as e:
            msg.good(f"\tUnable to update model {model.name} template")
            msg.good(f"\t\t{e}")

        try:
            invoke(
                "updateModelStyling",
                model={
                    "name": model.name,
                    "css": model.css,
                },
            )
            msg.good(f"\tUpdated model {model.name} css")
        except Exception as e:
            msg.good(f"\tUnable to update model {model.name} css")
            msg.good(f"\t\t{e}")
