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

    value = MarkdownIngester(
        uuid_extractor=lambda x: re.findall(r"UUID: (\d+)", x)[0],
        cut_note_after="# Delete after me",
        uuid_generator=None,
    ).get_note_from_file(Path(tmpdir) / "test.md")

    content = value.content
    assert "Test content" not in content
    assert value.uuid == "123"
