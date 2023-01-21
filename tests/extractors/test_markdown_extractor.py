from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent

from personal_mnemonic_medium.extractors.markdown import MarkdownToNotes


def test_get_notes_from_dir():
    notes = MarkdownToNotes().get_notes_from_dir(
        PROJECT_ROOT / "tests" / "test_md_files"
    )

    assert len(notes) == 4
    assert len([note for note in notes if "test_card_guid" == note.title]) == 1
    assert len([note for note in notes if "7696CDCD" in note.content]) == 1
    assert len([note for note in notes if "7696CDCD" in note.uuid]) == 1
    assert len([note for note in notes if "Medicine" in note.subdeck]) == 1
    assert len([note for note in notes if "med/Endocrinology" in note.tags]) == 1
