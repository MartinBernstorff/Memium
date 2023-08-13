import copy
import os
import re
from pathlib import Path
from typing import Any, Callable, List, Literal, Optional, Tuple

import genanki

from personal_mnemonic_medium.exporters.markdown_to_html.html_compiler import (
    compile_field,
)
from personal_mnemonic_medium.exporters.url_generators.obsidian_url import (
    get_obsidian_url,
)
from personal_mnemonic_medium.note_factories.note import Document
from personal_mnemonic_medium.prompt_extractors.prompt import Prompt
from personal_mnemonic_medium.utils.hasher import simple_hash


class AnkiCard:
    """A single anki card."""

    def __init__(
        self,
        fields: List[str],
        source_prompt: Prompt,
        model_type: Literal["QA", "Cloze"],
        url_generator: Callable[[Path, Optional[int]], str] = get_obsidian_url,
        html_compiler: Callable[[str], str] = compile_field,
    ):
        self.markdown_fields = fields
        self.model_type = model_type
        self.model = self.model_string_to_genanki_model(model_type=model_type)
        self.html_compiler = html_compiler
        self.url_generator = url_generator

        self.source_prompt = copy.deepcopy(source_prompt)

    @property
    def source_markdown(self) -> str:
        return self.source_doc.content

    @property
    def html_fields(self) -> List[str]:
        return list(map(self.html_compiler, self.markdown_fields))

    @property
    def tags(self) -> List[str]:
        return self.source_doc.tags

    @property
    def subdeck(self) -> str:
        if self.has_subdeck_tag(self.source_markdown):
            return self.get_subdeck_name(self.source_markdown)

        return "Default"

    @property
    def source_doc(self) -> Document:
        return self.source_prompt.source_note

    @staticmethod
    def has_subdeck_tag(input_str: str) -> bool:
        return len(re.findall(r"#anki\/deck\/\S+", input_str)) != 0

    @staticmethod
    def get_subdeck_name(input_str: str) -> str:
        return (
            re.findall(r"#anki\/deck\/\S+", input_str)[0][11:]
            .replace("/", "::")
            .replace("#", "")
        )

    def model_string_to_genanki_model(self, model_type: str = "Cloze") -> genanki.Model:
        GENANKI_QA_MODEL_TYPE = 0
        GENANKI_CLOZE_MODEL_TYPE = 1

        global CONFIG  # noqa

        if model_type == "Cloze":
            return genanki.Model(
                model_id=simple_hash(CONFIG["card_model_name_cloze"]),  # type: ignore
                name=CONFIG["card_model_name_cloze"],
                fields=CONFIG["card_model_fields_cloze"],
                templates=CONFIG["card_model_template_cloze"],
                css=CONFIG["card_model_css"],
                model_type=GENANKI_CLOZE_MODEL_TYPE,  # This is the model_type number for genanki, takes 0 for QA or 1 for cloze
            )

        if model_type == "QA":
            return genanki.Model(
                model_id=simple_hash(CONFIG["card_model_name_qa"]),  # type: ignore
                name=CONFIG["card_model_name_qa"],
                fields=CONFIG["card_model_fields_qa"],
                templates=CONFIG["card_model_template_qa"],
                css=CONFIG["card_model_css"],
                model_type=GENANKI_QA_MODEL_TYPE,
            )
        raise ValueError("model_type must be either Cloze or QA")

    @property
    def deckname(self) -> str:
        try:
            if len(self.subdeck) > 0:
                return (
                    "0. Don't click me::1. Active::Personal Mnemonic Medium::"
                    + self.subdeck
                )
            raise ValueError(
                "Subdeck length is 0",
            )  # This is purposefully non-valid code
        except:  # noqa
            return "0. Don't click me::1. Active::Personal Mnemonic Medium"

    @property
    def card_uuid(self) -> int:  # The identifier for cards
        if self.model_type == "Cloze":
            prompt_field = self.html_fields[0]
            cloze_fields = re.findall(r"{{c.+?}", prompt_field)

            cloze = cloze_fields[0]

            basename = self.source_doc.uuid
            hash_value = simple_hash(f"{cloze}{basename}")

            return hash_value

        # Q/A cards should be unique from the phrasing of the question.
        # A bunch of this is to maintain backwards compatability with a prior version of the code, ensuring that the hash is the same.
        hash_string = self.markdown_fields[0] + "\n"

        if hash_string[0] != " ":
            hash_string = " " + hash_string

        output_hash = simple_hash(f"{hash_string}")
        return output_hash

    def add_field(self, field: Any):
        self.markdown_fields.append(field)

    def get_source_button(self) -> str:
        """Get the button to open the source document."""
        url = self.url_generator(
            self.source_doc.source_path, self.source_prompt.line_nr,
        )
        html = f'<h4 class="right"><a href="{url}">Open</a></h4>'
        return html

    def to_genanki_note(self) -> genanki.Note:
        """Produce a genanki. Note with the specified guid."""
        if len(self.html_fields) > len(self.model.fields):
            raise ValueError(
                f"Too many fields for model {self.model.name}: {self.html_fields}",
            )

        if len(self.html_fields) < len(self.model.fields):
            while len(self.html_fields) < len(self.model.fields):
                before_extras_field = len(self.html_fields) == 2
                if before_extras_field:
                    self.add_field(self.get_source_button())
                    continue

                before_uuid_field = len(self.html_fields) == 3
                if before_uuid_field:
                    self.add_field(str(self.card_uuid))
                    continue

                self.html_fields.append("")

        return genanki.Note(
            model=self.model,
            fields=self.html_fields,
            guid=self.card_uuid,
            tags=self.tags,
        )

    def make_ref_pair(self, filename: str) -> Tuple[Path, str]:
        """Take a filename relative to the card, and make it absolute."""
        newname = "%".join(filename.split(os.sep))

        if os.path.isabs(filename):  # noqa
            abspath = Path(filename)
        else:
            abspath = Path(self.get_deck_dir()) / filename
        return (abspath, newname)

    def get_deck_dir(self) -> Path:
        # This is all it takes
        return Path(self.source_doc.source_path).parent

    def determine_media_references(self):
        """Find all media references in a card"""
        for i, field in enumerate(self.html_fields):
            current_stage = field
            for regex in [
                r'src="([^"]*?)"',
            ]:  # TODO not sure how this should work:, r'\[sound:(.*?)\]']:
                results = []

                def process_match(m) -> str:  # noqa
                    initial_contents = m.group(1)
                    abspath, newpath = self.make_ref_pair(initial_contents)
                    results.append((abspath, newpath))  # noqa
                    return r'src="' + newpath + '"'

                current_stage = re.sub(regex, process_match, current_stage)

                for r in results:
                    yield r

            # Anki seems to hate alt tags :(
            self.html_fields[i] = re.sub(r'alt="[^"]*?"', "", current_stage)
