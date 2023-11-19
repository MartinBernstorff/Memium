from collections.abc import Callable  # noqa: I001
from pathlib import Path

import genanki
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
from personal_mnemonic_medium.data_access.exporters.anki.globals import (  # noqa
    CONFIG,
)


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
        global CONFIG  # noqa
        return genanki.Model(
            model_id=simple_hash(CONFIG["card_model_name_qa"]),  # type: ignore
            name=CONFIG["card_model_name_qa"],  # type: ignore
            fields=CONFIG["card_model_fields_qa"],  # type: ignore
            templates=CONFIG["card_model_template_qa"],  # type: ignore
            css=CONFIG["card_model_css"],  # type: ignore
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
