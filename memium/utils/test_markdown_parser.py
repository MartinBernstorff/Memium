from dataclasses import dataclass

import pytest

from .markdown_parser import markdown_parser


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
    assert markdown_parser(example.given) == f"<p>{example.then}</p>"
