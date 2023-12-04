from pathlib import Path

import genanki
import pytest

from ...data_access.exporters.anki.globals import ANKICONNECT_URL
from ...data_access.exporters.anki.sync.gateway_utils import (
    anki_connect_is_live,
)
from .ankiconnect import AnkiConnectGateway, NoteInfo

ANKICONNECT_IS_RUNNING = anki_connect_is_live()


@pytest.mark.skipif(
    not ANKICONNECT_IS_RUNNING,
    reason="Tests require a running AnkiConnect server",
)
class TestAnkiConnect:
    gateway = AnkiConnectGateway(ankiconnect_url=ANKICONNECT_URL)

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
        note_infos = self.gateway.get_note_infos(deck_name="Default")

        assert [
            isinstance(note_info, NoteInfo)
            for note_info in note_infos
        ]
