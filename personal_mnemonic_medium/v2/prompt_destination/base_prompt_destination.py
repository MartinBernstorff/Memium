from collections.abc import Sequence
from typing import Protocol

from personal_mnemonic_medium.domain.prompt_extractors.prompt import (
    Prompt,
)

from ..prompt_source.destination_commands import (
    PromptDestinationCommand,
)


class BasePromptDestination(Protocol):
    def get_all_prompts(self) -> Sequence[Prompt]:
        ...

    def update(
        self, command: Sequence[PromptDestinationCommand]
    ) -> None:
        ...


class FakePromptDestination(BasePromptDestination):
    def get_all_prompts(self) -> Sequence[Prompt]:
        ...

    def update(
        self, command: Sequence[PromptDestinationCommand]
    ) -> None:
        ...
