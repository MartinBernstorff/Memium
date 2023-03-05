from typing import List, Optional

from personal_mnemonic_medium.note_factories.note import Note


class Prompt:
    def __init__(
        self,
        tags: List[str],
        uuid: str,
        source_note: Note,
    ):
        self.tags = tags
        self.uuid = uuid
        self.source_note = source_note
