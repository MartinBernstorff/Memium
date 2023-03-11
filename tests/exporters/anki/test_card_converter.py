from pathlib import Path

import genanki
from personal_mnemonic_medium.exporters.anki.anki_card import AnkiCard
from personal_mnemonic_medium.markdown_to_ankicard import markdown_to_ankicard
from personal_mnemonic_medium.note_factories.markdown import MarkdownNoteFactory
from personal_mnemonic_medium.note_factories.note import Document
from personal_mnemonic_medium.prompt_extractors.cloze_extractor import (
    ClozePromptExtractor,
)
from personal_mnemonic_medium.prompt_extractors.qa_extractor import (
    QAPrompt,
    QAPromptExtractor,
)


def test_custom_card_to_genanki_card():
    source_note = Document(
        title="Test",
        content="Test",
        uuid="1234",
        source_path=Path(__file__),
    )
    genanki_note = AnkiCard(
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
    ).to_genanki_note()

    assert isinstance(genanki_note, genanki.Note)


def test_get_subtags():
    source_note = Document(
        title="Test",
        content="Test",
        uuid="1234",
        source_path=Path(__file__),
    )

    card = AnkiCard(
        fields=[""],
        source_markdown="Testing subdeck extraction, #anki/deck/Medicine, #anki/tag/med/Endocrinology",
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

    assert "Medicine" in card.subdeck


def test_qa_uuid_generation():
    file_path = (
        Path(__file__).parent.parent.parent / "test_md_files" / "test_card_guid.md"
    )
    cards = markdown_to_ankicard(file_path=file_path, extractors=[QAPromptExtractor()])

    reference_guids = {9315717920, 3912828915, 6300568814}
    generated_guids = {card.uuid for card in cards}
    assert reference_guids == generated_guids


def test_cloze_uuid_generation():
    file_path = (
        Path(__file__).parent.parent.parent / "test_md_files" / "test_card_guid.md"
    )
    cloze_cards = markdown_to_ankicard(
        file_path=file_path,
        extractors=[ClozePromptExtractor()],
    )

    cloze_generated_guids = {card.uuid for card in cloze_cards}
    cloze_reference_guids = {3001245253, 952903559}
    assert cloze_reference_guids == cloze_generated_guids


def test_get_bear_id():
    factory = MarkdownNoteFactory()
    note_str = r"Q. A card with a GUID.\nA. And here is its answer.\n\nQS. How about a card like this?\nA. Yes, an answer too.\n\nQ. How about multiline questions?\n* Like this\n* Or this?\nA. What is the hash?\n\nAnd some {cloze} deletions? For sure! Multipe {even}.\n\n<!-- {BearID:7696CDCD-803A-40BC-88D8-855DDBEC56CA-31546-000054DF17EAE2C1} -->"

    expected_id = (
        r"<!-- {BearID:7696CDCD-803A-40BC-88D8-855DDBEC56CA-31546-000054DF17EAE2C1} -->"
    )

    extracted_id = factory.get_bear_id(note_str)

    assert extracted_id == expected_id
