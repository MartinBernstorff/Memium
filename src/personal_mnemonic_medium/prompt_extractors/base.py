from abc import ABC, abstractmethod
from collections.abc import Sequence

from personal_mnemonic_medium.note_factories.note import Document
from personal_mnemonic_medium.prompt_extractors.prompt import Prompt


class PromptExtractor(ABC):
    @abstractmethod
    def extract_prompts(self, note: Document) -> Sequence[Prompt]:
        pass
