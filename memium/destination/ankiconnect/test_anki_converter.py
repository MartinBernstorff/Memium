import pytest

from ...source.prompts.prompt import BasePrompt
from ...source.prompts.prompt_cloze import ClozeWithoutDoc
from ...source.prompts.prompt_qa import QAWithoutDoc
from .anki_converter import AnkiPromptConverter
from .anki_prompt import AnkiPrompt
from .anki_prompt_cloze import AnkiCloze
from .test_anki_prompt_qa import FakeAnkiQA

fake_anki_qa = FakeAnkiQA()
fake_anki_cloze = AnkiCloze(
    text="FakeText",
    base_deck="FakeDeck",
    tags=["FakeTag"],
    css="FakeCSS",
    uuid=0,
)


@pytest.mark.parametrize(
    ("input_prompt", "expected_card"),
    [
        (
            QAWithoutDoc(
                question="FakeQuestion",
                answer="FakeAnswer",
                add_tags=["FakeTag"],
            ),
            fake_anki_qa,
        ),
        (
            ClozeWithoutDoc(text="FakeText", add_tags=["FakeTag"]),
            fake_anki_cloze,
        ),
    ],
)
def test_anki_prompt_converter(
    input_prompt: BasePrompt, expected_card: AnkiPrompt
):
    """Tests the AnkiPromptConverter class"""
    card = AnkiPromptConverter(
        base_deck="FakeDeck", card_css="FakeCSS"
    ).prompt_to_card(input_prompt)

    assert card.uuid == expected_card.uuid
    for attr in expected_card.__dict__:
        assert getattr(card, attr) == getattr(expected_card, attr)
