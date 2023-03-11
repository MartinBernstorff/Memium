from typing import List, Optional

from personal_mnemonic_medium.note_factories.note import Document


class Prompt:
    def __init__(
        self,
        note_uuid: str,
        source_note: Document,
        tags: Optional[List[str]] = None,
    ):
        self.tags = tags
        self.note_uuid = note_uuid
        self.source_note = source_note
