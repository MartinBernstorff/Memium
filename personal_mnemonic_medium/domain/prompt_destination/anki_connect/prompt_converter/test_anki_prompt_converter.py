import pytest

from ....prompts.base_prompt import BasePrompt
from ....prompts.cloze_prompt import ClozeWithoutDoc
from ....prompts.qa_prompt import QAWithoutDoc
from .anki_prompt_converter import AnkiPromptConverter
from .prompts.anki_cloze import AnkiCloze
from .prompts.anki_qa import AnkiQA
from .prompts.base_anki_prompt import AnkiCard

fake_anki_qa = AnkiQA(
    question="FakeQuestion",
    answer="FakeAnswer",
    base_deck="FakeDeck",
    tags=["FakeTag"],
    css="FakeCSS",
)

fake_anki_cloze = AnkiCloze(
    text="FakeText",
    base_deck="FakeDeck",
    tags=["FakeTag"],
    css="FakeCSS",
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
