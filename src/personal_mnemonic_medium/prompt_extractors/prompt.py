from personal_mnemonic_medium.note_factories.note import Document


class Prompt:
    def __init__(
        self,
        note_uuid: str,
        source_note: Document,
        tags: list[str] | None = None,
        line_nr: int | None = None,
    ):
        self.tags = tags
        self.note_uuid = note_uuid
        self.source_note = source_note
        self.line_nr = line_nr
