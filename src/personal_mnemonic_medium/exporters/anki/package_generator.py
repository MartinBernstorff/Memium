"""This class takes a bunch of prompts, packages them, then syncs them to Anki.

Can take an arbitrary amount of post-processing steps to be applied.
"""

import logging
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from shutil import copyfile

import genanki

from personal_mnemonic_medium.exporters.anki.card_types.base import (
    AnkiCard,
)
from personal_mnemonic_medium.exporters.anki.card_types.cloze import (
    AnkiCloze,
)
from personal_mnemonic_medium.exporters.anki.card_types.qa import (
    AnkiQA,
)
from personal_mnemonic_medium.exporters.base import CardExporter
from personal_mnemonic_medium.prompt_extractors.cloze_extractor import (
    ClozePrompt,
)
from personal_mnemonic_medium.prompt_extractors.prompt import Prompt
from personal_mnemonic_medium.prompt_extractors.qa_extractor import (
    QAPrompt,
)
from personal_mnemonic_medium.utils.hasher import simple_hash

log = logging.getLogger(__name__)
# Log to disk, not to console.
logging.basicConfig(
    filename="anki_package_generator.log",
    filemode="w",
    level=logging.DEBUG,
)


@dataclass(frozen=True)
class DeckBundle:
    deck: genanki.Deck
    media: set[str]

    def get_package(self) -> genanki.Package:
        return genanki.Package(
            deck_or_decks=self.deck, media_files=list(self.media)
        )

    def save_deck_to_file(self, output_path: Path) -> Path:
        package = self.get_package()
        package.write_to_file(output_path)
        return output_path


class AnkiPackageGenerator(CardExporter):
    """Generates an anki package from a list of anki cards"""

    def __init__(self) -> None:
        pass

    @staticmethod
    def cards_to_deck_bundle(cards: list[AnkiCard]) -> DeckBundle:
        """Take an iterable prompts, output an .apkg in a file called output_name.
        NOTE: We _must_ be in a temp directory.
        """
        deck, media = AnkiPackageGenerator.cards_to_deck(cards=cards)

        return DeckBundle(deck=deck, media=media)

    @staticmethod
    def cards_to_deck(
        cards: Sequence[AnkiCard]
    ) -> tuple[genanki.Deck, set[str]]:
        media = set()  # type: ignore

        deck_name = cards[0].deckname
        deck_id = simple_hash(deck_name)
        deck = genanki.Deck(deck_id=deck_id, name=deck_name)

        for card in cards:
            for abspath, newpath in card.determine_media_references():
                try:
                    copyfile(
                        abspath, newpath
                    )  # This is inefficient but definitely works on all platforms.
                    media.add(newpath)  # type: ignore
                except FileNotFoundError as e:
                    log.debug(
                        f"Could not find file {abspath} for media, {e}."
                    )

            try:
                deck.add_note(card.to_genanki_note())
            except IndexError as e:
                log.debug(
                    f"Could not add card {card} to deck {deck_name}, {e}."
                )

        return deck, media  # type: ignore

    def prompts_to_cards(
        self, prompts: Sequence[Prompt]
    ) -> list[AnkiCard]:
        """Takes an iterable of prompts and turns them into AnkiCards"""

        cards: list[AnkiCard] = []

        for prompt in prompts:
            if isinstance(prompt, QAPrompt):
                card = AnkiQA(
                    fields=[prompt.question, prompt.answer],
                    source_prompt=prompt,
                )
            elif isinstance(prompt, ClozePrompt):
                card = AnkiCloze(
                    fields=[prompt.content], source_prompt=prompt
                )
            else:
                raise NotImplementedError(
                    f"Prompt type {type(prompt)} not supported."
                )

            cards += [card]

        return cards
