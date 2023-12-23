from collections.abc import Sequence
from dataclasses import dataclass

import genanki

from ...utils.hash_cleaned_str import clean_str, int_hash_str
from .anki_card import AnkiCard


@dataclass(frozen=True)
class AnkiCloze(AnkiCard):
    base_deck: str
    tags: Sequence[str]
    text: str
    css: str

    @property
    def uuid(self) -> int:
        return int_hash_str(clean_str(self.text))

    @property
    def genanki_model(self) -> genanki.Model:
        model_name = "Ankdown Cloze with UUID"

        return genanki.Model(
            model_id=int_hash_str(model_name),
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
                    "qfmt": r"{{{{cloze:Text}}}}\n<div class='extra'>{{{{Extra}}}}</div>\n{}",
                    "afmt": r"{{{{cloze:Text}}}}\n<div class='extra'>{{{{Extra}}}}</div>\n{}",
                }
            ],
            css=self.css,
            model_type=1,  # This is the model_type number for genanki, takes 0 for QA or 1 for cloze
        )

    def to_genanki_note(self) -> genanki.Note:
        return genanki.Note(
            guid=str(self.uuid),
            model=self.genanki_model,
            fields=[self.text, "", " ".join(self.tags), str(self.uuid)],
            tags=self.tags,
        )
