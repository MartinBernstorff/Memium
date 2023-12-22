from collections.abc import Sequence
from typing import Protocol


class BasePrompt(Protocol):
    @property
    def scheduling_uid(self) -> int:
        """UID used when scheduling the prompt. If this UID changes, the scheduling of the prompt is reset."""
        ...

    @property
    def update_uid(self) -> int:
        """The UID used to determine whether the prompt state has changed. If this UID changes, the prompt is updated on the remote."""
        ...

    @property
    def tags(self) -> Sequence[str]:
        ...


from dataclasses import dataclass


@dataclass(frozen=True)
class DestinationPrompt:
    prompt: BasePrompt
    destination_id: str
