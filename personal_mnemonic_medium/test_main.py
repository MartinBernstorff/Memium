from pathlib import Path

from .main import main


def test_smoke_main(tmpdir: Path):
    apkg_output_filepath = (
        Path(tmpdir) / "subdir" / "output_deck.apkg"
    )

    main(
        input_dir=Path(__file__).parent / "tests",
        apkg_output_filepath=apkg_output_filepath,
        ankiconnect_sync_from_dir=apkg_output_filepath,
        watch=False,
        use_anki_connect=False,
    )

    assert apkg_output_filepath.exists()
