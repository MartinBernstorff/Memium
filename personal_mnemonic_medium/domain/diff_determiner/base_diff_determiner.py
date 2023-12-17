from collections.abc import Mapping, Sequence
from typing import Generic, Protocol, TypeVar

from personal_mnemonic_medium.domain.prompt_destination.base_prompt_destination import (
    PromptDestinationCommand,
)

from ..prompt_destination.destination_commands import (
    DeletePrompts,
    PushPrompts,
)
from ..prompts.base_prompt import BasePrompt, DestinationPrompt

K = TypeVar("K")
T = TypeVar("T")
S = TypeVar("S")


class BaseDiffDeterminer(Protocol):
    def sync(
        self,
        source_prompts: Sequence[BasePrompt],
        destination_prompts: Sequence[DestinationPrompt],
    ) -> Sequence[PromptDestinationCommand]:
        ...


class GeneralSyncer(Generic[K, T, S]):
    def __init__(
        self, source: Mapping[K, T], destination: Mapping[K, S]
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


class PromptDiffDeterminer(BaseDiffDeterminer):
    def sync(
        self,
        source_prompts: Sequence[BasePrompt],
        destination_prompts: Sequence[DestinationPrompt],
    ) -> Sequence[PromptDestinationCommand]:
        syncer = GeneralSyncer(
            source={prompt.uid: prompt for prompt in source_prompts},
            destination={
                dest_prompt.prompt.uid: dest_prompt
                for dest_prompt in destination_prompts
            },
        )

        return [
            DeletePrompts(syncer.only_in_destination()),
            PushPrompts(syncer.only_in_source()),
        ]
