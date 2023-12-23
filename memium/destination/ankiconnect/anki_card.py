from abc import ABC, abstractmethod
from collections.abc import Sequence
from dataclasses import dataclass

import genanki


@dataclass(frozen=True)
class AnkiCard(ABC):
    base_deck: str
    tags: Sequence[str]

    @property
    @abstractmethod
    def uuid(self) -> int:
        ...

    @property
    @abstractmethod
    def genanki_model(self) -> genanki.Model:
        ...

    @abstractmethod
    def to_genanki_note(self) -> genanki.Note:
        ...

    @property
    def deck(self) -> str:
        deck_prefix = "anki/deck/"
        deck_in_tags = (
            tag.replace(deck_prefix, "").replace("/", "::")
            for tag in self.tags
            if tag.startswith(deck_prefix)
        )
        subdeck = next(deck_in_tags, None)

        if subdeck is None:
            return self.base_deck

        return f"{self.base_deck}::{subdeck}"
