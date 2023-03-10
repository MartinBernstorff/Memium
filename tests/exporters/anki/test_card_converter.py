from pathlib import Path

import genanki
from personal_mnemonic_medium.exporters.anki.anki_card import AnkiCard
from personal_mnemonic_medium.exporters.anki.package_generator import PackageGenerator
from personal_mnemonic_medium.note_factories.markdown import MarkdownNoteFactory
from personal_mnemonic_medium.prompt_extractors.qa_extractor import QAPromptExtractor


def test_custom_card_to_genanki_card():
    genanki_note = AnkiCard(
        fields=["Q. What is the capital of France?", "A. Paris"],
        source_markdown="Q. What is the capital of France?\nA. Paris",
        tags=["test"],
        model_type="QA",
        note_uuid="1234",
    ).to_genanki_note()

    assert isinstance(genanki_note, genanki.Note)


def test_get_subtags():
    card = AnkiCard(
        fields=[""],
        source_markdown="Testing subdeck extraction, #anki/deck/Medicine, #anki/tag/med/Endocrinology",
        tags=["test"],
        model_type="QA",
        note_uuid="1234",
    )

    assert "Medicine" in card.subdeck


def test_card_uuid_generation():
    file_path = (
        Path(__file__).parent.parent.parent / "test_md_files" / "test_card_guid.md"
    )
    note = MarkdownNoteFactory().get_note_from_file(file_path=file_path)
    qa_extractor = QAPromptExtractor(question_prefix="Q.", answer_prefix="A.")
    qa_prompts = qa_extractor.extract_prompts(note)

    cards = PackageGenerator().prompts_to_cards(prompts=qa_prompts)

    reference_guids = {9315717920, 3912828915, 6300568814}
    generated_guids = {card.uuid for card in cards}

    assert reference_guids == generated_guids

    cloze_guids = {3001245253, 952903559}
