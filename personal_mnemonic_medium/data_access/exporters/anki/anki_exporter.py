"""This class takes a bunch of prompts, packages them, then syncs them to Anki.

Can take an arbitrary amount of post-processing steps to be applied.
"""

import logging
import traceback
from collections import defaultdict
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from wasabi import Printer

from personal_mnemonic_medium.data_access.exporters.anki.card_types.base import (
    AnkiCard,
)
from personal_mnemonic_medium.data_access.exporters.anki.package_generator import (
    AnkiPackageGenerator,
    DeckBundle,
)
from personal_mnemonic_medium.data_access.exporters.anki.sync.anki_gateway import (
    get_anki_server_guid2noteinfo,
)
from personal_mnemonic_medium.data_access.exporters.base import (
    PromptExporter,
)
from personal_mnemonic_medium.domain.prompt_extractors.prompt import (
    Prompt,
)

from .sync.gateway_utils import AnkiConnectParams, invoke

log = logging.getLogger(__name__)
# Log to disk, not to console.
logging.basicConfig(
    filename="anki_package_generator.log",
    filemode="w",
    level=logging.DEBUG,
)
msg = Printer(timestamp=True)


@dataclass(frozen=True)
class NoteDiff:
    deck_bundle: DeckBundle
    deckbundle_guids: set[str]
    anki_guids: set[str]

    @property
    def symmetric_diff(self) -> set[str]:
        return self.deckbundle_guids.symmetric_difference(
            self.anki_guids
        )

    @property
    def guids_only_in_anki(self) -> set[str]:
        return self.anki_guids - self.deckbundle_guids


# TODO: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues/272 refactor: create pydantic class for noteinfo
class AnkiExporter(PromptExporter):
    """Generates an anki package from a list of anki cards"""

    def __init__(self, anki_connect: AnkiConnectParams) -> None:
        self.anki_connect = anki_connect

    def get_anki_database_note_infos(
        self, deck_bundle: DeckBundle
    ) -> dict[str, Any]:
        return get_anki_server_guid2noteinfo(deck_bundle)

    def get_note_diff(self, deck_bundle: DeckBundle) -> NoteDiff:
        anki_note_info_by_guid = self.get_anki_database_note_infos(
            deck_bundle
        )
        anki_note_guids: set[str] = set(anki_note_info_by_guid.keys())

        return NoteDiff(
            deckbundle_guids=deck_bundle.note_guids,
            anki_guids=anki_note_guids,
            deck_bundle=deck_bundle,
        )

    def add_to_anki(self, deck_bundle: DeckBundle) -> None:
        package_path = deck_bundle.save_to_apkg(
            output_path=Path("anki_package.apkg")
        )
        try:
            sync_path = str(self.anki_connect.apkg_dir / "deck.apkg")
            invoke("importPackage", path=sync_path)
            print(f"Imported {deck_bundle.deck.name}!")  # type: ignore
        except Exception:
            print(f"Unable to sync {package_path} to anki")
            traceback.print_exc()

    def delete_diff(self, note_diff: NoteDiff):
        try:
            guids_to_delete = note_diff.guids_only_in_anki

            if guids_to_delete:
                guid2noteinfo = get_anki_server_guid2noteinfo(
                    deck_bundle=note_diff.deck_bundle
                )

                note_ids = [  # type: ignore
                    guid2noteinfo[guid]["noteId"]  # type: ignore
                    for guid in guids_to_delete
                ]

                invoke("deleteNotes", notes=note_ids)
                msg.good(f"Deleted {len(guids_to_delete)} notes")

        except Exception:
            msg.fail(
                f"Unable to delete cards in {note_diff.deck_bundle.deck.name}"  # type: ignore
            )
            # Print full stack trace
            traceback.print_exc()

    def sync_prompts(self, prompts: Sequence[Prompt]):
        bundles = AnkiPackageGenerator().prompts_to_deck_bundles(
            prompts
        )
        for bundle in bundles:
            note_diff = self.get_note_diff(deck_bundle=bundle)
            if len(note_diff.symmetric_diff) > 0:
                self.add_to_anki(deck_bundle=bundle)

                if self.anki_connect.delete_cards:
                    self.delete_diff(note_diff=note_diff)


def group_cards_by_deck(
    cards: Sequence[AnkiCard]
) -> dict[str, list[AnkiCard]]:
    decks: dict[str, list[AnkiCard]] = defaultdict(list)

    for card in cards:
        decks[card.deckname] += [card]

    return decks
