from collections.abc import Mapping, Sequence
from typing import Generic, Protocol, TypeVar

from personal_mnemonic_medium.v2.domain.prompt_destination.base_prompt_destination import (
    PromptDestinationCommand,
)

from ..prompts.base_prompt import BasePrompt

T = TypeVar("T")
S = TypeVar("S")


class BaseSyncer(Protocol):
    def sync(
        self,
        source_prompts: Sequence[BasePrompt],
        destination_prompts: Sequence[BasePrompt],
    ) -> Sequence[PromptDestinationCommand]:
        ...


class GeneralSyncer(Generic[T, S]):
    def __init__(
        self, source: Mapping[str, T], destination: Mapping[str, S]
    ):
        self.source = source
        self.destination = destination

    def only_in_source(self) -> Sequence[T]:
        return [
            value
            for key, value in self.source.items()
            if key not in self.destination
        ]

    def only_in_destination(self) -> Sequence[S]:
        return [
            value
            for key, value in self.destination.items()
            if key not in self.source
        ]


class FakeDiffDeterminer(BaseSyncer):
    def sync(
        self,
        source_prompts: Sequence[BasePrompt],
        destination_prompts: Sequence[BasePrompt],
    ) -> Sequence[PromptDestinationCommand]:
        ...
