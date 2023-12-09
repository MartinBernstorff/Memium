from collections.abc import Mapping, Sequence
from pathlib import Path

import genanki
import pytest

from ...data_access.exporters.anki.globals import ANKICONNECT_URL
from ...data_access.exporters.anki.sync.gateway_utils import (
    anki_connect_is_live,
)
from .ankiconnect_gateway import (
    AnkiConnectGateway,
    AnkiField,
    NoteInfo,
)

ANKICONNECT_IS_RUNNING = anki_connect_is_live()


class MockNoteInfo(NoteInfo):
    noteId: int = 1
    tags: Sequence[str] = ["MockTag"]
    fields: Mapping[str, AnkiField] = {
        "Text": AnkiField(value="MockText", order=0)
    }
    modelName: str = "MockModel"
    cards: Sequence[int] = [1]


@pytest.mark.skipif(
    not ANKICONNECT_IS_RUNNING,
    reason="Tests require a running AnkiConnect server",
)
class TestAnkiConnectGateway:
    gateway = AnkiConnectGateway(
        ankiconnect_url=ANKICONNECT_URL,
        deck_name="0. Don't click me::1. Active::Personal Mnemonic Medium",
    )

    def test_import_package(self):
        output_path = Path("/output")

        # Delete all .apkg in the output directory
        for f in output_path.glob("*.apkg"):
            f.unlink()

        package = genanki.Package(
            deck_or_decks=genanki.Deck(deck_id=1, name="Test deck")
        )
        self.gateway.import_package(
            package=package,
            tmp_write_dir=Path("/output"),
            tmp_read_dir=Path("/Users/Leisure/ankidecks"),
        )
        assert len(list(Path("/output").glob("*.apkg"))) == 0

    def test_delete_notes(self):
        self.gateway.delete_notes(note_ids=[1, 2, 3])

    def test_get_note_infos(self):
        note_infos = self.gateway.get_all_note_infos()

        assert [
            isinstance(note_info, NoteInfo)
            for note_info in note_infos
        ]
