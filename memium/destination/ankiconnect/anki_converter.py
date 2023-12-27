from collections.abc import Sequence
from dataclasses import dataclass

from functionalpy._sequence import Seq

from ...post_processing.obsidian import ExtraGenerator
from ...source.prompts.prompt import BasePrompt
from ...source.prompts.prompt_cloze import ClozePrompt
from ...source.prompts.prompt_qa import QAPrompt
from .anki_prompt import AnkiPrompt
from .anki_prompt_cloze import AnkiCloze
from .anki_prompt_qa import AnkiQA


@dataclass(frozen=True)
class AnkiPromptConverter:
    base_deck: str
    deck_prefix: str
    card_css: str
    extra_generators: Sequence[ExtraGenerator]

    def _prompt_to_card(self, prompt: BasePrompt) -> AnkiPrompt:
        deck_in_tags = [
            tag for tag in prompt.tags if tag.startswith(self.deck_prefix)
        ]
        deck = deck_in_tags[0] if deck_in_tags else self.base_deck
        extra = "".join(gen(prompt) for gen in self.extra_generators)

        match prompt:
            case QAPrompt():
                return AnkiQA(
                    question=prompt.question,
                    answer=prompt.answer,
                    base_deck=deck,
                    tags=prompt.tags,
                    css=self.card_css,
                    extra=extra,
                )
            case ClozePrompt():
                return AnkiCloze(
                    text=prompt.text,
                    base_deck=deck,
                    tags=prompt.tags,
                    css=self.card_css,
                    extra=extra,
                )
            case BasePrompt():
                raise ValueError(
                    "BasePrompt is the base class for all prompts, use a subclass"
                )

    def prompts_to_cards(
        self, prompts: Sequence[BasePrompt]
    ) -> Sequence[AnkiPrompt]:
        """Takes an iterable of prompts and turns them into AnkiCards"""

        return Seq(prompts).map(self._prompt_to_card).to_list()
