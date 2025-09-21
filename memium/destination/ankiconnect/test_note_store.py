from memium.destination.ankiconnect.anki_model import AnkiQAModel, Markdown
from memium.destination.ankiconnect.ankiconnect_requester import ANKICONNECT_URL, AnkiRequester
from memium.destination.ankiconnect.note_store import AnkiNoteStore
from memium.test_main import INTEGRATION_TEST_DECK
from memium.utils.markdown import md_to_html

note_store = AnkiNoteStore(
    anki_requester=AnkiRequester(ankiconnect_url=ANKICONNECT_URL, max_wait_seconds=10),
    root_deck=INTEGRATION_TEST_DECK,
)
note_store.clear()


def test_CRUD():
    note = AnkiQAModel.dummy(question="What is life?", answer="But a butterfly?")

    # Create
    note_id = note_store.create([note])[0]

    # Read
    read = note_store.read([note_id])[0]
    assert read is not None

    # Update
    update = AnkiQAModel(
        Question=Markdown(note.Question + " UPDATED"),
        Answer=note.Answer,
        Extra=note.Extra,
        raw_prompt=note.raw_prompt,
        tags=["updated"],
        root_deck=INTEGRATION_TEST_DECK,
        destination_id=note_id,
        card_ids=[],
    )
    note_store.update(update)

    # Assert
    updated = note_store.read([note_id])[0]
    assert updated.deck == update.deck
    assert updated is not None
    assert updated.Question == md_to_html(update.Question)
    assert updated.tags == update.tags

    # Delete
    note_store.delete([note_id])

    # Assert gone
    deleted = note_store.read([note_id])
    assert len(deleted) == 0


def test_read_all():
    notes = AnkiNoteStore(
        anki_requester=AnkiRequester(ankiconnect_url=ANKICONNECT_URL, max_wait_seconds=10),
        root_deck="Memium",
    ).get_all_sans_decks()
    assert len(notes) > 0
