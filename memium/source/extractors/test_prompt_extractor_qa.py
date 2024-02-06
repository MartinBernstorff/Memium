from pathlib import Path

from ..document import Document
from .extractor_qa import QAPromptExtractor


def test_qa_prompt_extractor(tmpdir: Path):
    doc = Document(
        content="""

Q. What is the meaning of life?
A. 42

#anki/tag/test_tag

""",
        source_path=tmpdir / "test.md",
    )

    extractor = QAPromptExtractor(question_prefix="Q.", answer_prefix="A.").extract_prompts(doc)

    assert len(extractor) == 1
    prompt = extractor[0]
    assert prompt.question == "What is the meaning of life?"
    assert prompt.answer == "42"
    assert prompt.tags == ["anki/tag/test_tag"]
    assert prompt.scheduling_uid == 3643087944
