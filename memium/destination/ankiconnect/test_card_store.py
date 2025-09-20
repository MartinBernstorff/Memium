from memium.destination.ankiconnect.anki_model import AnkiQAModel
from memium.destination.ankiconnect.ankiconnect_requester import ANKICONNECT_URL, AnkiRequester
from memium.destination.ankiconnect.card_store import AnkiCardStore
from memium.destination.ankiconnect.test_note_store import note_store

cardStore = AnkiCardStore(
    anki_requester=AnkiRequester(ankiconnect_url=ANKICONNECT_URL, max_wait_seconds=10),
    root_deck="Main",
)


def test_CRUD():
    new_note = AnkiQAModel.dummy(question="Random", answer="Data")
    note_id = note_store.create([new_note])[0]
    note = note_store.read(note_id)
    if note is None:
        raise ValueError("Note not found after creation")

    cards = cardStore.read(note.card_ids[0])
    assert cards is not None
