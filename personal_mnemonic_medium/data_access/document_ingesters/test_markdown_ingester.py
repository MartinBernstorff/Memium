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

    subdir = tmpdir / "subdir"
    Path(subdir).mkdir(exist_ok=True, parents=True)
    (subdir / "test2.md").write_text("""UUID: 123""", encoding="utf8")

    notes = MarkdownIngester(
        uuid_extractor=lambda x: re.findall(r"UUID: (\d+)", x)[0],
        cut_note_after="# Delete after me",
        uuid_generator=None,
    ).get_notes_from_dir(Path(tmpdir))

    assert len(notes) == 2
    test_note = notes[0]
    assert test_note.title == "test"
    assert "# File title" in test_note.content
    assert "Test content" not in test_note.content
    assert test_note.uuid == "123"
