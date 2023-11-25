from dataclasses import dataclass
from typing import ClassVar

from personal_mnemonic_medium.data_access.exporters.anki.exporter import (
    NoteDiff,
)
from personal_mnemonic_medium.data_access.exporters.anki.sync.bundle_generator import (
    DeckBundle,
)


@dataclass(frozen=True)
class MockDeckBundle(DeckBundle):
    deck: None = None  # type: ignore
    media: ClassVar[set[str]] = {"1", "2", "3"}  # type: ignore


def test_notediff():
    diff = NoteDiff(
        deckbundle_guids={"1", "2", "3"},
        anki_guids={"2", "3", "4"},
        deck_bundle=MockDeckBundle(),
    )

    assert diff.symmetric_diff == {"1", "4"}
    assert diff.guids_only_in_anki == {"4"}
