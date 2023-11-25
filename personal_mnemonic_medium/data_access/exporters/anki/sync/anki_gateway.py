from typing import Any

from genanki import Model
from wasabi import Printer

from personal_mnemonic_medium.data_access.exporters.anki.package_generator import (
    DeckBundle,
)

from .gateway_utils import anki_connect_is_live, invoke

msg = Printer(timestamp=True)


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
