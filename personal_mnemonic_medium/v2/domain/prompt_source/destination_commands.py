from collections.abc import Sequence
from dataclasses import dataclass

from ..prompts.base_prompt import BasePrompt


@dataclass(frozen=True)
class DeletePrompts:
    prompts: Sequence[BasePrompt]


@dataclass(frozen=True)
class PushPrompts:
    prompts: Sequence[BasePrompt]


PromptDestinationCommand = DeletePrompts | PushPrompts
