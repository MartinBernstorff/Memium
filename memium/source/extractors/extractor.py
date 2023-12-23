from collections.abc import Sequence
from typing import Protocol

from ..document import Document
from ..prompts.prompt import BasePrompt


# TODO: https://github.com/MartinBernstorff/memium/issues/297 Implement ClozeExtractor
class BasePromptExtractor(Protocol):
    def extract_prompts(self, document: Document) -> Sequence[BasePrompt]:
        ...
