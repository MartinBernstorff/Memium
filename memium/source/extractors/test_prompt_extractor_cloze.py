from pathlib import Path

from ..document import Document
from .extractor_cloze import ClozePromptExtractor


def test_cloze_prompt_extractor(tmpdir: Path):
    doc = Document(
        content=r"""

What is the meaning of life? {42}


This is another block without any cloze prompts.

#anki/tag/test_tag

""",
        source_path=tmpdir / "test.md",
    )

    extractor = ClozePromptExtractor().extract_prompts(doc)

    assert len(extractor) == 1
    assert extractor[0].text == r"What is the meaning of life? {{c734::42}}"
    assert extractor[0].tags == ["anki/tag/test_tag"]
