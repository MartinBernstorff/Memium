from memium.destination.ankiconnect.anki_model import AnkiQAModel, Markdown
from memium.destination.ankiconnect.ankiconnect_requester import ANKICONNECT_URL, AnkiRequester
from memium.destination.ankiconnect.note_store import AnkiNoteStore
from memium.test_main import INTEGRATION_TEST_DECK

note_store = AnkiNoteStore(
    anki_requester=AnkiRequester(ankiconnect_url=ANKICONNECT_URL, max_wait_seconds=10),
    root_deck=INTEGRATION_TEST_DECK,
)
note_store.clear()


def test_CRUD():
    note = AnkiQAModel.dummy(question="Random", answer="Data")
    note_id = note_store.create([note])[0]

    update = AnkiQAModel(
        Question=Markdown(note.Question + " UPDATED"),
        Answer=note.Answer,
        Extra=note.Extra,
        raw_prompt=note.raw_prompt,
        tags=["updated"],
        deck=INTEGRATION_TEST_DECK + "::Subdeck",
        destination_id=note_id,
        card_ids=None,
    )

    # Act
    note_store.update(update)

    # Assert
    updated = note_store.read(note_id)
    assert updated is not None
    assert updated.Question == update.Question
    assert updated.tags == update.tags
    assert updated.deck == update.deck
