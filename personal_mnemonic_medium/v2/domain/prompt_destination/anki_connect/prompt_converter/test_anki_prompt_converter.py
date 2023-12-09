import pytest

from ....prompts.base_prompt import BasePrompt
from ....prompts.cloze_prompt import ClozePromptWithoutDoc
from ....prompts.qa_prompt import QAPrompt
from .anki_prompt_converter import AnkiPromptConverter
from .prompts.anki_cloze import AnkiCloze
from .prompts.anki_qa import AnkiQA
from .prompts.base_anki_prompt import AnkiPrompt


@pytest.mark.parametrize(
    ("input_prompt", "expected_card"),
    [
        (
            QAPrompt(question="FakeQuestion", answer="FakeAnswer"),
            AnkiQA(question="FakeQuestion", answer="FakeAnswer"),
        ),
        (
            ClozePromptWithoutDoc(text="FakeText"),
            AnkiCloze(text="FakeText"),
        ),
    ],
)
def test_anki_prompt_converter(
    input_prompt: BasePrompt, expected_card: AnkiPrompt
):
    """Tests the AnkiPromptConverter class"""
    card = AnkiPromptConverter.prompts_to_cards([input_prompt])[0]

    assert card.uuid == expected_card.uuid
    for attr in expected_card.__dict__:
        assert getattr(card, attr) == getattr(expected_card, attr)
