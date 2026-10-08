from memium.destination.ankiconnect.anki_model import AnkiQAModel
from memium.destination.ankiconnect.note_store import AnkiNoteStore
from memium.test_main import INTEGRATION_TEST_DECK
from memium.utils.markdown import Markdown, md_to_html


def test_CRUD(note_store: AnkiNoteStore):
    note_store.clear()
    note = AnkiQAModel.dummy(
        question="What is life?",
        answer="But a butterfly?",
        tags=["anki/deck/Subdeck/Subdeck2"],
        root_deck=INTEGRATION_TEST_DECK,
    )

    # Create
    note_id = note_store.create([note])[0]

    # Read
    read = note_store.read([note_id])[0]
    assert read.destination_id == note_id

    # Read all
    all_ids = note_store.get_all_ids()
    assert note_id in all_ids
    assert read.destination_id in all_ids

    # Update
    update = AnkiQAModel(
        Question=Markdown(note.Question + " UPDATED"),
        Answer=note.Answer,
        Extra=note.Extra,
        raw_prompt=note.raw_prompt,
        tags=["updated", "anki/deck/Subdeck/Subdeck2"],
        root_deck=INTEGRATION_TEST_DECK,
        destination_id=note_id,
        card_ids=[],
    )
    assert update.deck == INTEGRATION_TEST_DECK + "::Subdeck::Subdeck2"
    note_store.update(update)

    # Assert
    updated = note_store.read([note_id])[0]
    assert updated.deck == update.deck
    assert updated is not None
    assert updated.Question == md_to_html(update.Question)
    assert set(updated.tags) == set(update.tags)

    # Delete
    note_store.delete([note_id])

    # Assert gone
    deleted = note_store.read([note_id])
    assert len(deleted) == 0


def test_read_all(note_store: AnkiNoteStore):
    note_store.clear()
    note_id = note_store.create(
        [AnkiQAModel.dummy(question="Q", answer="A", root_deck=INTEGRATION_TEST_DECK)]
    )[0]

    notes = note_store.get_all_sans_decks()
    assert [n.destination_id for n in notes] == [note_id]
