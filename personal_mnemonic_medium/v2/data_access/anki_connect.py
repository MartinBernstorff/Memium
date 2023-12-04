# helper for creating anki connect requests
import json
import traceback
import urllib.request
from collections.abc import Sequence
from enum import Enum
from pathlib import Path
from typing import Any

import genanki
import pydantic

from personal_mnemonic_medium.data_access.exporters.anki.globals import (
    ANKICONNECT_URL,
)

from ...data_access.exporters.anki.card_types.base import AnkiCard


class NoteInfo(pydantic.BaseModel):
    ...


class AnkiConnectCommand(Enum):
    CARDS_TO_NOTES = "cardsToNotes"
    DELETE_NOTES = "deleteNotes"
    FIND_CARDS = "findCards"
    GET_NOTE_INFOS = "notesInfo"
    IMPORT_PACKAGE = "importPackage"


class AnkiConnectGateway:
    def __init__(
        self, ankiconnect_url: str = ANKICONNECT_URL
    ) -> None:
        self.ankiconnect_url = ankiconnect_url

    def import_cards(
        self, cards: Sequence[AnkiCard], tmp_path: Path
    ) -> None:
        decks = {c.subdeck for c in cards}
        package = genanki.Package(deck_or_decks=decks, media_files=[])

        output_path = tmp_path / "anki_package.apkg"
        package.write_to_file(output_path)  # type: ignore

        try:
            self._invoke(
                AnkiConnectCommand.IMPORT_PACKAGE, path=output_path
            )
            print(f"Imported from {output_path}!")
        except Exception:
            print(
                f"""Unable to sync from {output_path}.
"""
            )
            traceback.print_exc()

        # Delete the package after importing it
        output_path.unlink()

    def delete_notes(self, note_ids: Sequence[Any]) -> None:
        self._invoke(AnkiConnectCommand.DELETE_NOTES, notes=note_ids)

    def get_note_infos(self, deck_name: str) -> Sequence[NoteInfo]:
        anki_card_ids: list[int] = self._invoke(
            AnkiConnectCommand.FIND_CARDS, query=f'"deck:{deck_name}"'
        )

        # get a list of anki notes in the deck
        anki_note_ids: list[int] = self._invoke(
            AnkiConnectCommand.CARDS_TO_NOTES, cards=anki_card_ids
        )

        # get the note info for the notes in the deck
        anki_notes_info = self._invoke(
            AnkiConnectCommand.GET_NOTE_INFOS, notes=anki_note_ids
        )

        # convert the note info into a dictionary of guid to note info
        guid2note_info = {
            info["fields"]["UUID"]["value"]
            .replace("<p>", "")
            .replace("</p>", "")
            .strip(): info
            for info in anki_notes_info
        }
        return [NoteInfo(**info) for info in guid2note_info.values()]

    def _request(self, action: Any, **params: Any) -> dict[str, Any]:
        return {"action": action, "params": params, "version": 6}

    def _invoke(
        self, action: AnkiConnectCommand, **params: Any
    ) -> Any:
        """Helper for invoking actions with anki-connect
        Args:
            action (string): the action to invoke
        Raises:
            Exception: invalid fields provided
        Returns:
            Any: the response from anki connect
        """
        requestJson = json.dumps(
            self._request(action.value, **params)
        ).encode("utf-8")
        response = json.load(
            urllib.request.urlopen(
                urllib.request.Request(
                    self.ankiconnect_url, requestJson
                )
            )
        )
        if len(response) != 2:
            raise Exception(
                "response has an unexpected number of fields"
            )
        if "error" not in response:
            raise Exception(
                "response is missing required error field"
            )
        if "result" not in response:
            raise Exception(
                "response is missing required result field"
            )
        if response["error"] is not None:
            raise Exception(response["error"])
        return response["result"]
