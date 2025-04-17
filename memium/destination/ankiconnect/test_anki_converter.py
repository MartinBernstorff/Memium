from ...source.prompts.prompt_qa import QAPromptImpl, QAWithoutDoc
from .anki_converter import AnkiPromptConverter


def test_anki_prompt_converter():
    """Tests the AnkiPromptConverter class"""
    input_prompt = QAWithoutDoc(
        prompt=QAPromptImpl.dummy(question="FakeQuestion", answer="FakeAnswer"),
        add_tags=["FakeTag"],
    )
    generated_card = AnkiPromptConverter(
        base_deck="FakeBaseDeck", card_css="FakeCSS"
    ).prompt_to_card(input_prompt)

    # Ensure the generated uuid remains stable over time
    assert generated_card.uuid == 4875918425
