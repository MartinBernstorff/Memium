from dataclasses import dataclass

from .......data_access.exporters.anki.anki_css.py import (
    CARD_MODEL_CSS,
)
from ..anki_prompt_converter.py import AnkiCard


@dataclass(frozen=True)
class AnkiCloze(AnkiCard):
    text: str
    css: str = CARD_MODEL_CSS
