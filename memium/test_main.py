import logging
from pathlib import Path

import pytest

from memium.__main__ import main

from .destination.ankiconnect.ankiconnect_gateway import anki_connect_is_live


@pytest.mark.skipif(
    not anki_connect_is_live(),
    reason="Tests require a running AnkiConnect server",
)
def test_main(
    caplog: pytest.LogCaptureFixture, base_deck: str = "Main Integration Test"
):
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
            """QA. Du skal modtage en forbrændt patient. Efter ABCDE- og traumevurdering, hvad vil du da gøre?
A. 1) Skyld med vand i mindst 30 minutter (gerne 3-4 timer, hvis hypotermi kan undgås), 2) Anlæg 2 PVK'er i ikke-forbrændte områder, 3) Estimér forbrændt område i % (kun 2. og 3. gradsforbrændinger) + Opstart væskebeh. hvis forbrænding > 20% voksne, 10% børn
"""
        )

    main(
        base_deck=base_deck,
        input_dir=test_input_path,
        max_deletions_per_run=2,
        dry_run=False,
    )
    assert "Pushing 1 cards to Anki" in caplog.text

    # Test idempotency
    main(
        base_deck=base_deck,
        input_dir=test_input_path,
        max_deletions_per_run=0,  # 0 deletions allowed to test idempotency
        dry_run=False,
    )

    pass
