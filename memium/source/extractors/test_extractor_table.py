from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path

import pytest

from ..document import Document
from ..prompts.prompt_qa import QAPrompt
from .extractor_table import TableExtractor


@dataclass(frozen=True)
class TableExtractorExample:
    table_prompt: str  # What the example is testing
    expectation: Sequence[QAPrompt]  # Expected prompts


@pytest.mark.parametrize(
    ("example"),
    [
        TableExtractorExample(
            table_prompt="Descending // |Column one|? // |Column two|",
            expectation=[QAPrompt(question="11?", answer="22")],
        ),
        TableExtractorExample(
            table_prompt="Ascending // |Column one|? // |Column two|",
            expectation=[
                QAPrompt(question="21?", answer="12"),
                QAPrompt(question="31?", answer="22"),
            ],
        ),
        TableExtractorExample(
            table_prompt="Rowwise // |Column one|? // |Column two|",
            expectation=[
                QAPrompt(question="11?", answer="12"),
                QAPrompt(question="21?", answer="22"),
            ],
        ),
    ],
)
def test_table_extractor(example: TableExtractorExample):
    input_doc = Document(
        content=f"""
    Block one

| Column one | Column two |
| --- | --- |
| 11 | 12 |
| 21 | 22 |
| 31 |      |
{example.table_prompt}""",
        source_path=Path(__file__),
    )

    assert set(example.expectation) == set(TableExtractor().extract_prompts(input_doc))
