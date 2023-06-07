from pathlib import Path

from personal_mnemonic_medium.exporters.anki.anki_card import AnkiCard
from personal_mnemonic_medium.exporters.anki.package_generator import (
    DeckCollection,
    PackageGenerator,
)
from personal_mnemonic_medium.note_factories.note import Document
from personal_mnemonic_medium.prompt_extractors.qa_extractor import QAPrompt


def test_cards_to_decks():
    source_note = Document(
        title="Test",
        content="Test",
        uuid="1234",
        source_path=Path(__file__),
    )

    genanki_notes = [
        AnkiCard(
            fields=["Q. What is the capital of France?", "A. Paris"],
            source_markdown="Q. What is the capital of France?\nA. Paris",
            tags=["test"],
            model_type="QA",
            source_prompt=QAPrompt(
                question="What is the capital of France?",
                answer="Paris",
                note_uuid="1234",
                source_note=source_note,
            ),
            source_note=source_note,
        )
        for _ in range(4)
    ]

    decks, media = PackageGenerator().cards_to_deck(cards=genanki_notes)

    assert type(decks) == DeckCollection
    assert type(media) == set


def test_package_generators():
    source_note = Document(
        title="Test",
        content="Test",
        uuid="1234",
        source_path=Path(__file__),
    )

    genanki_notes = [
        AnkiCard(
            fields=["Q. What is the capital of France?", "A. Paris"],
            source_markdown="Q. What is the capital of France?\nA. Paris",
            tags=["test"],
            model_type="QA",
            source_prompt=QAPrompt(
                question="What is the capital of France?",
                answer="Paris",
                note_uuid="1234",
                source_note=source_note,
            ),
            source_note=source_note,
        )
        for _ in range(4)
    ]

    PackageGenerator().cards_to_deck_bundle(
        cards=genanki_notes,
        output_path="test_package",
    )
