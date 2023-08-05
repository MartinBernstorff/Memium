"""This class takes a bunch of prompts, packages them, then syncs them to Anki.

Can take an arbitrary amount of post-processing steps to be applied.
"""

import hashlib
import logging
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from shutil import copyfile
from typing import Any, List, Set, Union

import genanki

from personal_mnemonic_medium.exporters.anki.anki_card import AnkiCard
from personal_mnemonic_medium.prompt_extractors.cloze_extractor import ClozePrompt
from personal_mnemonic_medium.prompt_extractors.qa_extractor import QAPrompt

log = logging.getLogger(__name__)
# Log to disk, not to console.
logging.basicConfig(
    filename="anki_package_generator.log",
    filemode="w",
    level=logging.DEBUG,
)


def simple_hash(text: str) -> int:
    """MD5 of text, mod 2^63. Probably not a great hash function."""
    comp_hash = int(hashlib.sha256(text.encode("utf-8")).hexdigest(), 16) % 10**10

    return comp_hash


class DeckCollection(dict):
    """Defaultdict for decks, but with stored name."""

    def __getitem__(self, deckname: str) -> Any:
        if deckname not in self:
            deck_id = simple_hash(deckname)
            self[deckname] = genanki.Deck(deck_id, deckname)
        return super().__getitem__(deckname)


@dataclass(frozen=True)
class DeckBundle:
    deck: genanki.Deck
    media: Set[str]

    def get_package(self) -> genanki.Package:
        return genanki.Package(deck_or_decks=self.deck, media_files=list(self.media))

    def save_deck_to_file(self, output_path: Path) -> Path:
        package = self.get_package()
        package.write_to_file(output_path)
        return output_path


class PackageGenerator:
    """Generates an anki package from a list of anki cards"""

    def __init__(self) -> None:
        pass

    @staticmethod
    def cards_to_deck_bundle(cards: List[AnkiCard]) -> DeckBundle:
        """Take an iterable prompts, output an .apkg in a file called output_name.
        NOTE: We _must_ be in a temp directory.
        """
        deck, media = PackageGenerator.cards_to_deck(cards=cards)

        return DeckBundle(
            deck=deck,
            media=media,
        )

    @staticmethod
    def cards_to_deck(
        cards: Sequence[AnkiCard],
    ) -> tuple[genanki.Deck, Set[str]]:
        media = set()

        deck_name = cards[0].deckname
        deck_id = simple_hash(deck_name)
        deck = genanki.Deck(deck_id=deck_id, name=deck_name)

        for card in cards:
            for abspath, newpath in card.determine_media_references():
                try:
                    copyfile(
                        abspath,
                        newpath,
                    )  # This is inefficient but definitely works on all platforms.
                    media.add(newpath)
                except FileNotFoundError as e:
                    log.debug(f"Could not find file {abspath} for media, {e}.")

            deck.add_note(card.to_genanki_note())

        return deck, media

    def prompts_to_cards(
        self,
        prompts: Sequence[Union[QAPrompt, ClozePrompt]],
    ) -> List[AnkiCard]:
        """Takes an iterable of prompts and turns them into AnkiCards"""

        cards = []

        for prompt in prompts:
            if isinstance(prompt, QAPrompt):
                card = AnkiCard(
                    fields=[
                        prompt.question,
                        prompt.answer,
                    ],
                    tags=prompt.tags,
                    model_type="QA",
                    source_markdown=prompt.source_note.content,
                    source_note=prompt.source_note,
                    source_prompt=prompt,
                )
            elif isinstance(prompt, ClozePrompt):
                card = AnkiCard(
                    fields=[prompt.content],
                    tags=prompt.tags,
                    model_type="Cloze",
                    source_markdown=prompt.source_note.content,
                    source_note=prompt.source_note,
                    source_prompt=prompt,
                )

            cards += [card]  # type: ignore

        return cards
