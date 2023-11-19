from pathlib import Path

from personal_mnemonic_medium.data_access.document_ingesters.markdown_ingester import (
    is_markdown_file,
)


def test_is_markdown():
    assert is_markdown_file(Path("test.md"))
    assert is_markdown_file(Path("test.markdown"))
