from collections.abc import Sequence
from typing import Protocol

from memium.source.prompt import QAWithDoc

from ..document import Document


class BasePromptExtractor(Protocol):
    def extract_prompts(self, document: Document) -> Sequence[QAWithDoc]: ...
