from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Generic, TypeVar

from memium.source.prompt import QAWithDoc

from .destination.destination import DestinationPrompt

K = TypeVar("K")
T = TypeVar("T")
S = TypeVar("S")


@dataclass(frozen=True)
class GeneralSyncer(Generic[K, T, S]):
    source: Mapping[K, T]
    destination: Mapping[K, S]

    def only_in_source(self) -> Sequence[T]:
        return [value for key, value in self.source.items() if key not in self.destination]

    def only_in_destination(self) -> Sequence[S]:
        return [value for key, value in self.destination.items() if key not in self.source]


class PromptDiffDeterminer:
    def to_delete(
        self, source_prompts: Sequence[QAWithDoc], destination_prompts: Sequence[DestinationPrompt]
    ) -> Sequence[DestinationPrompt]:
        # Only delete prompts whose content have changed. This essentially resets their scheduling.
        prompts_to_delete = GeneralSyncer(
            source={prompt.scheduling_str: prompt for prompt in source_prompts},
            destination={
                dest_prompt.prompt.scheduling_uid_str: dest_prompt
                for dest_prompt in destination_prompts
            },
        ).only_in_destination()

        return prompts_to_delete
