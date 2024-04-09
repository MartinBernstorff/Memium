from collections.abc import Sequence
from dataclasses import dataclass

import pytest

from memium.utils.get_wikilinks_from_string import get_wikilinks_from_string


@dataclass(frozen=True)
class TestExample:
    input_string: str
    wikilinks: Sequence[str]


@pytest.mark.parametrize(
    ("example"),
    [
        TestExample("[[Test|Test2]]", ["Test"]),
        TestExample("[[Test (testing)]]", ["Test (testing)"]),
        TestExample("[[Test]]", ["Test"]),
        TestExample("[[Test]], [[Test2]]", ["Test", "Test2"]),
        TestExample("[[ Some things, are just not [[Wikilinks]] ]]", ["Wikilinks"]),
    ],
    ids=lambda x: x.input_string,
)
def test_get_wikilinks_from_string(example: TestExample):
    assert get_wikilinks_from_string(example.input_string) == example.wikilinks
