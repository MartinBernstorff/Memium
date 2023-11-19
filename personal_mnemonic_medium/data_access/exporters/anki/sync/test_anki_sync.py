import uuid
from dataclasses import dataclass

import genanki

from personal_mnemonic_medium.data_access.exporters.anki.card_types.base import (
    AnkiCard,
)
from personal_mnemonic_medium.data_access.exporters.anki.sync.anki_sync import (
    _cards_to_decks,  # type: ignore
)


@dataclass
class MockAnkiCard(AnkiCard):
    deckname: str = "Default::Subdeck"  # type: ignore

    @property
    def genanki_model(self) -> genanki.Model:
        ...

    @property
    def card_uuid(self) -> int:
        return int(uuid.uuid4())


def test_cards_to_decks():
    cards = (
        MockAnkiCard(deckname="Default::Subdeck1"),
        MockAnkiCard(deckname="Default::Subdeck2"),
        MockAnkiCard(deckname="Default::Subdeck2"),
    )

    decks = _cards_to_decks(cards)

    assert decks == {
        "Default::Subdeck1": [cards[0]],
        "Default::Subdeck2": [cards[1], cards[2]],
    }
