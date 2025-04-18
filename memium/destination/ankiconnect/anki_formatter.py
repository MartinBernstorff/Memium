from dataclasses import dataclass

import genanki

from memium.destination.ankiconnect.anki_model import AnkiQAModel
from memium.utils.hash_cleaned_str import hash_str_to_int
from memium.utils.markdown import md_to_html


@dataclass(frozen=True)
class AnkiQAFormatter:
    css: str

    CARD_NAME = "Ankdown QA with raw text"

    def format(self, model: AnkiQAModel) -> genanki.Note:
        return genanki.Note(
            guid=str(model.raw_prompt.scheduling_uid),
            model=self._genanki_model(model),
            fields=[
                *[md_to_html(getattr(model, field)) for field in model.formatted_field_names],
                model.raw_prompt.question,
                model.raw_prompt.answer,
            ],
            tags=model.tags,
        )

    def _genanki_model(self, model: AnkiQAModel) -> genanki.Model:
        return genanki.Model(
            model_id=hash_str_to_int(self.CARD_NAME),
            name=(self.CARD_NAME),
            fields=[
                {"name": field}
                for field in [*model.formatted_field_names, "raw_question", "raw_answer"]
            ],
            templates=self._model_template(model),
            css=self.css,
            model_type=0,
        )

    def _model_template(self, model: AnkiQAModel) -> list[dict[str, str]]:
        # TTS_QUESTION_STR = r"{{ tts en_US voices=Apple_Samantha speed=1.05:Question }}"  # noqa: ERA001
        # TTS_ANSWER_STR = r"{{ tts en_US voices=Apple_Samantha speed=1.05:Answer }}"  # noqa: ERA001

        QUESTION_PLACEHOLDER = r"{{ Question }}"
        ANSWER_PLACEHOLDER = r"{{ Answer }}"
        EXTRA_PLACEHOLDER = r"{{ Extra }}"

        placeholders = [QUESTION_PLACEHOLDER, ANSWER_PLACEHOLDER, EXTRA_PLACEHOLDER]

        for placeholder in placeholders:
            if (
                placeholder.replace(r"{{ ", "").replace(r" }}", "")
                not in model.formatted_field_names
            ):
                raise ValueError(f"Field {placeholder} is not defined in the model")

        return [
            {
                "name": self.CARD_NAME,
                "qfmt": f"""
<div class="front">{EXTRA_PLACEHOLDER}
    {QUESTION_PLACEHOLDER}
</div>""",
                "afmt": f"""
<div class="back">{EXTRA_PLACEHOLDER}
    <div class="question">
        {QUESTION_PLACEHOLDER}
    </div>
    <div class="answer">
        {ANSWER_PLACEHOLDER}
    </div>
</div>
            """,
            }
        ]
