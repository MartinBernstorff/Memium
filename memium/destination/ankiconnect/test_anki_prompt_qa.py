from collections.abc import Sequence
from dataclasses import dataclass, field

from .anki_prompt_cloze import AnkiCloze
from .anki_prompt_qa import AnkiQA


def fake_tag_factory() -> Sequence[str]:
    return ["FakeTag"]


@dataclass(frozen=True)
class FakeAnkiCloze(AnkiCloze):
    text: str = "FakeText"
    base_deck: str = "FakeBaseDeck"
    tags: Sequence[str] = field(default_factory=fake_tag_factory)
    css: str = "FakeCSS"
    uuid: int = 0


@dataclass(frozen=True)
class FakeAnkiQA(AnkiQA):
    base_deck: str = "FakeBaseDeck"
    tags: Sequence[str] = field(default_factory=fake_tag_factory)
    question: str = "FakeQuestion"
    answer: str = "FakeAnswer"
    css: str = "FakeCSS"
    uuid: int = 0


def test_ankiqa_deck_inference():
    card = FakeAnkiQA(tags=["anki/deck/Subdeck"])
    assert card.deck == "FakeBaseDeck::Subdeck"


def test_formatting():
    card = FakeAnkiQA(question="Q. This is a _question_?")
    note = card.to_genanki_note()
    assert note.fields[0] == "<p>Q. This is a <em>question</em>?</p>"  # type: ignore
