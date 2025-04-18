from ...source.prompts.prompt_qa import QAWithoutDoc
from .anki_converter import AnkiPromptConverter


def test_anki_prompt_converter():
    """Tests the AnkiPromptConverter class"""
    input_prompt = QAWithoutDoc.dummy()
    generated_card = AnkiPromptConverter.dummy().to_destination(input_prompt)

    # Ensure the generated uuid remains stable over time
    assert generated_card.uuid == "4875918425"
