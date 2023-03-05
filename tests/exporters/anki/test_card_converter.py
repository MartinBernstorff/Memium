import genanki

from personal_mnemonic_medium.exporters.anki.anki_card import AnkiCard


def test_custom_card_to_genanki_card():
    genanki_note = AnkiCard(
        fields=["Q. What is the capital of France?", "A. Paris"],
        source_markdown="Q. What is the capital of France?\nA. Paris",
        filepath="tests/fixtures/anki_cards/anki_card.md",
        tags=["test"],
        model_type="QA",
    ).to_genanki_note()

    assert isinstance(genanki_note, genanki.Note)
