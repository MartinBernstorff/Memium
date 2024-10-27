import pathlib
from dataclasses import dataclass

import pytest

from .markdown_parser import to_html


@dataclass(frozen=True)
class Ex:
    given: str
    # Required setup

    then: str
    # What the expected result is


@pytest.mark.parametrize(
    ("example"),
    [
        Ex("_Method_s", "<em>Method</em>s")  # Example one
    ],
)
def test_markdown_parser(example: Ex):
    assert to_html(example.given) == f"<p>{example.then}</p>"


def test_code_block_parsing(snapshot: str, tmp_path: pathlib.Path):
    contents = pathlib.Path(__file__).parent / "code_block.md"
    parsed = to_html(contents.read_text())
    path = tmp_path / "test.htm"
    path.write_text(parsed)
    assert parsed == snapshot
