"""This class takes a bunch of prompts, packages them, then syncs them to Anki.

Can take an arbitrary amount of post-processing steps to be applied.
"""

import hashlib
from pathlib import Path
from shutil import copyfile
from typing import List, Sequence, Union

import genanki

from personal_mnemonic_medium.exporters.anki.anki_card import AnkiCard
from personal_mnemonic_medium.prompt_extractors.cloze_extractor import ClozePrompt
from personal_mnemonic_medium.prompt_extractors.qa_extractor import QAPrompt


def simple_hash(text: str) -> int:
    """MD5 of text, mod 2^63. Probably not a great hash function."""
    comp_hash = int(hashlib.sha256(text.encode("utf-8")).hexdigest(), 16) % 10**10

    return comp_hash


class DeckCollection(dict):
    """Defaultdict for decks, but with stored name."""

    def __getitem__(self, deckname):
        if deckname not in self:
            deck_id = simple_hash(deckname)
            self[deckname] = genanki.Deck(deck_id, deckname)
        return super().__getitem__(deckname)


class PackageGenerator:
    """Generates an anki package from a list of anki cards"""

    def __init__(self) -> None:
        pass

    @staticmethod
    def cards_to_package(cards: List[AnkiCard], output_path: Path) -> Path:
        """Take an iterable prompts, output an .apkg in a file called output_name.
        NOTE: We _must_ be in a temp directory.
        """
        decks = DeckCollection()

        media = set()

        for card in cards:
            card.finalize()
            for abspath, newpath in card.determine_media_references():
                copyfile(
                    abspath, newpath
                )  # This is inefficient but definitely works on all platforms.
                media.add(newpath)
            decks[card.deckname()].add_note(card.to_genanki_note())

        if len(decks) == 0:
            raise ValueError("No decks were generated.")

        package = genanki.Package(deck_or_decks=decks.values(), media_files=list(media))

        package.write_to_file(output_path)

        return Path(output_path)

    def prompts_to_cards(
        self, prompts: Sequence[Union[QAPrompt, ClozePrompt]]
    ) -> List[AnkiCard]:
        """Takes an iterable of prompts and turns them into AnkiCards"""

        cards = []

        for prompt in prompts:
            if isinstance(prompt, QAPrompt):
                card = AnkiCard(
                    fields=[prompt.question, prompt.answer],
                    tags=prompt.tags,
                    model_type="QA",
                    source_markdown=prompt.source_note.content,
                    note_uuid=prompt.note_uuid,
                )
            elif isinstance(prompt, ClozePrompt):
                card = AnkiCard(
                    fields=[prompt.content],
                    tags=prompt.tags,
                    model_type="Cloze",
                    source_markdown=prompt.source_note.content,
                    note_uuid=prompt.note_uuid,
                )

            cards += [card]

        return cards