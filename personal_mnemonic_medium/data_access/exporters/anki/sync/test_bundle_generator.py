from dataclasses import dataclass
from pathlib import Path

import genanki

from personal_mnemonic_medium.data_access.document_ingesters.document import (
    Document,
)
from personal_mnemonic_medium.data_access.exporters.anki.card_types.base import (
    AnkiCard,
)
from personal_mnemonic_medium.data_access.exporters.anki.sync.bundle_generator import (
    AnkiPackageGenerator,
    group_cards_by_deck,  # type: ignore
)
from personal_mnemonic_medium.domain.prompt_extractors.qa_extractor import (
    QAPrompt,
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


def test_card_grouper():
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


def MockDocument() -> Document:
    return Document(
        content="Content",
        uuid="uuid",
        source_path=Path("source_path"),
    )


def MockQAPrompt() -> QAPrompt:
    return QAPrompt(
        question="prompt", answer="answer", source_doc=MockDocument()
    )


def test_prompts_to_bundles():
    cards = [MockQAPrompt()]
    bundles = AnkiPackageGenerator.prompts_to_bundles(cards)

    assert len(bundles) == 1
