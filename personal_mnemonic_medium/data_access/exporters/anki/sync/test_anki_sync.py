from dataclasses import dataclass

import genanki

from personal_mnemonic_medium.data_access.exporters.anki.anki_exporter import (
    group_cards_by_deck,  # type: ignore
)
from personal_mnemonic_medium.data_access.exporters.anki.card_types.base import (
    AnkiCard,
)


@dataclass
class MockAnkiCard(AnkiCard):
    deckname: str = "Default::Subdeck"  # type: ignore

    @property
    def genanki_model(self) -> genanki.Model:
        ...

    @property
    def card_uuid(self) -> int:
        ...


def test_cards_to_decks():
    cards = (
        MockAnkiCard(deckname="Default::Subdeck1"),
        MockAnkiCard(deckname="Default::Subdeck2"),
        MockAnkiCard(deckname="Default::Subdeck2"),
    )

    decks = group_cards_by_deck(cards)

    assert decks == {
        "Default::Subdeck1": [cards[0]],
        "Default::Subdeck2": [cards[1], cards[2]],
    }
