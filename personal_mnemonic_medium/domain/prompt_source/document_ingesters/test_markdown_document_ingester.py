from pathlib import Path

from .markdown_document_ingester import MarkdownDocumentIngester


def test_markdown_document_ingester(tmpdir: Path):
    ingester = MarkdownDocumentIngester(directory=Path(tmpdir))

    with (Path(tmpdir) / "test.md").open("w") as f:
        f.write(
            """# Hello World\n
#anki/tag/test_tag #anki/tag/test_tag2 <!-- #comment_tag -->
"""
        )

    documents = ingester.get_documents()
    assert len(documents) == 1
    document = documents[0]
    assert document.title == "test"
    assert document.tags == [
        "#anki/tag/test_tag",
        "#anki/tag/test_tag2",
        "#comment_tag",
    ]
