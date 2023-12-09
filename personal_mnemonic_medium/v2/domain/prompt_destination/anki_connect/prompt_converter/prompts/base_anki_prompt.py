from collections.abc import Sequence
from dataclasses import dataclass
from typing import Protocol

import genanki


@dataclass(frozen=True)
class AnkiCard(Protocol):
    deck: str
    tags: Sequence[str]

    @property
    def uuid(self) -> int:
        ...

    @property
    def genanki_model(self) -> genanki.Model:
        ...

    def to_genanki_note(self) -> genanki.Note:
        ...
