from collections.abc import Sequence
from pathlib import Path

from memium.destination.ankiconnect.anki_converter import AnkiPromptConverter
from memium.destination.ankiconnect.anki_model import AnkiCardID, AnkiNoteID, AnkiQAModel
from memium.destination.ankiconnect.syncer import Syncer
from memium.source.document import Document
from memium.source.extractors.extractor_table import TableExtractor
from memium.source.prompt import QAWithDoc
from memium.utils.markdown import md_to_html

TABLE = """| Year | Event |
| - | - |
| 1900 | A |
| 1910 | B |
Rowwise // What happened in |Year|? // |Event|
"""


class FakeNoteStore:
    def __init__(self) -> None:
        self.updated: list[AnkiQAModel] = []
        self.created: list[AnkiQAModel] = []
        self.deleted: list[AnkiNoteID] = []

    def create(self, note: Sequence[AnkiQAModel]) -> Sequence[AnkiNoteID]:
        self.created.extend(note)
        return [AnkiNoteID(i) for i, _ in enumerate(note)]

    def update(self, note: AnkiQAModel) -> None:
        self.updated.append(note)

    def delete(self, note_ids: Sequence[AnkiNoteID]) -> None:
        self.deleted.extend(note_ids)


def _table_prompts(source_path: Path) -> Sequence[QAWithDoc]:
    return TableExtractor().extract_prompts(
        Document(content=TABLE, source_path=source_path, vault_name="Vault")
    )


def _in_anki(prompts: Sequence[QAWithDoc], converter: AnkiPromptConverter) -> Sequence[AnkiQAModel]:
    """The notes as they come back from Anki, i.e. with their fields rendered to HTML."""
    return [
        AnkiQAModel(
            Question=md_to_html(note.Question),
            Answer=md_to_html(note.Answer),
            Extra=md_to_html(note.Extra),
            raw_prompt=note.raw_prompt,
            tags=note.tags,
            root_deck=note.root_deck,
            destination_id=AnkiNoteID(i),
            card_ids=[AnkiCardID(i)],
        )
        for i, note in enumerate(converter.to_destination(prompt) for prompt in prompts)
    ]


def _sync(source_prompts: Sequence[QAWithDoc], destination: Sequence[AnkiQAModel]) -> FakeNoteStore:
    note_store = FakeNoteStore()
    Syncer(
        source_prompts=source_prompts,
        destination_prompts=destination,
        converter=AnkiPromptConverter(root_deck="FakeBaseDeck"),
        note_store=note_store,
    ).sync()
    return note_store


def test_unchanged_document_does_not_update():
    prompts = _table_prompts(Path("original.md"))
    destination = _in_anki(prompts, AnkiPromptConverter(root_deck="FakeBaseDeck"))

    note_store = _sync(prompts, destination)

    assert note_store.updated == []
    assert note_store.created == []
    assert note_store.deleted == []


def test_moving_a_table_to_another_document_updates_the_note():
    """Question and answer are unchanged, so scheduling is kept, but the Obsidian link and
    note title in the Extra field now point at the wrong document."""
    destination = _in_anki(
        _table_prompts(Path("original.md")), AnkiPromptConverter(root_deck="FakeBaseDeck")
    )
    moved = _table_prompts(Path("moved.md"))

    note_store = _sync(moved, destination)

    assert len(note_store.updated) == len(destination)
    assert all("moved" in note.Extra for note in note_store.updated)
    assert note_store.created == []
    assert note_store.deleted == []
