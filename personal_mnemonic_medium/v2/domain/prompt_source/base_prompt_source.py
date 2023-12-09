from collections.abc import Sequence
from typing import Protocol

from ..prompts.base_prompt import BasePrompt


class BasePromptSource(Protocol):
    def get_prompts(self) -> Sequence[BasePrompt]:
        ...


class FakePromptSource:
    def get_prompts(self) -> Sequence[BasePrompt]:
        ...
