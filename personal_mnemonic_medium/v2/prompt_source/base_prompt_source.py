from collections.abc import Sequence
from typing import Protocol

from personal_mnemonic_medium.domain.prompt_extractors.prompt import (
    Prompt,
)


class BasePromptSource(Protocol):
    def get_prompts(self) -> Sequence[Prompt]:
        ...


class FakePromptSource:
    def get_prompts(self) -> Sequence[Prompt]:
        ...
