from inline_snapshot import snapshot

from ...source.prompt import QAWithDoc
from .anki_converter import AnkiPromptConverter


def test_anki_prompt_converter():
    """Tests the AnkiPromptConverter class"""
    input_prompt = QAWithDoc.dummy()
    generated_card = AnkiPromptConverter.dummy().to_destination(input_prompt)

    # Ensure the generated uuid remains stable over time
    assert generated_card.raw_prompt.question == snapshot("FakeQuestion")
    assert generated_card.raw_prompt.answer == snapshot("FakeAnswer")
    assert generated_card.raw_prompt.scheduling_uid == 4875918425
