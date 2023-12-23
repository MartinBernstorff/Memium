import pytest

from ...source.prompts.prompt import BasePrompt
from ...source.prompts.prompt_cloze import ClozeWithoutDoc
from ...source.prompts.prompt_qa import QAWithoutDoc
from .anki_card import AnkiCard
from .anki_converter import AnkiPromptConverter
from .anki_prompt_cloze import AnkiCloze
from .anki_prompt_qa import AnkiQA

fake_anki_qa = AnkiQA(
    question="FakeQuestion",
    answer="FakeAnswer",
    base_deck="FakeDeck",
    tags=["FakeTag"],
    css="FakeCSS",
)

fake_anki_cloze = AnkiCloze(
    text="FakeText", base_deck="FakeDeck", tags=["FakeTag"], css="FakeCSS"
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
    input_prompt: BasePrompt, expected_card: AnkiCard
):
    """Tests the AnkiPromptConverter class"""
    card = AnkiPromptConverter(
        base_deck="FakeDeck", card_css="FakeCSS"
    ).prompts_to_cards([input_prompt])[0]

    assert card.uuid == expected_card.uuid
    for attr in expected_card.__dict__:
        assert getattr(card, attr) == getattr(expected_card, attr)
