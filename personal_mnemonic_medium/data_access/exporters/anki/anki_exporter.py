"""This class takes a bunch of prompts, packages them, then syncs them to Anki.

Can take an arbitrary amount of post-processing steps to be applied.
"""

import logging
import traceback
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from shutil import copyfile
from typing import Any

import genanki
from wasabi import Printer

from personal_mnemonic_medium.data_access.exporters.anki.card_types.base import (
    AnkiCard,
)
from personal_mnemonic_medium.data_access.exporters.anki.card_types.cloze import (
    AnkiCloze,
)
from personal_mnemonic_medium.data_access.exporters.anki.card_types.qa import (
    AnkiQA,
)
from personal_mnemonic_medium.data_access.exporters.anki.sync.anki_sync import (
    get_anki_server_guid2noteinfo,
)
from personal_mnemonic_medium.data_access.exporters.anki.sync.gateway.ankiconnect_utils import (
    AnkiConnectParams,
    invoke,
)
from personal_mnemonic_medium.data_access.exporters.base import (
    PromptExporter,
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

log = logging.getLogger(__name__)
# Log to disk, not to console.
logging.basicConfig(
    filename="anki_package_generator.log",
    filemode="w",
    level=logging.DEBUG,
)
msg = Printer(timestamp=True)


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
        # Tests return a local, so explicitly turning into path here


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


class AnkiPackageGenerator(PromptExporter):
    """Generates an anki package from a list of anki cards"""

    def __init__(self, anki_connect: AnkiConnectParams) -> None:
        self.anki_connect = anki_connect

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
        package_path = deck_bundle.save_deck_to_file(
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
        cards = self.prompts_to_cards(prompts=prompts)
        deck_bundle = self.cards_to_deck_bundle(cards=cards)
        note_diff = self.get_note_diff(deck_bundle=deck_bundle)

        if len(note_diff.symmetric_diff) > 0:
            self.add_to_anki(deck_bundle=deck_bundle)

            if self.anki_connect.delete_cards:
                self.delete_diff(note_diff=note_diff)
