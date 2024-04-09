from collections.abc import Sequence
from dataclasses import dataclass
from typing import Protocol, TypeAlias

from ..source.prompts.prompt import BasePrompt, DestinationPrompt


@dataclass(frozen=True)
class PushPrompts:
    prompts: Sequence[BasePrompt]


@dataclass(frozen=True)
class DeletePrompts:
    prompts: Sequence[DestinationPrompt]


PromptDestinationCommand: TypeAlias = PushPrompts | DeletePrompts


class PromptDestination(Protocol):
    def get_all_prompts(self) -> Sequence[DestinationPrompt]: ...

    def update(self, commands: Sequence[PromptDestinationCommand]) -> None: ...
