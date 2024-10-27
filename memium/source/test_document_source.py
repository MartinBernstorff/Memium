import logging
from dataclasses import dataclass
from pathlib import Path

import pytest

from .document_source import MarkdownDocumentSource


class TestMarkdownIngester:
    def test_happy_path(self, tmp_path: Path):
        with (tmp_path / "test.md").open("w") as f:
            f.write(
                """# Hello World\n
    #anki/tag/test_tag #anki/tag/test_tag2 <!-- #comment_tag -->
    """
            )

        documents = MarkdownDocumentSource(directory=tmp_path).get_documents()

        assert len(documents) == 1
        document = documents[0]
        assert document.title == "test"
        assert document.tags == ["anki/tag/test_tag", "anki/tag/test_tag2", "comment_tag"]

    def test_should_log_error_if_file_not_retrieved(
        self, tmp_path: Path, caplog: pytest.LogCaptureFixture
    ):
        caplog.set_level(logging.WARNING)

        (tmp_path / "succesful.md").write_text("""# I should succeed""")

        failed_path = tmp_path / "failed.md"
        failed_path.write_text("""# I should fail""")
        # Change permission to write only
        # Removing read and execute permissions for owner, group and others
        failed_path.chmod(0o200)

        MarkdownDocumentSource(directory=tmp_path)._get_document_from_file(  # type: ignore[PrivateMethodUsage]
            Path("I do not exist")
        )
        assert "I do not exist" in caplog.records[0].message

    def test_sanitize_to_valid_markdown(self):
        input_str = (
            """Linking to a valid [[Note|Note Alias]], and can handle [[Note2|Multiple Aliases]]"""
        )
        expected_output = """Linking to a valid _Note Alias_, and can handle _Multiple Aliases_"""
        assert (
            MarkdownDocumentSource(directory=Path())._sanitize_to_valid_markdown(  # type: ignore[PrivateMethodUsage]
                input_str
            )
            == expected_output
        )


@dataclass(frozen=True)
class Ex:
    given: str
    # Required setup

    then: str
    # What the expected result is


@pytest.mark.parametrize(
    ("example"),
    [
        Ex("[[N|Alias]]", "[[Alias]]"),  # Base
        Ex(" [[N|Alias]] ", " [[Alias]] "),  # Spaces
        Ex("[[N/N2|Alias]]", "[[Alias]]"),  # Nesting
        Ex("[[-|A]]", "[[A]]"),  # Dash
    ],
    ids=lambda x: x.given,
)
def test_replace_alias_wiki_links(example: Ex):
    given = MarkdownDocumentSource._replace_alias_wiki_links(example.given)  # type: ignore
    then = example.then
    assert given == then
