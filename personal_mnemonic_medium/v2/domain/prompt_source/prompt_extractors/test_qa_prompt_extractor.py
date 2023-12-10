from pathlib import Path

from ..document_ingesters.document import Document
from .qa_prompt_extractor import QAPromptExtractor


def test_qa_prompt_extractor(tmpdir: Path):
    doc = Document(
        content="""

Q. What is the meaning of life?
A. 42

#anki/tag/test_tag

""",
        source_path=tmpdir / "test.md",
    )

    extractor = QAPromptExtractor(
        question_prefix="Q.", answer_prefix="A."
    ).extract_prompts(doc)

    assert len(extractor) == 1
    assert extractor[0].question == "What is the meaning of life?"
    assert extractor[0].answer == "42"
    assert extractor[0].tags == ["#anki/tag/test_tag"]
