from pathlib import Path
from typing import Any, Callable, List, Optional, Sequence

from personal_mnemonic_medium.exporters.anki.anki_card import AnkiCard
from personal_mnemonic_medium.exporters.anki.package_generator import PackageGenerator
from personal_mnemonic_medium.note_factories.markdown import MarkdownNoteFactory
from personal_mnemonic_medium.prompt_extractors.cloze_extractor import (
    ClozePromptExtractor,
)
from personal_mnemonic_medium.prompt_extractors.qa_extractor import QAPromptExtractor


def markdown_to_ankicard(
    dir_path: Optional[Path] = None,
    file_path: Optional[Path] = None,
    extractors: Sequence[Any] = (
        QAPromptExtractor(),
        ClozePromptExtractor(),
    ),
) -> List[AnkiCard]:
    notes = []

    if dir_path is not None:
        notes += MarkdownNoteFactory().get_notes_from_dir(dir_path=dir_path)

    if file_path is not None:
        note_from_file = MarkdownNoteFactory().get_note_from_file(file_path=file_path)
        if note_from_file is not None:
            notes += [note_from_file]

    collected_prompts = []

    for extractor in extractors:
        for note in notes:
            collected_prompts += extractor.extract_prompts(note)  # type: ignore

    cards = PackageGenerator().prompts_to_cards(prompts=collected_prompts)
    return cards
