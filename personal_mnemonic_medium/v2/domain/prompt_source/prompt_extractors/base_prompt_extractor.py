from collections.abc import Sequence
from typing import Protocol

from ...prompts.base_prompt import BasePrompt
from ..document_ingesters.document import Document


# TODO: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues/294 Implement QA and Cloze promptextractors
class BasePromptExtractor(Protocol):
    def extract_prompts(
        self, document: Document
    ) -> Sequence[BasePrompt]:
        ...
