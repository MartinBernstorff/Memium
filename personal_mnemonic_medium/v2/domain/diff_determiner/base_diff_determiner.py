from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Generic, Protocol, TypeVar

from personal_mnemonic_medium.v2.domain.prompt_destination.base_prompt_destination import (
    PromptDestinationCommand,
)

from ..prompt_destination.destination_commands import (
    DeletePrompts,
    PushPrompts,
)
from ..prompts.base_prompt import BasePrompt

K = TypeVar("K")
T = TypeVar("T")
S = TypeVar("S")


class BaseDiffDeterminer(Protocol):
    def sync(
        self,
        source_prompts: Sequence[BasePrompt],
        destination_prompts: Sequence[BasePrompt],
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
    def __init__(self, tmp_read_dir: Path, tmp_write_dir: Path):
        # TODO: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues/308 refactor: get rid of tmp_read_dir and tmp_write_dir
        self.tmp_read_dir = tmp_read_dir
        self.tmp_read_dir.mkdir(exist_ok=True)

        self.tmp_write_dir = tmp_write_dir
        self.tmp_write_dir.mkdir(exist_ok=True)

    def sync(
        self,
        source_prompts: Sequence[BasePrompt],
        destination_prompts: Sequence[BasePrompt],
    ) -> Sequence[PromptDestinationCommand]:
        syncer = GeneralSyncer(
            source={prompt.uid: prompt for prompt in source_prompts},
            destination={
                prompt.uid: prompt for prompt in destination_prompts
            },
        )

        return [
            DeletePrompts(syncer.only_in_destination()),
            PushPrompts(
                syncer.only_in_source(),
                tmp_write_dir=self.tmp_write_dir,
                tmp_read_dir=self.tmp_read_dir,
            ),
        ]


class FakeDiffDeterminer(BaseDiffDeterminer):
    def sync(
        self,
        source_prompts: Sequence[BasePrompt],
        destination_prompts: Sequence[BasePrompt],
    ) -> Sequence[PromptDestinationCommand]:
        ...
