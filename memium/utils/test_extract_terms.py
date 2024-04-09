from collections.abc import Sequence
from dataclasses import dataclass

import pytest

from memium.utils.extract_terms import get_terms_surrounded_by_underscores


@dataclass(frozen=True)
class TestExample:
    input_string: str
    wikilinks: Sequence[str]


@pytest.mark.parametrize(
    ("example"),
    [
        TestExample("_Test_", ["Test"]),
        TestExample("_Test (testing)_", ["Test (testing)"]),
        TestExample("_Test_, _Test2_", ["Test", "Test2"]),
        TestExample("_ Some things, are just not _Wikilinks_ _", ["Wikilinks"]),
    ],
    ids=lambda x: x.input_string,
)
def test_get_wikilinks_from_string(example: TestExample):
    assert get_terms_surrounded_by_underscores(example.input_string) == example.wikilinks
