import traceback
from collections import defaultdict
from collections.abc import Sequence
from pathlib import Path
from time import sleep
from typing import Any

from genanki import Model
from wasabi import Printer

from personal_mnemonic_medium.data_access.exporters.anki.card_types.base import (
    AnkiCard,
)
from personal_mnemonic_medium.data_access.exporters.anki.package_generator import (
    AnkiPackageGenerator,
    DeckBundle,
)
from personal_mnemonic_medium.data_access.exporters.anki.sync.gateway.ankiconnect_utils import (
    AnkiConnectParams,
    anki_connect_is_live,
    invoke,
)

msg = Printer(timestamp=True)

# TODO: refactor: add ankiconnect gateway for injection


# synchronize the deck with markdown
# Borrowed from https://github.com/lukesmurray/markdown-anki-decks/blob/de6556d7ecd2d39335607c05171f8a9c39c8f422/markdown_anki_decks/sync.py#L64
def sync_deck(
    cards: Sequence[AnkiCard],
    anki_connect: AnkiConnectParams | None,
    local_output_dir: Path,
):
    # TODO: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues/210 feat: log which cards are added to disk

    deck_bundle = AnkiPackageGenerator().cards_to_deck_bundle(
        cards=cards
    )

    if "Medicine" in deck_bundle.deck.name:  # type: ignore
        msg.fail("Skipping Medicine deck to save resources")
        return

    if anki_connect:
        for _ in range(anki_connect.max_wait_seconds):
            if anki_connect_is_live():
                break
            print("Waiting for anki connect to start...")
            sleep(secs=0.5)
        else:
            msg.fail("Unable to connect to anki")
            return

        # get a list of anki cards in the deck
        anki_note_info_by_guid = get_anki_server_guid2noteinfo(
            deck_bundle
        )
        anki_note_guids: set[str] = set(anki_note_info_by_guid.keys())
    else:
        anki_note_info_by_guid = None
        anki_note_guids: set[str] = set()

    # get the unique guids of the md notes
    md_note_guids = deck_bundle.note_guids()

    note_diff = md_note_guids.symmetric_difference(anki_note_guids)

    if note_diff:
        _sync_deck(
            deck_bundle=deck_bundle,
            apkg_output_filepath=local_output_dir,
            anki_connect=anki_connect,
            anki_note_info_by_guid=anki_note_info_by_guid,
            anki_note_guids=anki_note_guids,
            md_note_guids=md_note_guids,
        )
    else:
        msg.info("Skipped")
        msg.info(f"{deck_bundle.deck.name}")  # type: ignore
        msg.info("\tNo notes added or removed")
        print("\n")


def _sync_deck(
    deck_bundle: DeckBundle,
    apkg_output_filepath: Path,
    anki_connect: AnkiConnectParams | None,
    anki_note_info_by_guid: dict[str, Any] | None,
    anki_note_guids: set[str],
    md_note_guids: set[str],
):
    msg.info(" Syncing deck: ")
    msg.info(f"\t{deck_bundle.deck.name}")  # type: ignore

    msg.info(f"Anki note guids: {anki_note_guids}")
    msg.info(f".md note guids: {md_note_guids}")

    added_note_guids = md_note_guids - anki_note_guids
    if added_note_guids:
        msg.info("\tNotes added: ")
        msg.info(f"\t\t{added_note_guids}")

    removed_note_guids = anki_note_guids - md_note_guids
    if removed_note_guids:
        msg.info("\tNotes removed: ")
        msg.info(f"\t\t{removed_note_guids}")

    msg.info(f"Saving deck to {apkg_output_filepath}")
    package_path = deck_bundle.save_deck_to_file(apkg_output_filepath)
    if anki_connect:
        try:
            sync_path = str(anki_connect.apkg_dir / "deck.apkg")
            invoke("importPackage", path=sync_path)
            print(f"Imported {deck_bundle.deck.name}!")  # type: ignore

            if anki_connect.delete_cards:
                try:
                    guids_to_delete = anki_note_guids - md_note_guids
                    if guids_to_delete:
                        note_ids = [  # type: ignore
                            anki_note_info_by_guid[guid]["noteId"]  # type: ignore
                            for guid in guids_to_delete
                        ]

                        invoke("deleteNotes", notes=note_ids)
                        msg.good(
                            f"Deleted {len(guids_to_delete)} notes"
                        )

                except Exception:
                    msg.fail(
                        f"Unable to delete cards in {deck_bundle.deck.name}"  # type: ignore
                    )
                    # Print full stack trace
                    traceback.print_exc()
        except Exception as e:
            print(f"Unable to sync {package_path} to anki")
            print(f"{e}")
            traceback.print_exc()


# TODO: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues/272 refactor: create pydantic class for noteinfo
def get_anki_server_guid2noteinfo(
    deck_bundle: DeckBundle
) -> dict[str, Any]:
    anki_card_ids: list[int] = invoke(
        "findCards",
        query=f'"deck:{deck_bundle.deck.name}"',  # type: ignore
    )

    # get a list of anki notes in the deck
    anki_note_ids: list[int] = invoke(
        "cardsToNotes", cards=anki_card_ids
    )

    # get the note info for the notes in the deck
    anki_notes_info = invoke("notesInfo", notes=anki_note_ids)

    # convert the note info into a dictionary of guid to note info
    guid2note_info = {
        info["fields"]["UUID"]["value"]
        .replace("<p>", "")
        .replace("</p>", "")
        .strip(): info
        for info in anki_notes_info
    }
    return guid2note_info


# synchronize the model and styling in the deck
def sync_model(model: Model):
    model_names_to_ids = {}
    try:
        model_names_to_ids = invoke("modelNamesAndIds")
        if model.name not in model_names_to_ids:  # type: ignore
            return
    except Exception as e:
        msg.good(
            "\tUnable to fetch existing model names and ids from anki"
        )
        msg.good(f"\t\t{e}")

    if anki_connect_is_live():
        try:
            invoke(
                "updateModelTemplates",
                model={
                    "name": model.name,  # type: ignore
                    "templates": {
                        t["name"]: {
                            "qfmt": t["qfmt"],
                            "afmt": t["afmt"],
                        }
                        for t in model.templates  # type: ignore
                    },
                },
            )
            msg.good(f"\tUpdated model {model.name} template")  # type: ignore
        except Exception as e:
            msg.good(
                f"\tUnable to update model {model.name} template"  # type: ignore
            )
            msg.good(f"\t\t{e}")

        try:
            invoke(
                "updateModelStyling",
                model={"name": model.name, "css": model.css},  # type: ignore
            )
            msg.good(f"\tUpdated model {model.name} css")  # type: ignore
        except Exception as e:
            msg.good(f"\tUnable to update model {model.name} css")  # type: ignore
            msg.good(f"\t\t{e}")


# TODO: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues/240 refactor: sync decks into functional core, imperative shell
def sync_decks(
    local_output_dir: Path,
    anki_connect: AnkiConnectParams | None,
    cards: Sequence[AnkiCard],
):
    decks = _cards_to_decks(cards)

    for cards in decks.values():
        sync_deck(
            cards=cards,
            anki_connect=anki_connect,
            local_output_dir=local_output_dir,
        )


def _cards_to_decks(
    cards: Sequence[AnkiCard]
) -> dict[str, list[AnkiCard]]:
    decks: dict[str, list[AnkiCard]] = defaultdict(list)

    for card in cards:
        decks[card.deckname] += [card]

    return decks
