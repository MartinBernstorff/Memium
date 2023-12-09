from dataclasses import dataclass

import genanki

from personal_mnemonic_medium.data_access.exporters.anki.anki_css import (
    CARD_MODEL_CSS,
)

from ....int_hash_str import int_hash_str
from ....utils.clean_str import clean_str
from .anki_prompt_converter import AnkiCard


@dataclass(frozen=True)
class AnkiQA(AnkiCard):
    question: str
    answer: str
    css: str = CARD_MODEL_CSS

    @property
    def uuid(self) -> int:
        return int_hash_str(clean_str(self.question))

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
            model_id=int_hash_str("Ankdown QA with UUID"),
            name=("Ankdown QA with UUID"),
            fields=model_fields,
            templates=model_template,
            css=self.css,
            model_type=0,
        )
