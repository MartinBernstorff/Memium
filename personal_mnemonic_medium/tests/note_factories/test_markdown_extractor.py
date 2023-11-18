from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent

from personal_mnemonic_medium.note_factories.markdown import (
    MarkdownNoteFactory,
)


def test_get_notes_from_dir():
    notes = MarkdownNoteFactory().get_notes_from_dir(
        PROJECT_ROOT / "tests" / "test_md_files"
    )

    assert len(notes) == 4
    assert (
        len(
            [note for note in notes if note.title == "test_card_guid"]
        )
        == 1
    )
    assert (
        len([note for note in notes if "7696CDCD" in note.content])
        == 1
    )
    assert (
        len([note for note in notes if "7696CDCD" in note.uuid]) == 1
    )
