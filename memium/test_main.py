import logging
from pathlib import Path

import pytest

from memium.main import main

from .data_access.ankiconnect_gateway import anki_connect_is_live


@pytest.mark.skipif(
    not anki_connect_is_live(),
    reason="Tests require a running AnkiConnect server",
)
def test_main(
    tmp_path: Path,
    caplog: pytest.LogCaptureFixture,
    base_deck: str = "Tests::Integration Test deck",
):
    caplog.set_level(logging.INFO)
    output_path = tmp_path / "test.md"
    with output_path.open("w") as f:
        f.write(
            """# Test note
Q. Test question?
A. Test answer!
"""
        )

    main(
        base_deck=base_deck,
        input_dir=tmp_path,
        max_deletions_per_run=1,
        dry_run=True,
    )
    assert "Pushing prompt" in caplog.text
    assert "Test question?" in caplog.text
