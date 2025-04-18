from collections.abc import Sequence
from dataclasses import dataclass

from inline_snapshot import snapshot

from memium.destination.ankiconnect.anki_formatter import AnkiQAFormatter
from memium.destination.ankiconnect.anki_model import AnkiQAModel


def fake_tag_factory() -> Sequence[str]:
    return ["FakeTag"]


import pytest


@dataclass(frozen=True)
class QAExample:
    card: AnkiQAModel
    expected_deck: str


@pytest.mark.parametrize(
    ("example"),
    [
        QAExample(AnkiQAModel.dummy(tags=["anki/deck/Subdeck"]), "FakeBaseDeck::Subdeck"),
        QAExample(
            AnkiQAModel.dummy(
                tags=["anki/deck/Subdeck"], question="What are _Wikilinks_ on _Wikipedia_?"
            ),
            "FakeBaseDeck::Subdeck::Wikilinks-Wikipedia",
        ),
        QAExample(
            AnkiQAModel.dummy(question="On _Wikipedia_, what are _Wikilinks_?"),
            "FakeBaseDeck::Wikilinks-Wikipedia",
        ),
        QAExample(AnkiQAModel.dummy(question="Without wikilinks?"), "FakeBaseDeck"),
    ],
    ids=lambda x: x.expected_deck,
)
def test_ankiqa_deck_inference(example: QAExample):
    assert example.card.deck == example.expected_deck


def test_model():
    card = AnkiQAModel.dummy(question="Q. This is a _question_?")
    model = AnkiQAFormatter("FakeCSS").format(card).model  # type: ignore
    assert model.model_id == snapshot(9079488902)  # type: ignore
    assert model.model_type == snapshot(0)  # type: ignore
    assert model.name == snapshot('Ankdown QA with raw text')  # type: ignore
    assert model.fields == snapshot(  # type: ignore
        [{"name": "Question"}, {"name": "Answer"}, {"name": "Extra"}, {'name':'raw_question'}, {'name':'raw_answer'}]
    )  # type: ignore
    assert model.css == snapshot('FakeCSS')  # type: ignore
    assert model.templates == snapshot(  # type: ignore
        [
            {
                "name": 'Ankdown QA with raw text',
                "qfmt": """\

<div class="front">{{ Extra }}
    {{ Question }}
</div>\
""",
                "afmt": """\

<div class="back">{{ Extra }}
    <div class="question">
        {{ Question }}
    </div>
    <div class="answer">
        {{ Answer }}
    </div>
</div>
            \
""",
            }
        ]
    )  # type: ignore


def test_formatting():
    card = AnkiQAModel.dummy(question="Q. This is a _question_?")
    note = AnkiQAFormatter("").format(card)
    assert note.fields == snapshot(  # type: ignore
        [
            "<p>Q. This is a <em>question</em>?</p>",
            '<p>A. DummyAnswer</p>',
            '', 'Q. This is a _question_?', 'A. DummyAnswer']
    )
