from collections.abc import Sequence
from typing import Protocol

from personal_mnemonic_medium.data_access.document_ingesters.document import (
    Document,
)


class Prompt(Protocol):
    source_note: Document
    line_nr: int | None

    @property
    def note_uuid(self) -> str:
        ...

    @property
    def tags(self) -> Sequence[str]:
        ...

    def __init__(
        self,
        content: str,
        note_uuid: str,
        source_note: Document,
        tags: list[str] | None = None,
        line_nr: int | None = None,
    ):
        ...
