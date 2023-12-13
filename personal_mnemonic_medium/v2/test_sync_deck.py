from pathlib import Path

import pytest

from personal_mnemonic_medium.v2.sync_deck import sync_deck

from ..data_access.exporters.anki.sync.gateway_utils import (
    anki_connect_is_live,
)


@pytest.mark.skipif(
    not anki_connect_is_live(),
    reason="Tests require a running AnkiConnect server",
)
def test_sync_deck(tmp_path: Path):
    with (tmp_path / "test.md").open("w") as f:
        f.write(
            """# Test note
Q. Test question?
A. Test answer!
"""
        )

    sync_deck(
        base_deck="Tests::Integration Test deck",
        input_dir=tmp_path,
        apkg_output_dir=Path("/output"),
        ankiconnect_read_apkg_from_dir=Path(
            "/Users/Leisure/ankidecks"
        ),
        max_deletions_per_run=1,
    )
