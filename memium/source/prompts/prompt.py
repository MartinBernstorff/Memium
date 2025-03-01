from collections.abc import Sequence
from dataclasses import dataclass
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


# refactor: I think this can be _dramatically_ simplified.
# * I don't use the cloze prompt, so that can be removed.
# * Why is tags a property? It's fine for now, but I don't think I'm really using it anywhere.


# refactor: is this basically a "materialised prompt"? If so, it means that it should contain more metadata; last review, due date, etc.
# ?: In general, for e.g. presentation, if there is more than one way of presenting a prompt, the presentation should be a function, not a method on the prompt.
@dataclass(frozen=True)
class DestinationPrompt:
    prompt: BasePrompt
    destination_id: str
