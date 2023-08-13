from pathlib import Path

import genanki
from personal_mnemonic_medium.exporters.anki.anki_card import AnkiCard
from personal_mnemonic_medium.exporters.anki.package_generator import (
    AnkiPackageGenerator,
)
from personal_mnemonic_medium.note_factories.note import Document
from personal_mnemonic_medium.prompt_extractors.qa_extractor import QAPrompt


def test_cards_to_decks():
    source_note = Document(
        title="Test",
        content="Q. What is the capital of France?\nA. Paris",
        uuid="1234",
        source_path=Path(__file__),
    )

    genanki_notes = [
        AnkiCard(
            fields=["Q. What is the capital of France?", "A. Paris"],
            model_type="QA",
            source_prompt=QAPrompt(
                question="What is the capital of France?",
                answer="Paris",
                note_uuid="1234",
                source_note=source_note,
            ),
        )
        for _ in range(4)
    ]

    deck, media = AnkiPackageGenerator().cards_to_deck(cards=genanki_notes)

    assert type(deck) == genanki.Deck
    assert type(media) == set


def test_package_generators():
    source_note = Document(
        title="Test",
        content="Q. What is the capital of France?\nA. Paris",
        uuid="1234",
        source_path=Path(__file__),
    )

    genanki_notes = [
        AnkiCard(
            fields=["Q. What is the capital of France?", "A. Paris"],
            model_type="QA",
            source_prompt=QAPrompt(
                question="What is the capital of France?",
                answer="Paris",
                note_uuid="1234",
                source_note=source_note,
            ),
        )
        for _ in range(4)
    ]

    AnkiPackageGenerator().cards_to_deck_bundle(
        cards=genanki_notes,
    )
