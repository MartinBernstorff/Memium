from typing import Protocol

from personal_mnemonic_medium.data_access.document_ingesters.document import (
    Document,
)


class Prompt(Protocol):
    note_uuid: str
    source_note: Document
    tags: list[str] | None
    line_nr: int | None

    def __init__(
        self,
        content: str,
        note_uuid: str,
        source_note: Document,
        tags: list[str] | None = None,
        line_nr: int | None = None,
    ):
        ...
