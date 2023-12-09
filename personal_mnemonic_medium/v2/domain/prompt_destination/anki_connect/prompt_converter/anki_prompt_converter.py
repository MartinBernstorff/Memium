from collections.abc import Sequence
from typing import Protocol

import genanki
from functionalpy._sequence import Seq

from personal_mnemonic_medium.v2.domain.prompt_destination.anki_connect.prompt_converter.anki_cloze import (
    AnkiCloze,
)
from personal_mnemonic_medium.v2.domain.prompt_destination.anki_connect.prompt_converter.anki_qa import (
    AnkiQA,
)

from ....prompts.base_prompt import BasePrompt
from ....prompts.cloze_prompt import ClozePrompt
from ....prompts.qa_prompt import QAPrompt


class AnkiCard(Protocol):
    @property
    def uuid(self) -> int:
        ...

    @property
    def genanki_model(self) -> genanki.Model:
        ...


class AnkiPromptConverter:
    @staticmethod
    def _prompt_to_card(prompt: BasePrompt) -> AnkiCard:
        match prompt:
            case QAPrompt():
                card = AnkiQA(
                    question=prompt.question, answer=prompt.answer
                )
            case ClozePrompt():
                card = AnkiCloze(text=prompt.text)
            case BasePrompt():
                raise ValueError(
                    "BasePrompt is the base class for all prompts, use a subclass"
                )

        return card

    @staticmethod
    def prompts_to_cards(
        prompts: Sequence[BasePrompt]
    ) -> Sequence[AnkiCard]:
        """Takes an iterable of prompts and turns them into AnkiCards"""

        return (
            Seq(prompts)
            .map(AnkiPromptConverter._prompt_to_card)
            .to_list()
        )
