from collections.abc import Sequence
from typing import Protocol

from personal_mnemonic_medium.domain.prompt_extractors.prompt import (
    Prompt,
)
from personal_mnemonic_medium.v2.prompt_destination.base_prompt_destination import (
    PromptDestinationCommand,
)


class BaseSyncer(Protocol):
    def sync(
        self,
        source_prompts: Sequence[Prompt],
        destination_prompts: Sequence[Prompt],
    ) -> Sequence[PromptDestinationCommand]:
        ...


class FakeSyncer(BaseSyncer):
    def sync(
        self,
        source_prompts: Sequence[Prompt],
        destination_prompts: Sequence[Prompt],
    ) -> Sequence[PromptDestinationCommand]:
        ...
