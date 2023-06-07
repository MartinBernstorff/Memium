import hashlib
import os
import re
import urllib
from pathlib import Path
from typing import Any, List, Literal, Optional, Tuple

import genanki
import misaka

from personal_mnemonic_medium.exporters.anki.globals import CONFIG
from personal_mnemonic_medium.note_factories.note import Document
from personal_mnemonic_medium.prompt_extractors.prompt import Prompt


def strip_header(string: str) -> str:
    """Strip first occurrence of a markdown level 1 header"""
    return re.sub(r"^#.*\n", "", string)


def field_to_html(field: Any) -> str:
    # Math processing
    """
    Need to extract the math in brackets so that it doesn't get markdowned.
    If math is separated with dollar sign it is converted to brackets.
    """
    if CONFIG["dollar"]:
        for sep, (op, cl) in [("$$", (r"\\[", r"\\]")), ("$", (r"\\(", r"\\)"))]:
            escaped_sep = sep.replace(r"$", r"\$")
            # ignore escaped dollar signs when splitting the field
            field = re.split(rf"(?<!\\){escaped_sep}", field)
            # add op(en) and cl(osing) brackets to every second element of the list
            field[1::2] = [op + e + cl for e in field[1::2]]
            field = "".join(field)
    else:
        for bracket in ["(", ")", "[", "]"]:
            field = field.replace(rf"\{bracket}", rf"\\{bracket}")
            # backslashes, man.

    for token in ["*", "/"]:
        if token == "/":
            replacement = "*"
        elif token == "*":
            replacement = "**"

        pattern = f"\\{token}[^<>\\-\n]+\\{token}"

        token_instances = re.findall(pattern, field)

        for instance in token_instances:
            field = field.replace(instance, replacement + instance[1:-1] + replacement)  # type: ignore

    # Make sure every \n converts into a newline
    field = field.replace("\n", "  \n")

    return misaka.html(field, extensions=("fenced-code", "math"))


def compile_field(fieldtext: str) -> str:
    """Turn source markdown into an HTML field suitable for Anki."""
    fieldtext_sans_wiki = fieldtext.replace("[[", "<u>").replace("]]", "</u>")
    return field_to_html(fieldtext_sans_wiki)


def simple_hash(text: str) -> int:
    """MD5 of text, mod 2^63. Probably not a great hash function."""
    comp_hash = int(hashlib.sha256(text.encode("utf-8")).hexdigest(), 16) % 10**10

    return comp_hash


class AnkiCard:
    """A single anki card."""

    def __init__(
        self,
        fields: List[str],
        source_markdown: str,
        source_prompt: Prompt,
        source_note: Document,
        model_type: Literal["QA", "Cloze"],
        tags: Optional[List[str]] = None,
    ):
        self.markdown_fields = fields
        self.compiled_fields = [compile_field(field) for field in fields]
        self.source_markdown = source_markdown
        self.tags = tags
        self.model_type = model_type
        self.model = self.model_string_to_genanki_model(model_type=model_type)
        self.source_prompt = source_prompt
        self.source_document = source_note

        if self.has_subdeck_tag(self.source_markdown):
            self.subdeck = self.get_subdeck_name(self.source_markdown)
        else:
            self.subdeck = "Default"

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
            prompt_field = self.compiled_fields[0]
            cloze_fields = re.findall(r"{{c.+?}", prompt_field)

            cloze = cloze_fields[0]

            basename = self.source_document.uuid
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
        self.compiled_fields.append(compile_field(field))

    def get_obsidian_uri(self) -> str:
        """Get the obsidian URI for the source document."""
        vault = urllib.parse.quote(self.source_document.source_path.parent.name)
        file = urllib.parse.quote(self.source_document.source_path.name)

        href = f"obsidian://open?vault={vault}&file={file}"

        return f'<h4 class="right"><a href="{href}">Open</a></h4>'

    def to_genanki_note(self) -> genanki.Note:
        """Produce a genanki.Note with the specified guid."""
        if len(self.compiled_fields) > len(self.model.fields):
            raise ValueError(
                f"Too many fields for model {self.model.name}: {self.compiled_fields}",
            )

        if len(self.compiled_fields) < len(self.model.fields):
            while len(self.compiled_fields) < len(self.model.fields):
                before_extras_field = len(self.compiled_fields) == 2
                before_uuid_field = len(self.compiled_fields) == 3

                if before_extras_field:
                    self.add_field(self.get_obsidian_uri())

                if before_uuid_field:
                    self.add_field(str(self.card_uuid))

                self.compiled_fields.append("")

        return genanki.Note(
            model=self.model,
            fields=self.compiled_fields,
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
        return Path(self.source_document.source_path).parent

    def determine_media_references(self):
        """Find all media references in a card"""
        for i, field in enumerate(self.compiled_fields):
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
            self.compiled_fields[i] = re.sub(r'alt="[^"]*?"', "", current_stage)
