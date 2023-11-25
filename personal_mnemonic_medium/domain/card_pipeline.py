from collections.abc import Sequence
from pathlib import Path
from typing import Protocol

from personal_mnemonic_medium.data_access.document_ingesters.base import (
    DocumentIngester,
)
from personal_mnemonic_medium.data_access.exporters.anki.card_types.base import (
    AnkiCard,
)
from personal_mnemonic_medium.domain.prompt_extractors.base import (
    PromptExtractor,
)
from personal_mnemonic_medium.domain.prompt_extractors.prompt import (
    Prompt,
)


class CardExporter(Protocol):
    def prompts_to_cards(
        self, prompts: Sequence[Prompt]
    ) -> Sequence[AnkiCard]:
        ...


def extract_prompts(
    input_dir: Path,
    document_ingester: DocumentIngester,
    prompt_extractors: Sequence[PromptExtractor],
) -> Sequence[Prompt]:
    notes = document_ingester.get_notes_from_dir(dir_path=input_dir)

    collected_prompts: list[Prompt] = []
    for extractor in prompt_extractors:
        for note in notes:
            collected_prompts += extractor.extract_prompts(note)

    return collected_prompts
