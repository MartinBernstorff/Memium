import logging
from pathlib import Path

import pytest

from personal_mnemonic_medium.sync_deck import sync_deck

from .data_access.ankiconnect_gateway import anki_connect_is_live


@pytest.mark.skipif(
    not anki_connect_is_live(),
    reason="Tests require a running AnkiConnect server",
)
def test_sync_deck(tmp_path: Path, caplog: pytest.LogCaptureFixture):
    caplog.set_level(logging.INFO)
    output_path = tmp_path / "test.md"
    with output_path.open("w") as f:
        f.write(
            """# Test note
Q. Test question?
A. Test answer!
"""
        )

    base_deck = "Tests::Integration Test deck"
    apkg_output_dir = Path("/output")
    read_dir = Path("/Users/Leisure/ankidecks")

    sync_deck(
        base_deck=base_deck,
        input_dir=tmp_path,
        apkg_output_dir=apkg_output_dir,
        ankiconnect_read_apkg_from_dir=read_dir,
        max_deletions_per_run=1,
        dry_run=True,
    )
    assert "Pushing prompt" in caplog.text
    assert "Test question?" in caplog.text
