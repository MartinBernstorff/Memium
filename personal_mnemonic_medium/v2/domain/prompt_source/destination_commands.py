from collections.abc import Sequence
from dataclasses import dataclass

from ....domain.prompt_extractors.prompt import Prompt


@dataclass(frozen=True)
class DeletePrompts:
    prompts: Sequence[Prompt]


@dataclass(frozen=True)
class PushPrompts:
    prompts: Sequence[Prompt]


PromptDestinationCommand = DeletePrompts | PushPrompts
