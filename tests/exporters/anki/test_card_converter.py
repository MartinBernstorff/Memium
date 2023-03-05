import genanki

from personal_mnemonic_medium.exporters.anki.anki_card import AnkiCard
from personal_mnemonic_medium.note_factories.markdown import MarkdownNoteFactory
from tests.note_factories.test_markdown_extractor import PROJECT_ROOT


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
    cards = AnkiCard(fields=[""], sou)

    assert len([note for note in notes if "Medicine" in note.subdeck]) == 1
    assert len([note for note in notes if "med/Endocrinology" in note.tags]) == 1