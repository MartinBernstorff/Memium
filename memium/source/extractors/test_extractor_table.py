from collections.abc import Sequence
from dataclasses import dataclass

import pytest

from memium.source.prompt import QAWithDoc

from ..document import Document
from .extractor_table import TableExtractor
from .to_line_blocks import LineBlock, to_line_blocks


@dataclass(frozen=True)
class TableExtractorExample:
    table_prompt: str  # What the example is testing
    expectation: Sequence[QAWithDoc]  # Expected prompts


# p3: if the row contains a wikilink with a pipe, it will be split into two cells
# e.g. [[Name|Alias]] will be parsed incorrectly.


@pytest.mark.parametrize(
    ("example"),
    [
        TableExtractorExample(
            table_prompt="Descending // |Column one|? // |Column two|.",
            expectation=[QAWithDoc.dummy(question="11?", answer="22.", line_nr=8)],
        ),
        TableExtractorExample(
            table_prompt="Ascending // |Column one|? // |Column two|.",
            expectation=[
                QAWithDoc.dummy(question="31?", answer="22.", line_nr=8),
                QAWithDoc.dummy(question="21?", answer="12.", line_nr=8),
            ],
        ),
        TableExtractorExample(
            table_prompt="Rowwise // |Column one|? // |Column two|.",
            expectation=[
                QAWithDoc.dummy(question="21?", answer="22.", line_nr=8),
                QAWithDoc.dummy(question="11?", answer="12.", line_nr=8),
            ],
        ),
    ],
    ids=lambda x: x.table_prompt,
)
def test_table_extractor(example: TableExtractorExample):
    input_doc = Document.dummy(
        content=f"""
    Block one

| Column one | Column two |
| --- | --- |
| 11 | 12 |
| 21 | 22 |
| 31 |      |
{example.table_prompt}"""
    )

    result = TableExtractor().extract_prompts(input_doc)

    assert _scheduling_strs(result) == _scheduling_strs(example.expectation)


def _scheduling_strs(prompts: Sequence[QAWithDoc]) -> set[str]:
    return {p.scheduling_str for p in prompts}


def test_line_block_extractor():
    document = """Block 1

Block 2
With multiline"""
    assert to_line_blocks(document) == [
        LineBlock(starting_line=0, lines=["Block 1"]),
        LineBlock(starting_line=2, lines=["Block 2", "With multiline"]),
    ]
