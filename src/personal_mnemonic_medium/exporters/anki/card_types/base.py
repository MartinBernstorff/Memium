import copy
import os
import re
from abc import ABC, abstractmethod
from collections.abc import Callable, Iterator
from pathlib import Path
from typing import Any

import genanki
from personal_mnemonic_medium.exporters.markdown_to_html.html_compiler import (
    compile_field,
)
from personal_mnemonic_medium.exporters.url_generators.obsidian_url import (
    get_obsidian_url,
)
from personal_mnemonic_medium.note_factories.note import Document
from personal_mnemonic_medium.prompt_extractors.prompt import Prompt


class AnkiCard(ABC):
    """A single anki card."""

    def __init__(
        self,
        fields: list[str],
        source_prompt: Prompt,
        url_generator: Callable[
            [Path, int | None], str
        ] = get_obsidian_url,
        html_compiler: Callable[[str], str] = compile_field,
    ):
        self.markdown_fields = fields
        self.html_compiler = html_compiler
        self.url_generator = url_generator

        self.source_prompt = copy.deepcopy(source_prompt)

    @property
    def source_markdown(self) -> str:
        return self.source_doc.content

    @property
    def html_fields(self) -> list[str]:
        return list(map(self.html_compiler, self.markdown_fields))

    @property
    def tags(self) -> list[str]:
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

    @property
    @abstractmethod
    def genanki_model(self) -> genanki.Model:
        pass

    @property
    def deckname(self) -> str:
        try:
            if len(self.subdeck) > 0:
                return (
                    "0. Don't click me::1. Active::Personal Mnemonic Medium::"
                    + self.subdeck
                )
            raise ValueError(
                "Subdeck length is 0"
            )  # This is purposefully non-valid code
        except:  # noqa
            return "0. Don't click me::1. Active::Personal Mnemonic Medium"

    @property
    @abstractmethod
    def card_uuid(self) -> int:  # The identifier for cards
        pass

    def add_field(self, field: Any):
        self.markdown_fields.append(field)

    def get_source_button(self) -> str:
        """Get the button to open the source document."""
        url = self.url_generator(
            self.source_doc.source_path, self.source_prompt.line_nr
        )
        html = f'<h4 class="right"><a href="{url}">Open</a></h4>'
        return html

    def to_genanki_note(self) -> genanki.Note:
        """Produce a genanki. Note with the specified guid."""
        if len(self.html_fields) > len(self.genanki_model.fields):  # type: ignore
            raise ValueError(
                f"Too many fields for model {self.genanki_model.name}: {self.html_fields}"  # type: ignore
            )

        if len(self.html_fields) < len(self.genanki_model.fields):  # type: ignore
            while len(self.html_fields) < len(
                self.genanki_model.fields  # type: ignore
            ):  # type: ignore
                before_extras_field = len(self.html_fields) == 2
                if before_extras_field:
                    self.add_field(self.get_source_button())
                    continue

                before_uuid_field = len(self.html_fields) == 3
                if before_uuid_field:
                    self.add_field(str(self.card_uuid))
                    continue

                self.add_field("")

        return genanki.Note(
            model=self.genanki_model,
            fields=self.html_fields,
            guid=self.card_uuid,
            tags=self.tags,
        )

    def make_ref_pair(self, filename: str) -> tuple[Path, str]:
        """Take a filename relative to the card, and make it absolute."""
        newname = "%".join(filename.split(os.sep))  # type: ignore  # noqa: PTH206

        if os.path.isabs(filename):  # noqa
            abspath = Path(filename)
        else:
            abspath = Path(self.get_deck_dir()) / filename
        return (abspath, newname)

    def get_deck_dir(self) -> Path:
        # This is all it takes
        return Path(self.source_doc.source_path).parent

    def determine_media_references(
        self
    ) -> Iterator[tuple[Path, Path]]:
        """Find all media references in a card"""
        for i, field in enumerate(self.html_fields):
            current_stage = field
            for regex in [
                r'src="([^"]*?)"'
            ]:  # TODO not sure how this should work:, r'\[sound:(.*?)\]']:
                results = []

                def process_match(m) -> str:  # noqa # type: ignore
                    initial_contents = m.group(1)  # type: ignore
                    abspath, newpath = self.make_ref_pair(
                        initial_contents  # type: ignore
                    )  # type: ignore
                    results.append((abspath, newpath))  # noqa # type: ignore
                    return r'src="' + newpath + '"'

                current_stage = re.sub(
                    regex,
                    process_match,
                    current_stage,  # type: ignore
                )  # type: ignore

                yield from results

            # Anki seems to hate alt tags :(
            self.html_fields[i] = re.sub(
                r'alt="[^"]*?"', "", current_stage
            )
