from pathlib import Path

from .markdown_document_ingester import MarkdownDocumentIngester


def test_markdown_document_ingester(tmpdir: Path):
    ingester = MarkdownDocumentIngester(directory=Path(tmpdir))

    with (Path(tmpdir) / "test.md").open("w") as f:
        f.write("# Hello World")

    documents = ingester.get_documents()
    assert len(documents) == 1
