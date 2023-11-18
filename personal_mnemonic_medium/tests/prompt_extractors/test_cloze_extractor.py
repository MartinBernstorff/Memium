from pathlib import Path

from personal_mnemonic_medium.note_factories.note import Document
from personal_mnemonic_medium.prompt_extractors.cloze_extractor import (
    ClozePromptExtractor,
)


def test_cloze_with_hits():
    note_with_cloze = Document(
        title="Test note",
        content=r"""Test content.
{Cloze deletions} are part of the {game}. Right?
Even after newlines.

Even after new blocks. They should {all} be found.
        """,
        uuid="1234",
        source_path=Path(__file__),
    )

    prompts = ClozePromptExtractor().extract_prompts(note_with_cloze)

    assert len(prompts) == 3


def test_cloze_no_hits():
    note_without_cloze = Document(
        title="Test note",
        content=r"""Test content.""",
        uuid="1234",
        source_path=Path(__file__),
    )

    prompts = ClozePromptExtractor().extract_prompts(
        note_without_cloze
    )

    assert len(prompts) == 0
