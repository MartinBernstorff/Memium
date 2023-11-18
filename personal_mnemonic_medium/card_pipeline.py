from collections.abc import Sequence
from pathlib import Path

from personal_mnemonic_medium.exporters.anki.card_types.base import (
    AnkiCard,
)
from personal_mnemonic_medium.exporters.base import CardExporter
from personal_mnemonic_medium.note_factories.base import (
    DocumentFactory,
)
from personal_mnemonic_medium.note_factories.note import Document
from personal_mnemonic_medium.prompt_extractors.base import (
    PromptExtractor,
)
from personal_mnemonic_medium.prompt_extractors.prompt import Prompt


class CardPipeline:
    def __init__(
        self,
        document_factory: DocumentFactory,
        prompt_extractors: Sequence[PromptExtractor],
        card_exporter: CardExporter,
    ) -> None:
        self.document_factory = document_factory
        self.prompt_extractors = prompt_extractors
        self.card_exporter = card_exporter

    def run(self, input_path: Path) -> list[AnkiCard]:
        notes: list[Document] = []
        if input_path.is_dir():
            notes += list(
                self.document_factory.get_notes_from_dir(
                    dir_path=input_path
                )
            )

        if not input_path.is_dir():
            note_from_file = self.document_factory.get_note_from_file(
                file_path=input_path
            )
            notes.append(note_from_file)

        collected_prompts: list[Prompt] = []

        for extractor in self.prompt_extractors:
            for note in notes:
                collected_prompts += extractor.extract_prompts(note)

        cards: list[AnkiCard] = self.card_exporter.prompts_to_cards(
            prompts=collected_prompts
        )
        return cards
