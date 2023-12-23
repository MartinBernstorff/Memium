from collections.abc import Sequence

from functionalpy._sequence import Seq

from ...source.prompts.prompt import BasePrompt
from ...source.prompts.prompt_cloze import ClozePrompt
from ...source.prompts.prompt_qa import QAPrompt
from .anki_card import AnkiCard
from .anki_prompt_cloze import AnkiCloze
from .anki_prompt_qa import AnkiQA


class AnkiPromptConverter:
    def __init__(
        self, base_deck: str, card_css: str, deck_prefix: str = "#anki_deck"
    ) -> None:
        self.base_deck = base_deck
        self.deck_prefix = deck_prefix
        self.card_css = card_css

    def _prompt_to_card(self, prompt: BasePrompt) -> AnkiCard:
        deck_in_tags = [
            tag for tag in prompt.tags if tag.startswith(self.deck_prefix)
        ]
        deck = deck_in_tags[0] if deck_in_tags else self.base_deck

        match prompt:
            case QAPrompt():
                return AnkiQA(
                    question=prompt.question,
                    answer=prompt.answer,
                    base_deck=deck,
                    tags=prompt.tags,
                    css=self.card_css,
                )
            case ClozePrompt():
                return AnkiCloze(
                    text=prompt.text,
                    base_deck=deck,
                    tags=prompt.tags,
                    css=self.card_css,
                )
            case BasePrompt():
                raise ValueError(
                    "BasePrompt is the base class for all prompts, use a subclass"
                )

    def prompts_to_cards(
        self, prompts: Sequence[BasePrompt]
    ) -> Sequence[AnkiCard]:
        """Takes an iterable of prompts and turns them into AnkiCards"""

        return Seq(prompts).map(self._prompt_to_card).to_list()
