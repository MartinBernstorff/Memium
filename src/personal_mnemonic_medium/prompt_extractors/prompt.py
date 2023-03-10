from typing import List

from personal_mnemonic_medium.note_factories.note import Note


class Prompt:
    def __init__(
        self,
        tags: List[str],
        note_uuid: str,
        source_note: Note,
    ):
        self.tags = tags
        self.note_uuid = note_uuid
        self.source_note = source_note
