from collections.abc import Sequence
from dataclasses import dataclass, field

import genanki

from memium.str_utils.term_extractor import get_terms_surrounded_by_underscores

from ...str_utils.hasher import hash_str_to_int
from .anki_cloze import AnkiCloze
from .anki_prompt import AnkiPrompt


def fake_tag_factory() -> Sequence[str]:
    return ["FakeTag"]


@dataclass(frozen=True)
class FakeAnkiCloze(AnkiCloze):
    text: str = "FakeText"
    base_deck: str = "FakeBaseDeck"
    tags: Sequence[str] = field(default_factory=fake_tag_factory)
    css: str = "FakeCSS"
    uuid: int = 0
    edit_url: str = "FakeEditURL"


@dataclass(frozen=True)
class AnkiQA(AnkiPrompt):
    base_deck: str
    tags: Sequence[str]
    question: str
    answer: str
    css: str
    uuid: int  # UUID used for scheduling. If a new note is added with the same uuid, it will override the old note.

    @property
    def genanki_model(self) -> genanki.Model:
        model_fields = [
            {"name": "Question"},
            {"name": "Answer"},
            {"name": "Extra"},
            {"name": "UUID"},
        ]

        QUESTION_STR = r"{{ Question }}"
        TTS_QUESTION_STR = r"{{ tts en_US voices=Apple_Samantha speed=1.05:Question }}"

        ANSWER_STR = r"{{ Answer }}"
        TTS_ANSWER_STR = r"{{ tts en_US voices=Apple_Samantha speed=1.05:Answer }}"

        EXTRA_STR = r"{{ Extra }}"

        model_template = [
            {
                "name": "Ankdown QA Card with UUID",
                "qfmt": f"""
<div class="front">
    {QUESTION_STR}{TTS_QUESTION_STR}
</div>
<div class="extra">
    {EXTRA_STR}
</div>
            """,
                "afmt": f"""
<div class="back">
    <div class="question">
        {QUESTION_STR}
    </div>
    <div class="answer">
        {ANSWER_STR}{TTS_ANSWER_STR}
    </div>
    <div class="extra">
        {EXTRA_STR}
    </div>
</div>
            """,
            }
        ]

        return genanki.Model(
            model_id=hash_str_to_int("Ankdown QA with UUID"),
            name=("Ankdown QA with UUID"),
            fields=model_fields,
            templates=model_template,
            css=self.css,
            model_type=0,
        )

    def _extra_field_content(self) -> str:
        return "" if not self.edit_url else edit_button(self.edit_url)

    def to_genanki_note(self) -> genanki.Note:
        return genanki.Note(
            guid=str(self.uuid),
            model=self.genanki_model,
            fields=[
                self._field_to_html(self.question),
                self._field_to_html(self.answer),
                self._extra_field_content,
                str(self.uuid),
            ],
            tags=self.tags,
        )

    @property
    def deck(self) -> str:
        base_deck = super().deck
        wiki_links = get_terms_surrounded_by_underscores(self.question)
        wiki_subdeck = "-".join(sorted(wiki_links))

        if wiki_subdeck != "":
            return f"{base_deck}::{wiki_subdeck}"
        return base_deck


@dataclass(frozen=True)
class FakeAnkiQA(AnkiQA):
    base_deck: str = "FakeBaseDeck"
    tags: Sequence[str] = field(default_factory=fake_tag_factory)
    question: str = "FakeQuestion"
    answer: str = "FakeAnswer"
    css: str = "FakeCSS"
    uuid: int = 0
    edit_url: str = "FakeEditURL"


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
            FakeAnkiQA(tags=["anki/deck/Subdeck"], question="What are _Wikilinks_ on _Wikipedia_?"),
            "FakeBaseDeck::Subdeck::Wikilinks-Wikipedia",
        ),
        QAExample(
            FakeAnkiQA(question="On _Wikipedia_, what are _Wikilinks_?"),
            "FakeBaseDeck::Wikilinks-Wikipedia",
        ),
        QAExample(FakeAnkiQA(question="Without wikilinks?"), "FakeBaseDeck"),
    ],
)
def should_match_deck(example: QAExample):
    assert example.card.deck == example.deck


def should_format():
    card = FakeAnkiQA(question="Q. This is a _question_?")
    note = card.to_genanki_note()
    assert note.fields[0] == "<p>Q. This is a <em>question</em>?</p>"  # type: ignore


def edit_button(url: str) -> str:
    return f"""<a href="{url}" style="background-color: #5f0069;
border: none;
color: white;
padding: 0.8em;
text-align: center;
text-decoration: none;
font-size: 0.8em;
font-family: 'Inter', sans-serif;
float: right;
border-radius: 8px;
opacity: 0.8;
">Obsidian</a>"""
