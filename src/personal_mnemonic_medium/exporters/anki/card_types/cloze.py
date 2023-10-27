import re
from collections.abc import Callable
from pathlib import Path

import genanki
from personal_mnemonic_medium.exporters.anki.card_types.base import (
    AnkiCard,
)
from personal_mnemonic_medium.exporters.anki.globals import CONFIG
from personal_mnemonic_medium.exporters.markdown_to_html.html_compiler import (
    compile_field,
)
from personal_mnemonic_medium.exporters.url_generators.obsidian_url import (
    get_obsidian_url,
)
from personal_mnemonic_medium.prompt_extractors.prompt import Prompt
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
        return genanki.Model(
            model_id=simple_hash(CONFIG["card_model_name_cloze"]),  # type: ignore
            name=CONFIG["card_model_name_cloze"],
            fields=CONFIG["card_model_fields_cloze"],
            templates=CONFIG["card_model_template_cloze"],
            css=CONFIG["card_model_css"],  # type: ignore
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
