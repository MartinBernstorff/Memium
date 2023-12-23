from collections.abc import Sequence
from dataclasses import dataclass

from ..source.prompts.prompt import BasePrompt, DestinationPrompt


@dataclass(frozen=True)
class DeletePrompts:
    prompts: Sequence[DestinationPrompt]


@dataclass(frozen=True)
class PushPrompts:
    prompts: Sequence[BasePrompt]


PromptDestinationCommand = DeletePrompts | PushPrompts
