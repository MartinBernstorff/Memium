from collections.abc import Sequence
from typing import Protocol

from personal_mnemonic_medium.v2.domain.prompt_destination.base_prompt_destination import (
    PromptDestinationCommand,
)

from ..prompts.base_prompt import BasePrompt


class BaseSyncer(Protocol):
    def sync(
        self,
        source_prompts: Sequence[BasePrompt],
        destination_prompts: Sequence[BasePrompt],
    ) -> Sequence[PromptDestinationCommand]:
        ...


class FakeDiffDeterminer(BaseSyncer):
    def sync(
        self,
        source_prompts: Sequence[BasePrompt],
        destination_prompts: Sequence[BasePrompt],
    ) -> Sequence[PromptDestinationCommand]:
        ...
