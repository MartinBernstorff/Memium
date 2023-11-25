from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path

from wasabi import Printer

from personal_mnemonic_medium.data_access.exporters.anki.anki_exporter import (
    AnkiExporter,
)
from personal_mnemonic_medium.data_access.exporters.anki.card_types.base import (
    AnkiCard,
)

msg = Printer(timestamp=True)


@dataclass(frozen=True)
class SkippedDeck:
    deck_name: str


# TODO: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues/266 https://github.com/MartinBernstorff/personal-mnemonic-medium/issues/265 Move deck skipping to ingester
def cards_to_apkg(
    cards: Sequence[AnkiCard],
    output_dir: Path,
    skip_decks: Sequence[str] = (),
) -> Path | SkippedDeck:
    deck_bundle = AnkiExporter().cards_to_deck_bundle(cards=cards)

    if any(d in deck_bundle.deck_name for d in skip_decks):
        msg.fail(
            f"Skipping {deck_bundle.deck_name} because it is marked for skipping"
        )
        return SkippedDeck(deck_name=deck_bundle.deck_name)

    return deck_bundle.save_deck_to_file(
        output_path=output_dir / "deck.apkg"
    )
