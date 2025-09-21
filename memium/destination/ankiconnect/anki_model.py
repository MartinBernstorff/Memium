from collections.abc import Sequence
from typing import NewType

from pydantic import BaseModel

from memium.source.prompt import QAPrompt

Markdown = NewType("Markdown", str)
AnkiNoteID = NewType("AnkiNoteID", int)
AnkiCardID = NewType("AnkiCardID", int)
SyncIdentity = NewType("SyncIdentity", str)


class AnkiQAModel(BaseModel):
    # Field capitalisation must be preserved for backwards compatibility
    Question: Markdown
    Answer: Markdown
    Extra: Markdown

    raw_prompt: QAPrompt

    tags: Sequence[str]
    root_deck: str  # E.g. "BaseDeck" or "BaseDeck::Subdeck". Used with tags in the deck property to form the full deck name

    destination_id: AnkiNoteID | None
    card_ids: Sequence[AnkiCardID]

    @staticmethod
    def from_primitives(
        question: str,
        answer: str,
        extra: str,
        raw_question: str,
        raw_answer: str,
        tags: Sequence[str],
        root_deck: str,
        destination_id: AnkiNoteID | None,
        card_ids: Sequence[AnkiCardID],
    ) -> "AnkiQAModel":
        return AnkiQAModel(
            Question=Markdown(question),
            Answer=Markdown(answer),
            Extra=Markdown(extra),
            raw_prompt=QAPrompt(question=raw_question, answer=raw_answer),
            tags=tags,
            root_deck=root_deck,
            destination_id=destination_id,
            card_ids=card_ids,
        )

    @staticmethod
    def dummy(
        question: str = "Q. DummyQuestion?",
        answer: str = "A. DummyAnswer",
        extra: str = "",
        tags: Sequence[str] = (),
    ) -> "AnkiQAModel":
        return AnkiQAModel(
            Question=Markdown(question),
            Answer=Markdown(answer),
            Extra=Markdown(extra),
            tags=tags,
            raw_prompt=QAPrompt.dummy(question, answer),
            root_deck="FakeBaseDeck",
            destination_id=None,
            card_ids=[],
        )

    @property
    def formatted_field_names(self) -> list[str]:
        return [name for name, type_hint in self.__annotations__.items() if type_hint == Markdown]

    @property
    def deck(self) -> str:
        deck_prefix = "anki/deck/"
        deck_in_tags = (
            tag.replace(deck_prefix, "").replace("/", "::")
            for tag in self.tags
            if tag.startswith(deck_prefix)
        )
        subdeck = next(deck_in_tags, None)

        base_anki_deck = self.root_deck if subdeck is None else f"{self.root_deck}::{subdeck}"

        return base_anki_deck

    def sync_identity(self) -> SyncIdentity:
        lowered_tags = [tag.lower() for tag in self.tags]
        return SyncIdentity(f"{self.raw_prompt.scheduling_uid_str}::{sorted(lowered_tags)}")
