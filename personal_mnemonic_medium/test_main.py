from pathlib import Path

from .main import main


def test_smoke_main(tmpdir: Path):
    apkg_output_filepath = Path(tmpdir) / "output_deck.apkg"

    main(
        apkg_output_filepath=apkg_output_filepath,
        input_dir=Path(__file__).parent / "tests",
        ankiconnect_sync_from_dir=apkg_output_filepath,
        watch=False,
        use_anki_connect=False,
    )

    assert apkg_output_filepath.exists()
