from pathlib import Path

from ..document import Document
from ..prompts.prompt_qa import QAPrompt
from .extractor_table import TableExtractor


def test_table_extractor():
    input_doc = Document(
        content="""
    Block one

| Column one | Column two |
| --- | --- |
| R1C1 | R1C2 |
| R2C1 | R2C2 |
Descending // |Column one| is real? // |Column two|
Ascending // |Column two|? // |Column one|
Rowwise // |Column one|? // |Column two|""",
        source_path=Path(__file__),
    )

    prompts = TableExtractor().extract_prompts(input_doc)
    assert prompts == [
        QAPrompt(question="R1C1 is real?", answer="R2C2"),  # Descending
        QAPrompt(question="R2C2?", answer="R1C1"),  # Ascending
        QAPrompt(question="R1C1?", answer="R1C2"),  # Rowwise
        QAPrompt(question="R2C1?", answer="R2C2"),  # Rowwise
    ]
