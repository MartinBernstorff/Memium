import hashlib
import os
import re
from typing import List, Literal

import genanki

from personal_mnemonic_medium.exporters.anki.globals import CONFIG


class AnkiCard(object):
    """A single anki card."""

    def __init__(
        self,
        fields: List[str],
        source_markdown: str,
        tags: List[str],
        model_type: Literal["QA", "Cloze", "QA_DK"],
        note_uuid: str,
    ):
        self.fields = fields
        self.source_markdown = source_markdown
        self.tags = tags
        self.model = self.model_string_to_genanki_model(model_type=model_type)
        self.note_uuid = note_uuid

        if self.has_subdeck_tag(self.source_markdown):
            self.subdeck = self.get_subdeck_name(self.source_markdown)
        else:
            self.subdeck = "Default"

    def get_deck_dir(self):
        return os.path.dirname(self.filepath)

    @staticmethod
    def has_subdeck_tag(input_str) -> bool:
        return len(re.findall(r"#anki\/deck\/\S+", input_str)) != 0

    @staticmethod
    def get_subdeck_name(input_str) -> str:
        return (
            re.findall(r"#anki\/deck\/\S+", input_str)[0][11:]
            .replace("/", "::")
            .replace("#", "")
        )

    def model_string_to_genanki_model(self, model_type="Cloze") -> genanki.Model:
        GENANKI_QA_MODEL_TYPE = 1
        GENANKI_CLOZE_MODEL_TYPE = 1

        if model_type == "Cloze":
            return genanki.Model(
                model_id=simple_hash(CONFIG["card_model_name_cloze"]),
                name=CONFIG["card_model_name_cloze"],
                fields=CONFIG["card_model_fields_cloze"],
                templates=CONFIG["card_model_template_cloze"],
                css=CONFIG["card_model_css"],
                model_type=GENANKI_CLOZE_MODEL_TYPE,  # This is the model_type number for genanki, takes 0 for QA or 1 for cloze
            )
        elif model_type == "QA":
            return genanki.Model(
                model_id=simple_hash(CONFIG["card_model_name_qa"]),
                name=CONFIG["card_model_name_qa"],
                fields=CONFIG["card_model_fields_qa"],
                templates=CONFIG["card_model_template_qa"],
                css=CONFIG["card_model_css"],
                model_type=GENANKI_QA_MODEL_TYPE,
            )
        elif model_type == "QA_DA":
            return genanki.Model(
                model_id=simple_hash(CONFIG["card_model_name_qa_da"]),
                name=CONFIG["card_model_name_qa_da"],
                fields=CONFIG["card_model_fields_qa"],
                templates=CONFIG["card_model_template_qa_da"],
                css=CONFIG["card_model_css"],
                model_type=GENANKI_QA_MODEL_TYPE,
            )
        else:
            raise ValueError("model_type must be either Cloze or QA")

    def deckname(self):
        try:
            if len(self.subdeck) > 0:
                return (
                    "0. Don't click me::1. Active::Personal Mnemonic Medium::"
                    + self.subdeck
                )
            else:
                raise ValueError(
                    "Subdeck length is 0"
                )  # This is purposefully non-valid code
        except:
            return "0. Don't click me::1. Active::Personal Mnemonic Medium"

    def basename(self):
        with open(self.filepath, "r", encoding="utf8") as file:
            full_string = ""

            for line in file.readlines():
                full_string += line

            uid = re.findall(r"<!-- {BearID:.+} -->", full_string)[0]
            return uid

    def card_id(self):  # The identifier for cards
        if len(re.findall(r"{(?!BearID).[^}]*}", self.fields[0])) > 0:
            # Excludes bearID. We don't want clozes to update just because the surrounding information did.
            cloze = re.findall(r"{(?!BearID).[^}]*}", self.fields[0])[0]

            # Card ID is the cloze deletions + BearID
            return simple_hash(f"{cloze}{self.basename()}")

        else:  # If not cloze
            # Q/A cards should be unique from their phrasing. Now it's not tied to a given note.
            hash_string = self.source_markdown[0]

            hash = simple_hash(f"{hash_string}")
            return hash

    def note_uuid(self):  # The identifier for notes
        return (
            self.card_id()
        )  # This is now the hash of the BearID and the cloze or question side

    def add_field(self, field, is_markdown=True):
        self.fields.append(compile_field(field, is_markdown))
        self.source_markdown.append(field)

    def has_cloze(self):
        return len(self.fields) > 0 and any("{" in s for s in self.fields)

    def has_front_and_back(self):
        return len(self.fields) >= 2

    def finalize(self):
        """Ensure proper shape, for extraction into result formats."""
        if len(self.fields) > 3:
            self.fields = self.fields[:3]
        else:
            while len(self.fields) < 3:
                self.fields.append("")

    def to_genanki_note(self):
        """Produce a genanki.Note with the specified guid."""
        return genanki.Note(
            model=self.model, fields=self.fields, guid=self.note_uuid, tags=self.tags
        )

    def make_ref_pair(self, filename):
        """Take a filename relative to the card, and make it absolute."""
        newname = "%".join(filename.split(os.sep))

        if os.path.isabs(filename):
            abspath = filename
        else:
            abspath = os.path.normpath(os.path.join(self.get_deck_dir(), filename))
        return (abspath, newname)

    def determine_media_references(self):
        """Find all media references in a card"""
        for i, field in enumerate(self.fields):
            current_stage = field
            for regex in [
                r'src="([^"]*?)"'
            ]:  # TODO not sure how this should work:, r'\[sound:(.*?)\]']:
                results = []

                def process_match(m):
                    initial_contents = m.group(1)
                    abspath, newpath = self.make_ref_pair(initial_contents)
                    results.append((abspath, newpath))
                    return r'src="' + newpath + '"'

                current_stage = re.sub(regex, process_match, current_stage)

                for r in results:
                    yield r

            # Anki seems to hate alt tags :(
            self.fields[i] = re.sub(r'alt="[^"]*?"', "", current_stage)


def compile_field(fieldtext, is_markdown):
    """Turn source markdown into an HTML field suitable for Anki."""
    fieldtext_sans_wiki = fieldtext.replace("[[", "<u>").replace("]]", "</u>")

    fieldtext_sans_headers = strip_header(fieldtext_sans_wiki)

    if is_markdown == 0:
        return fieldtext
    else:
        return field_to_html(fieldtext_sans_headers)


def simple_hash(text: str) -> int:
    """MD5 of text, mod 2^63. Probably not a great hash function."""
    comp_hash = int(hashlib.sha256(text.encode("utf-8")).hexdigest(), 16) % 10**10

    return comp_hash
