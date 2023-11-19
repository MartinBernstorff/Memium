from abc import ABC, abstractmethod
from collections.abc import Sequence

from personal_mnemonic_medium.data_access.document_ingesters.document import (
    Document,
)
from personal_mnemonic_medium.domain.prompt_extractors.prompt import (
    Prompt,
)


class PromptExtractor(ABC):
    @abstractmethod
    def extract_prompts(self, note: Document) -> Sequence[Prompt]:
        pass
