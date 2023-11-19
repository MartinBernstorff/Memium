from collections.abc import Callable  # noqa: I001
from pathlib import Path

import genanki
from personal_mnemonic_medium.data_access.exporters.anki.anki_css import (
    CARD_MODEL_CSS,
)
from personal_mnemonic_medium.data_access.exporters.anki.card_types.base import (
    AnkiCard,
)
from personal_mnemonic_medium.domain.markdown_to_html import (
    compile_field,
)
from personal_mnemonic_medium.domain.url_generators.obsidian_url import (
    get_obsidian_url,
)
from personal_mnemonic_medium.domain.prompt_extractors.prompt import (
    Prompt,
)
from personal_mnemonic_medium.utils.hasher import simple_hash


class AnkiQA(AnkiCard):
    def __init__(
        self,
        fields: list[str],
        source_prompt: Prompt,
        url_generator: Callable[
            [Path, int | None], str
        ] = get_obsidian_url,
        html_compiler: Callable[[str], str] = compile_field,
    ):
        super().__init__(
            fields=fields,
            source_prompt=source_prompt,
            url_generator=url_generator,
            html_compiler=html_compiler,
        )

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
            model_id=simple_hash("Ankdown QA with UUID"),
            name=("Ankdown QA with UUID"),
            fields=model_fields,
            templates=model_template,
            css=CARD_MODEL_CSS,
            model_type=0,
        )
        # TODO: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues/203 Refactor the CONFIG to be a dataclass

    @property
    def card_uuid(self) -> int:
        # Q/A cards should be unique from the phrasing of the question.
        # A bunch of this is to maintain backwards compatability with a prior version of the code, ensuring that the hash is the same.
        hash_string = self.markdown_fields[0] + "\n"

        if hash_string[0] != " ":
            hash_string = " " + hash_string

        output_hash = simple_hash(f"{hash_string}")
        return output_hash
