import pytest

from ...source.prompts.prompt import BasePrompt
from ...source.prompts.prompt_cloze import ClozeWithoutDoc
from ...source.prompts.prompt_qa import QAWithoutDoc
from .anki_converter import AnkiPromptConverter
from .anki_prompt import AnkiPrompt
from .test_anki_prompt_qa import FakeAnkiCloze, FakeAnkiQA


@pytest.mark.parametrize(
    ("input_prompt", "expected_card"),
    [
        (
            QAWithoutDoc(question="FakeQuestion", answer="FakeAnswer", add_tags=["FakeTag"]),
            FakeAnkiQA(
                uuid=4875918425
            ),  # Ensure that UUID generation remains stable to retain idempotency over time
        ),
        (
            ClozeWithoutDoc(text="FakeText", add_tags=["FakeTag"]),
            FakeAnkiCloze(
                uuid=1873301177
            ),  # Ensure that UUID generation remains stable to retain idempotency over time
        ),
    ],
)
def test_anki_prompt_converter(input_prompt: BasePrompt, expected_card: AnkiPrompt):
    """Tests the AnkiPromptConverter class"""
    generated_card = AnkiPromptConverter(
        base_deck="FakeBaseDeck", card_css="FakeCSS"
    ).prompt_to_card(input_prompt)

    assert generated_card.uuid == expected_card.uuid
