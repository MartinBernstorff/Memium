from collections.abc import Sequence
from typing import Protocol

from ..prompts.base_prompt import DestinationPrompt
from .destination_commands import PromptDestinationCommand


class PromptDestination(Protocol):
    def get_all_prompts(self) -> Sequence[DestinationPrompt]:
        ...

    def update(
        self, commands: Sequence[PromptDestinationCommand]
    ) -> None:
        ...


class FakePromptDestination(PromptDestination):
    def get_all_prompts(self) -> Sequence[DestinationPrompt]:
        ...

    def update(
        self, commands: Sequence[PromptDestinationCommand]
    ) -> None:
        ...
