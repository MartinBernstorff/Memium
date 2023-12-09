from typing import Protocol

import genanki


class AnkiPrompt(Protocol):
    @property
    def uuid(self) -> int:
        ...

    @property
    def genanki_model(self) -> genanki.Model:
        ...
