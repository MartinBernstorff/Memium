from collections.abc import Sequence
from dataclasses import dataclass

import pytest

from memium.utils.extract_terms import get_terms_surrounded_by_underscores


@dataclass(frozen=True)
class Example:
    input_string: str
    wikilinks: Sequence[str]


@pytest.mark.parametrize(
    ("example"),
    [
        Example("_Test_", ["Test"]),
        Example("_Test (testing)_", ["Test (testing)"]),
        Example("_Test_, _Test2_", ["Test", "Test2"]),
        Example("_ Some things, are just not _Wikilinks_ _", ["Wikilinks"]),
    ],
    ids=lambda x: x.input_string,
)
def test_get_wikilinks_from_string(example: Example):
    assert get_terms_surrounded_by_underscores(example.input_string) == example.wikilinks
