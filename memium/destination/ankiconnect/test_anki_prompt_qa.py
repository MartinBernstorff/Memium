from collections.abc import Sequence
from dataclasses import dataclass, field

from inline_snapshot import snapshot

from memium.source.prompts.prompt_qa import QAPromptImpl

from .anki_prompt_qa import AnkiQA


def fake_tag_factory() -> Sequence[str]:
    return ["FakeTag"]


@dataclass(frozen=True)
class FakeAnkiQA(AnkiQA):
    base_deck: str = "FakeBaseDeck"
    tags: Sequence[str] = field(default_factory=fake_tag_factory)
    prompt: QAPromptImpl = field(default_factory=QAPromptImpl.dummy)
    css: str = "FakeCSS"
    uuid: int = 0
    edit_url: str = "FakeEditURL"
    source_title: str | None = None
    render_parent_doc: bool = False


from dataclasses import dataclass

import pytest


@dataclass(frozen=True)
class QAExample:
    card: AnkiQA
    deck: str


@pytest.mark.parametrize(
    ("example"),
    [
        QAExample(FakeAnkiQA(tags=["anki/deck/Subdeck"]), "FakeBaseDeck::Subdeck"),
        QAExample(
            FakeAnkiQA(
                tags=["anki/deck/Subdeck"],
                prompt=QAPromptImpl.dummy(question="What are _Wikilinks_ on _Wikipedia_?"),
            ),
            "FakeBaseDeck::Subdeck::Wikilinks-Wikipedia",
        ),
        QAExample(
            FakeAnkiQA(prompt=QAPromptImpl.dummy(question="On _Wikipedia_, what are _Wikilinks_?")),
            "FakeBaseDeck::Wikilinks-Wikipedia",
        ),
        QAExample(
            FakeAnkiQA(prompt=QAPromptImpl.dummy(question="Without wikilinks?")), "FakeBaseDeck"
        ),
    ],
)
def test_ankiqa_deck_inference(example: QAExample):
    assert example.card.deck == example.deck


def test_formatting():
    card = FakeAnkiQA(prompt=QAPromptImpl.dummy(question="Q. This is a _question_?"))
    note = card.to_genanki_note()
    assert note.fields == snapshot(  # type: ignore
        [
            "<p>Q. This is a <em>question</em>?</p>",
            "<p>DummyAnswer</p>",
            """\
<div class='edit_button' style='text-align: center;'><a href="FakeEditURL" style="background-color: #5f0069;
        border: none;
        color: white;
        padding: 0.8em;
        text-align: center;
        text-decoration: none;
        font-size: 0.8em;
        font-family: 'Inter', sans-serif;
        border-radius: 8px;
        opacity: 0.8;
">Obsidian</a></div>\
""",
            "0",
        ]
    )
