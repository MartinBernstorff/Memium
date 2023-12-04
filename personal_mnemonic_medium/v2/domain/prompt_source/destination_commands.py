from collections.abc import Sequence
from dataclasses import dataclass
from typing import Protocol

from ....domain.prompt_extractors.prompt import Prompt


class PromptDestinationCommand(Protocol):
    ...


@dataclass(frozen=True)
class DeletePrompts(PromptDestinationCommand):
    prompts: Sequence[Prompt]


@dataclass(frozen=True)
class PushPrompts(PromptDestinationCommand):
    prompts: Sequence[Prompt]
