from collections.abc import Sequence
from dataclasses import dataclass, field

from .anki_prompt_qa import AnkiQA


def fake_tag_factory() -> Sequence[str]:
    return ["FakeTag"]


@dataclass(frozen=True)
class FakeAnkiQA(AnkiQA):
    base_deck: str = "FakeBaseDeck"
    tags: Sequence[str] = field(default_factory=fake_tag_factory)
    question: str = "FakeQuestion"
    answer: str = "FakeAnswer"
    css: str = "FakeCSS"


def test_ankiqa_deck_inference():
    card = FakeAnkiQA(tags=["anki/deck/Subdeck"])
    assert card.deck == "FakeBaseDeck::Subdeck"
