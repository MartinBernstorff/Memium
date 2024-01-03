from collections.abc import Sequence
from dataclasses import dataclass

import genanki

from ...utils.hash_cleaned_str import hash_str_to_int
from .anki_prompt import AnkiPrompt


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
        TTS_QUESTION_STR = (
            r"{{ tts en_US voices=Apple_Samantha speed=1.05:Question }}"
        )

        ANSWER_STR = r"{{ Answer }}"
        TTS_ANSWER_STR = (
            r"{{ tts en_US voices=Apple_Samantha speed=1.05:Answer }}"
        )

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

    def to_genanki_note(self) -> genanki.Note:
        return genanki.Note(
            guid=str(self.uuid),
            model=self.genanki_model,
            fields=[
                self.field_to_html(self.question),
                self.field_to_html(self.answer),
                " ".join(self.tags),
                str(self.uuid),
            ],
            tags=self.tags,
        )
