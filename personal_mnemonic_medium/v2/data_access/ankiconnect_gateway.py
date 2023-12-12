# helper for creating anki connect requests
import datetime
import json
import traceback
import urllib.request
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any

import genanki
import pydantic


class AnkiField(pydantic.BaseModel):
    value: str
    order: int


class NoteInfo(pydantic.BaseModel):
    noteId: int
    tags: Sequence[str]
    fields: Mapping[str, AnkiField]
    modelName: str
    cards: Sequence[int]


class AnkiConnectCommand(Enum):
    CARDS_TO_NOTES = "cardsToNotes"
    DELETE_NOTES = "deleteNotes"
    FIND_CARDS = "findCards"
    GET_NOTE_INFOS = "notesInfo"
    IMPORT_PACKAGE = "importPackage"
    UPDATE_MODEL_TEMPLATES = "updateModelTemplates"
    UPDATE_MODEL_STYLING = "updateModelStyling"


class AnkiConnectGateway:
    def __init__(self, ankiconnect_url: str, deck_name: str) -> None:
        self.ankiconnect_url = ankiconnect_url
        self.deck_name = deck_name

    def update_model(self, model: genanki.Model) -> None:
        self._invoke(
            AnkiConnectCommand.UPDATE_MODEL_TEMPLATES,
            model={
                "name": model.name,  # type: ignore
                "templates": {
                    t["name"]: {"qfmt": t["qfmt"], "afmt": t["afmt"]}
                    for t in model.templates  # type: ignore
                },
            },
        )
        self._invoke(
            AnkiConnectCommand.UPDATE_MODEL_STYLING,
            model={"name": model.name, "css": model.css},  # type: ignore
        )

    def import_package(
        self,
        package: genanki.Package,
        tmp_write_dir: Path,
        tmp_read_dir: Path,
    ) -> None:
        apkg_name = f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.apkg"
        write_path = tmp_write_dir / apkg_name
        package.write_to_file(write_path)  # type: ignore

        read_path = tmp_read_dir / apkg_name
        try:
            self._invoke(
                AnkiConnectCommand.IMPORT_PACKAGE, path=str(read_path)
            )
            print(f"Imported from {read_path}!")
            write_path.unlink()
        except Exception:
            print(f"""Unable to sync from {read_path}.""")
            traceback.print_exc()

    def delete_notes(self, note_ids: Sequence[int]) -> None:
        self._invoke(AnkiConnectCommand.DELETE_NOTES, notes=note_ids)

    def get_all_note_infos(self) -> Sequence[NoteInfo]:
        anki_card_ids: list[int] = self._invoke(
            AnkiConnectCommand.FIND_CARDS,
            query=f'"deck:{self.deck_name}"',
        )

        # get a list of anki notes in the deck
        anki_note_ids: list[int] = self._invoke(
            AnkiConnectCommand.CARDS_TO_NOTES, cards=anki_card_ids
        )

        # get the note info for the notes in the deck
        anki_notes_info: list[dict[str, Any]] = self._invoke(
            AnkiConnectCommand.GET_NOTE_INFOS, notes=anki_note_ids
        )

        return [NoteInfo(**info) for info in anki_notes_info]

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
        if response["error"] is not None:
            raise Exception(response["error"])
        return response["result"]


@dataclass(frozen=True)
class FakeAnkiCommand:
    ...


@dataclass(frozen=True)
class ImportPackage(FakeAnkiCommand):
    package: genanki.Package
    tmp_write_dir: Path
    tmp_read_dir: Path


@dataclass(frozen=True)
class UpdateModel(FakeAnkiCommand):
    model: genanki.Model


class SpieAnkiconnectGateway(AnkiConnectGateway):
    def __init__(self, note_infos: Sequence[NoteInfo] = ()) -> None:
        self.deck_name = "FakeDeck"
        self.note_infos: list[NoteInfo] = list(note_infos)
        self.executed_commands: list[FakeAnkiCommand] = []

    def get_all_note_infos(self) -> Sequence[NoteInfo]:
        return self.note_infos

    def update_model(self, model: genanki.Model) -> None:
        self.executed_commands.append(UpdateModel(model=model))

    def import_package(
        self,
        package: genanki.Package,
        tmp_write_dir: Path,
        tmp_read_dir: Path,
    ) -> None:
        self.executed_commands.append(
            ImportPackage(
                package=package,
                tmp_write_dir=tmp_write_dir,
                tmp_read_dir=tmp_read_dir,
            )
        )
