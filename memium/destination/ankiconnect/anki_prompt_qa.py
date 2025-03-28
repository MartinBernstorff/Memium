from collections.abc import Sequence
from dataclasses import dataclass

import genanki

from memium.utils.extract_terms import get_terms_surrounded_by_underscores

from ...utils.hash_cleaned_str import hash_str_to_int
from .anki_prompt import AnkiPrompt


@dataclass(frozen=True)
class AnkiQA(AnkiPrompt):
    base_deck: str
    tags: Sequence[str]
    question: str
    answer: str
    source_title: str | None
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
        # TTS_QUESTION_STR = r"{{ tts en_US voices=Apple_Samantha speed=1.05:Question }}"  # noqa: ERA001

        ANSWER_STR = r"{{ Answer }}"
        # TTS_ANSWER_STR = r"{{ tts en_US voices=Apple_Samantha speed=1.05:Answer }}"  # noqa: ERA001

        EXTRA_STR = r"{{ Extra }}"

        model_template = [
            {
                "name": "Ankdown QA Card with UUID",
                "qfmt": f"""
<div class="front">{EXTRA_STR}
    {QUESTION_STR}
</div>""",
                "afmt": f"""
<div class="back">{EXTRA_STR}
    <div class="question">
        {QUESTION_STR}
    </div>
    <div class="answer">
        {ANSWER_STR}
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

    @property
    def _extra_field_content(self) -> str:
        note_title = (
            f"<span style='opacity: 0.5; font-size: 0.7em; line-height: 0%;'>{self.source_title}</span>"
            if self.source_title
            else ""
        )
        edit_button_html = edit_button(self.edit_url) if self.edit_url else ""
        return f"<div class='edit_button' style='text-align: center;'>{edit_button_html}</div>{note_title}"

    def to_genanki_note(self) -> genanki.Note:
        return genanki.Note(
            guid=str(self.uuid),
            model=self.genanki_model,
            fields=[
                self._to_html(self.question),
                self._to_html(self.answer),
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


def edit_button(url: str) -> str:
    return f"""<a href="{url}" style="background-color: #5f0069;
        border: none;
        color: white;
        padding: 0.8em;
        text-align: center;
        text-decoration: none;
        font-size: 0.8em;
        font-family: 'Inter', sans-serif;
        border-radius: 8px;
        opacity: 0.8;
">Obsidian</a>"""
