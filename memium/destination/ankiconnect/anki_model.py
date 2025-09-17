from collections.abc import Sequence
from dataclasses import dataclass
from typing import NewType

from memium.source.prompt import QAPrompt

Markdown = NewType("Markdown", str)


@dataclass(frozen=True)
class AnkiQAModel:
    # Field capitalisation must be preserved for backwards compatibility
    Question: Markdown
    Answer: Markdown
    Extra: Markdown

    raw_prompt: QAPrompt

    tags: Sequence[str]
    root_deck: str

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
