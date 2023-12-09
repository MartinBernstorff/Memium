from collections.abc import Sequence
from typing import Protocol

from ..prompt_source.destination_commands import (
    PromptDestinationCommand,
)
from ..prompts.base_prompt import BasePrompt


class PromptDestination(Protocol):
    def get_all_prompts(self) -> Sequence[BasePrompt]:
        ...

    def update(
        self, commands: Sequence[PromptDestinationCommand]
    ) -> None:
        ...


class FakePromptDestination(PromptDestination):
    def get_all_prompts(self) -> Sequence[BasePrompt]:
        ...

    def update(
        self, commands: Sequence[PromptDestinationCommand]
    ) -> None:
        ...
