from collections.abc import Sequence
from typing import Protocol, runtime_checkable


@runtime_checkable
class BasePrompt(Protocol):
    @property
    def scheduling_uid(self) -> int:
        """UID used when scheduling the prompt. If this UID changes, the old prompt is deleted and a new prompt is created."""
        ...

    @property
    def update_uid(self) -> int:
        """The UID used to determine whether the prompt state has changed. If this UID changes, the prompt is updated on the remote."""
        ...

    @property
    def tags(self) -> Sequence[str]: ...

    @property
    def edit_url(self) -> str | None:
        """A link which, when pressed, opens a location where the prompt can be edited. E.g. opens a given Markdown document in the correct editor, or a web interface for a CMS."""
        ...


from dataclasses import dataclass


@dataclass(frozen=True)
class DestinationPrompt:
    prompt: BasePrompt
    destination_id: str
