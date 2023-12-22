from collections.abc import Sequence
from typing import Protocol

from .prompt_base import BasePrompt
from .document import Document


# TODO: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues/297 Implement ClozeExtractor
class BasePromptExtractor(Protocol):
    def extract_prompts(
        self, document: Document
    ) -> Sequence[BasePrompt]:
        ...
