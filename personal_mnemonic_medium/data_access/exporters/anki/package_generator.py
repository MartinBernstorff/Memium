from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from shutil import copyfile

import genanki

from personal_mnemonic_medium.data_access.exporters.anki.card_types.base import (
    AnkiCard,
)
from personal_mnemonic_medium.data_access.exporters.anki.card_types.cloze import (
    AnkiCloze,
)
from personal_mnemonic_medium.data_access.exporters.anki.card_types.qa import (
    AnkiQA,
)
from personal_mnemonic_medium.domain.prompt_extractors.cloze_extractor import (
    ClozePrompt,
)
from personal_mnemonic_medium.domain.prompt_extractors.prompt import (
    Prompt,
)
from personal_mnemonic_medium.domain.prompt_extractors.qa_extractor import (
    QAPrompt,
)
from personal_mnemonic_medium.utils.hasher import simple_hash


@dataclass(frozen=True)
class DeckBundle:
    deck: genanki.Deck
    media: set[str]

    @property
    def deck_name(self) -> str:
        return self.deck.name  # type: ignore

    def get_package(self) -> genanki.Package:
        return genanki.Package(
            deck_or_decks=self.deck, media_files=list(self.media)
        )

    @property
    def note_guids(self) -> set[str]:
        md_notes: list[genanki.Note] = self.deck.notes  # type: ignore
        md_note_guids = {str(n.guid) for n in md_notes}  # type: ignore
        return md_note_guids

    def save_deck_to_file(self, output_path: Path) -> Path:
        package = self.get_package()
        package.write_to_file(output_path)  # type: ignore
        return Path(output_path)


class AnkiPackageGenerator:
    @staticmethod
    def cards_to_deck_bundle(cards: Sequence[AnkiCard]) -> DeckBundle:
        media: set[str] = set()  # type: ignore

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
                deck.add_note(card.to_genanki_note())  # type: ignore
            except IndexError as e:
                log.debug(
                    f"Could not add card {card} to deck {deck_name}, {e}."
                )

        return DeckBundle(deck=deck, media=media)

    def prompts_to_cards(
        self, prompts: Sequence[Prompt]
    ) -> Sequence[AnkiCard]:
        """Takes an iterable of prompts and turns them into AnkiCards"""

        cards: list[AnkiCard] = []

        for prompt in prompts:
            match prompt:
                case QAPrompt():
                    card = AnkiQA(
                        fields=[prompt.question, prompt.answer],
                        source_prompt=prompt,
                    )
                case ClozePrompt():
                    card = AnkiCloze(
                        fields=[prompt.content], source_prompt=prompt
                    )
                # TODO: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues/271 feat: ensure all prompt types are covered in anki_exporter
                case _:
                    raise NotImplementedError(
                        f"Prompt type {type(prompt)} not supported."
                    )

            cards += [card]

        return cards
