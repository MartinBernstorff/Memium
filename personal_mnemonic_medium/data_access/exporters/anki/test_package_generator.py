from pathlib import Path

from personal_mnemonic_medium.data_access.document_ingesters.document import (
    Document,
)
from personal_mnemonic_medium.data_access.exporters.anki.anki_exporter import (
    AnkiExporter,
)
from personal_mnemonic_medium.data_access.exporters.anki.card_types.qa import (
    AnkiQA,
)
from personal_mnemonic_medium.domain.prompt_extractors.qa_extractor import (
    QAPrompt,
)


def test_cards_to_decks():
    source_note = Document(
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
                source_note=source_note,
            ),
        )
        for _ in range(4)
    ]

    AnkiExporter().cards_to_deck(cards=genanki_notes)


def test_package_generators():
    source_note = Document(
        content="Q. What is the capital of France?\nA. Paris",
        uuid="1234",
        source_path=Path(__file__),
    )

    genanki_notes: list[AnkiQA] = [
        AnkiQA(
            fields=["Q. What is the capital of France?", "A. Paris"],
            source_prompt=QAPrompt(
                question="What is the capital of France?",
                answer="Paris",
                source_note=source_note,
            ),
        )
        for _ in range(4)
    ]

    AnkiExporter().cards_to_deck_bundle(cards=genanki_notes)
