import pathlib
from collections.abc import Sequence
from dataclasses import dataclass

import pytest
from inline_snapshot import snapshot

from memium.utils.markdown import get_terms_surrounded_by_underscores

from .markdown import md_to_html


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
    assert md_to_html(example.given) == f"<p>{example.then}</p>"


def test_code_block_parsing(tmp_path: pathlib.Path):
    contents = pathlib.Path(__file__).parent / "code_block.md"
    parsed = md_to_html(contents.read_text())
    path = tmp_path / "test.htm"
    path.write_text(parsed)
    assert parsed == snapshot("""\
<pre><code class="language-python">def myfunc():
    return res
</code></pre>\
""")


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
