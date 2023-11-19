import re
from collections.abc import Callable
from pathlib import Path
import textwrap

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
from personal_mnemonic_medium.domain.prompt_extractors.prompt import (
    Prompt,
)
from personal_mnemonic_medium.domain.url_generators.obsidian_url import (
    get_obsidian_url,
)
from personal_mnemonic_medium.utils.hasher import simple_hash


class AnkiCloze(AnkiCard):
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
        model_name = "Ankdown Cloze with UUID"
        CARD_MATHJAX_CONTENT = textwrap.dedent(
            """\

"""
        )
        # TODO: refactor: remove mathjax if tests keep passing

        return genanki.Model(
            model_id=simple_hash(model_name),
            name=model_name,
            fields=[
                {"name": "Text"},
                {"name": "Extra"},
                {"name": "Tags"},
                {"name": "UUID"},
            ],
            templates=[
                {
                    "name": "Ankdown Cloze Card with UUID",
                    "qfmt": r"{{{{cloze:Text}}}}\n<div class='extra'>{{{{Extra}}}}</div>\n{}".format(
                        CARD_MATHJAX_CONTENT
                    ),
                    "afmt": r"{{{{cloze:Text}}}}\n<div class='extra'>{{{{Extra}}}}</div>\n{}".format(
                        CARD_MATHJAX_CONTENT
                    ),
                }
            ],
            css=CARD_MODEL_CSS,
            model_type=1,  # This is the model_type number for genanki, takes 0 for QA or 1 for cloze
        )

    @property
    def card_uuid(self) -> int:
        prompt_field = self.html_fields[0]
        cloze_fields = re.findall(r"{{c.+?}", prompt_field)

        cloze = cloze_fields[0]

        basename = self.source_doc.uuid
        hash_value = simple_hash(f"{cloze}{basename}")

        return hash_value
