from pathlib import Path

from personal_mnemonic_medium.exporters.anki.card_types.base import (
    AnkiCard,
)
from personal_mnemonic_medium.exporters.anki.card_types.qa import (
    AnkiQA,
)
from personal_mnemonic_medium.exporters.anki.package_generator import (
    AnkiPackageGenerator,
)
from personal_mnemonic_medium.note_factories.note import Document
from personal_mnemonic_medium.prompt_extractors.qa_extractor import (
    QAPrompt,
)


def test_cards_to_decks():
    source_note = Document(
        title="Test",
        content="Q. What is the capital of France?\nA. Paris",
        uuid="1234",
        source_path=Path(__file__),
    )

    genanki_notes = [
        AnkiQA(
            fields=["Q. What is the capital of France?", "A. Paris"],
            source_prompt=QAPrompt(
                question="What is the capital of France?",
                answer="Paris",
                note_uuid="1234",
                source_note=source_note,
            ),
        )
        for _ in range(4)
    ]

    AnkiPackageGenerator().cards_to_deck(cards=genanki_notes)


def test_package_generators():
    source_note = Document(
        title="Test",
        content="Q. What is the capital of France?\nA. Paris",
        uuid="1234",
        source_path=Path(__file__),
    )

    genanki_notes: list[AnkiCard] = [
        AnkiQA(
            fields=["Q. What is the capital of France?", "A. Paris"],
            source_prompt=QAPrompt(
                question="What is the capital of France?",
                answer="Paris",
                note_uuid="1234",
                source_note=source_note,
            ),
        )
        for _ in range(4)
    ]

    AnkiPackageGenerator().cards_to_deck_bundle(cards=genanki_notes)
