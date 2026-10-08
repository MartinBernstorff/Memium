from memium.destination.ankiconnect.anki_model import AnkiQAModel
from memium.destination.ankiconnect.ankiconnect_requester import AnkiRequester
from memium.destination.ankiconnect.card_store import AnkiCardStore
from memium.destination.ankiconnect.note_store import AnkiNoteStore
from memium.test_main import INTEGRATION_TEST_DECK


def test_CRUD(anki_requester: AnkiRequester, note_store: AnkiNoteStore):
    card_store = AnkiCardStore(anki_requester=anki_requester, root_deck="Main")
    note_store.clear()
    new_note = AnkiQAModel.dummy(question="Random", answer="Data", root_deck=INTEGRATION_TEST_DECK)
    note_id = note_store.create([new_note])[0]
    note = note_store.read([note_id])

    cards = card_store.read(note[0].card_ids[0])
    assert cards is not None
