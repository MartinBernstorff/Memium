from typing import List, Optional

from personal_mnemonic_medium.note_factories.note import Note


class Prompt:
    def __init__(
        self,
        tags: List[str],
        subdeck: str,
        uuid: str,
        source_note: Optional[Note] = None,
    ):
        self.tags = tags
        self.subdeck = subdeck
        self.uuid = uuid
        self.source_note = source_note
