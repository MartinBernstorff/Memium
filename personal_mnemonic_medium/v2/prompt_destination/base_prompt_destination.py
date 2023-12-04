from collections.abc import Sequence
from typing import Protocol

from personal_mnemonic_medium.domain.prompt_extractors.prompt import (
    Prompt,
)


class PromptDestinationCommand(Protocol):
    ...


class DeletePrompts(PromptDestinationCommand):
    def __init__(self, prompts: Sequence[Prompt]):
        ...


class PushPrompts(PromptDestinationCommand):
    def __init__(self, prompts: Sequence[Prompt]):
        ...


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
