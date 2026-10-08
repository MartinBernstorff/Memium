import pytest

from memium.destination.ankiconnect.ankiconnect_requester import (
    ANKICONNECT_URL,
    AnkiRequester,
    anki_connect_is_live,
)
from memium.destination.ankiconnect.note_store import AnkiNoteStore
from memium.test_main import INTEGRATION_TEST_DECK


@pytest.fixture
def anki_requester() -> AnkiRequester:
    if not anki_connect_is_live():
        pytest.skip("Requires a running AnkiConnect server.")
    return AnkiRequester(ankiconnect_url=ANKICONNECT_URL, max_wait_seconds=10)


@pytest.fixture
def note_store(anki_requester: AnkiRequester) -> AnkiNoteStore:
    return AnkiNoteStore(anki_requester=anki_requester, root_deck=INTEGRATION_TEST_DECK)
