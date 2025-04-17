from collections.abc import Sequence
from dataclasses import dataclass

import genanki

from memium.source.prompts.prompt_qa import QAPromptImpl
from memium.utils.extract_terms import get_terms_surrounded_by_underscores
from memium.utils.markdown_parser import md_to_html

from ...utils.hash_cleaned_str import hash_str_to_int


@dataclass(frozen=True)
class AnkiPrompt:
    prompt: QAPromptImpl
    source_title: str | None

    render_parent_doc: bool

    css: str

    base_deck: str
    tags: Sequence[str]

    edit_url: str | None

    @property
    def uuid(self) -> int:
        return self.prompt.scheduling_uid

    @property
    def genanki_model(self) -> genanki.Model:
        model_fields = [
            {"name": "Question"},
            {"name": "Answer"},
            {"name": "Extra"},
            {"name": "UUID"},
            {"name": "Question raw"},
            {"name": "Answer raw"},
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

        field_names = [d["name"] for d in model_fields]
        return genanki.Model(
            model_id=hash_str_to_int("-".join(field_names)),
            name=(f"Ankdown QA with {field_names}"),
            fields=model_fields,
            templates=model_template,
            css=self.css,
            model_type=0,
        )

    def _md_to_html(self, field: str) -> str:
        return md_to_html(field)

    @property
    def _extra_field_content(self) -> str:
        note_title = (
            f"<span style='opacity: 0.5; font-size: 0.7em; line-height: 0%;'>{self.source_title}</span>"
            if self.source_title and self.render_parent_doc
            else ""
        )
        edit_button_html = edit_button(self.edit_url) if self.edit_url else ""
        return f"<div class='edit_button' style='text-align: center;'>{edit_button_html}</div>{note_title}"

    def to_genanki_note(self) -> genanki.Note:
        return genanki.Note(
            guid=str(self.uuid),
            model=self.genanki_model,
            fields=[
                self._md_to_html(self.prompt.question),
                self._md_to_html(self.prompt.answer),
                self._extra_field_content,
                str(self.uuid),
                self.prompt.question,
                self.prompt.answer,
            ],
            tags=self.tags,
        )

    @property
    def deck(self) -> str:
        deck_prefix = "anki/deck/"
        deck_in_tags = (
            tag.replace(deck_prefix, "").replace("/", "::")
            for tag in self.tags
            if tag.startswith(deck_prefix)
        )
        subdeck = next(deck_in_tags, None)

        base_anki_deck = self.base_deck if subdeck is None else f"{self.base_deck}::{subdeck}"

        wiki_links = get_terms_surrounded_by_underscores(self.prompt.question)
        wiki_subdeck = "-".join(sorted(wiki_links))

        if wiki_subdeck != "":
            return f"{base_anki_deck}::{wiki_subdeck}"
        return base_anki_deck


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
