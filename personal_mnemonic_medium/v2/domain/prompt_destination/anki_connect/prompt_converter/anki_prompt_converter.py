from collections.abc import Sequence

from functionalpy._sequence import Seq

from personal_mnemonic_medium.v2.domain.prompt_destination.anki_connect.prompt_converter.prompts.anki_cloze import (
    AnkiCloze,
)
from personal_mnemonic_medium.v2.domain.prompt_destination.anki_connect.prompt_converter.prompts.anki_qa import (
    AnkiQA,
)
from personal_mnemonic_medium.v2.domain.prompt_destination.anki_connect.prompt_converter.prompts.base_anki_prompt import (
    AnkiCard,
)

from ....prompts.base_prompt import BasePrompt
from ....prompts.cloze_prompt import ClozePrompt
from ....prompts.qa_prompt import QAPrompt


class AnkiPromptConverter:
    def __init__(
        self,
        base_deck: str,
        card_css: str,
        deck_prefix: str = "#anki_deck",
    ) -> None:
        self.base_deck = base_deck
        self.deck_prefix = deck_prefix
        self.card_css = card_css

    def _prompt_to_card(self, prompt: BasePrompt) -> AnkiCard:
        deck_in_tags = [
            tag
            for tag in prompt.tags
            if tag.startswith(self.deck_prefix)
        ]
        deck = deck_in_tags[0] if deck_in_tags else self.base_deck

        match prompt:
            case QAPrompt():
                card = AnkiQA(
                    question=prompt.question,
                    answer=prompt.answer,
                    deck=deck,
                    tags=prompt.tags,
                    css=self.card_css,
                )
            case ClozePrompt():
                card = AnkiCloze(
                    text=prompt.text,
                    deck=deck,
                    tags=prompt.tags,
                    css=self.card_css,
                )
            case BasePrompt():
                raise ValueError(
                    "BasePrompt is the base class for all prompts, use a subclass"
                )

        return card

    def prompts_to_cards(
        self, prompts: Sequence[BasePrompt]
    ) -> Sequence[AnkiCard]:
        """Takes an iterable of prompts and turns them into AnkiCards"""

        return Seq(prompts).map(self._prompt_to_card).to_list()
