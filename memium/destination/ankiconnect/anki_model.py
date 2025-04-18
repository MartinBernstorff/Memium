from collections.abc import Sequence
from dataclasses import dataclass
from typing import NewType

from memium.source.prompts.prompt_qa import QAPromptImpl
from memium.utils.extract_terms import get_terms_surrounded_by_underscores

Markdown = NewType("Markdown", str)


@dataclass(frozen=True)
class AnkiQAModel:
    # Field capitalisation must be preserved for backwards compatibility
    Question: Markdown
    Answer: Markdown
    Extra: Markdown
    UUID: Markdown

    raw_prompt: QAPromptImpl

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
            UUID=Markdown(""),
            tags=tags,
            raw_prompt=QAPromptImpl.dummy(question, answer),
            root_deck="FakeBaseDeck",
        )

    @property
    def uuid(self) -> str:
        return str(self.UUID).replace("<p>", "").replace("</p>", "")

    @property
    def field_names(self) -> list[str]:
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

        wiki_links = get_terms_surrounded_by_underscores(self.Question)
        wiki_subdeck = "-".join(sorted(wiki_links))

        if wiki_subdeck != "":
            return f"{base_anki_deck}::{wiki_subdeck}"
        return base_anki_deck
