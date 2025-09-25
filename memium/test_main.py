import logging
from pathlib import Path

import pytest

from memium.__main__ import main

from .destination.ankiconnect.ankiconnect_requester import anki_connect_is_live

INTEGRATION_TEST_DECK = "Main Integration Test"


@pytest.mark.skipif(
    not anki_connect_is_live() or not Path("/output").exists(),
    reason="Tests require a running AnkiConnect server and an output directory. Use the Docker container to run the tests.",
)
def test_main(caplog: pytest.LogCaptureFixture, root_deck: str = INTEGRATION_TEST_DECK) -> None:  # noqa: PT028
    caplog.set_level(logging.INFO)

    # Clear and delete output path
    test_input_path = Path("/output")

    if test_input_path.exists():
        for entity in test_input_path.iterdir():
            if not entity.is_dir():
                entity.unlink()
    else:
        test_input_path.mkdir(parents=True)

    with (test_input_path / "test.md").open("w") as f:
        f.write(
            """Q. What are [[Trees]]?
A. å
"""
        )

    main(root_deck=root_deck, input_dir=test_input_path)
    assert "Pushing 1 cards to Anki" in caplog.text

    # Test idempotency
    main(root_deck=root_deck, input_dir=test_input_path)
