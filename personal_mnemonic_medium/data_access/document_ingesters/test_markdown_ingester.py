import re
from pathlib import Path

from personal_mnemonic_medium.data_access.document_ingesters.markdown_ingester import (
    MarkdownIngester,
)


def test_markdown_ingester(tmpdir: Path):
    (tmpdir / "test.md").write_text(
        """# File title
Some content.
UUID: 123

# Delete after me
Test content
""",
        encoding="utf8",
    )

    # Test globbing through subdirs
    subdir = tmpdir / "subdir"
    Path(subdir).mkdir(exist_ok=True, parents=True)

    # Test UUID appending
    (subdir / "test2.md").write_text(
        """File contents""", encoding="utf8"
    )
    note_2_uuid = "UUID: 456"

    notes = MarkdownIngester(
        uuid_extractor=lambda x: re.findall(r"UUID: (\d+)", x)[0],
        cut_note_after="# Delete after me",
        uuid_generator=lambda: note_2_uuid,
    ).get_notes_from_dir(Path(tmpdir))

    # All notes were found
    assert len(notes) == 2

    # Basic ingesting
    test_note = notes[0]
    assert test_note.title == "test"
    assert "# File title" in test_note.content
    assert "Test content" not in test_note.content
    assert test_note.uuid == "123"

    # Test UUID appending
    assert notes[1].uuid == note_2_uuid
    assert note_2_uuid in notes[1].content
    assert note_2_uuid in (subdir / "test2.md").open("r").read()
