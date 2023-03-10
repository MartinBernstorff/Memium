from typing import Optional

from personal_mnemonic_medium.note_factories.note import Note


class Prompt:
    def __init__(
        self,
        note_uuid: str,
        source_note: Note,
        tags: Optional[list[str]] = None,
    ):
        self.tags = tags
        self.note_uuid = note_uuid
        self.source_note = source_note
