from collections.abc import Sequence

from functionalpy._sequence import Seq

from personal_mnemonic_medium.v2.domain.prompt_destination.anki_connect.prompt_converter.prompts.anki_cloze import (
    AnkiCloze,
)
from personal_mnemonic_medium.v2.domain.prompt_destination.anki_connect.prompt_converter.prompts.anki_qa import (
    AnkiQA,
)
from personal_mnemonic_medium.v2.domain.prompt_destination.anki_connect.prompt_converter.prompts.base_anki_prompt import (
    AnkiPrompt,
)

from ....prompts.base_prompt import BasePrompt
from ....prompts.cloze_prompt import ClozePromptWithoutDoc
from ....prompts.qa_prompt import QAPrompt


class AnkiPromptConverter:
    @staticmethod
    def _prompt_to_card(prompt: BasePrompt) -> AnkiPrompt:
        match prompt:
            case QAPrompt():
                card = AnkiQA(
                    question=prompt.question, answer=prompt.answer
                )
            case ClozePromptWithoutDoc():
                card = AnkiCloze(text=prompt.text)
            case BasePrompt():
                raise ValueError(
                    "BasePrompt is the base class for all prompts, use a subclass"
                )

        return card

    @staticmethod
    def prompts_to_cards(
        prompts: Sequence[BasePrompt]
    ) -> Sequence[AnkiPrompt]:
        """Takes an iterable of prompts and turns them into AnkiCards"""

        return (
            Seq(prompts)
            .map(AnkiPromptConverter._prompt_to_card)
            .to_list()
        )
