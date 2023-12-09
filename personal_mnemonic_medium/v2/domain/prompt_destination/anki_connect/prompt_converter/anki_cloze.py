from dataclasses import dataclass

import genanki

from ......data_access.exporters.anki.anki_css import CARD_MODEL_CSS
from ....int_hash_str import int_hash_str
from ....utils.clean_str import clean_str
from .anki_prompt_converter import AnkiCard


@dataclass(frozen=True)
class AnkiCloze(AnkiCard):
    text: str
    css: str = CARD_MODEL_CSS

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
