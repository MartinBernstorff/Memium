from collections.abc import Sequence
from typing import Protocol

from personal_mnemonic_medium.domain.prompt_extractors.prompt import (
    Prompt,
)


class PromptExporter(Protocol):
    def sync_prompts(self, prompts: Sequence[Prompt]):
        ...
