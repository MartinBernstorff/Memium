from abc import ABC
from collections.abc import Sequence
from dataclasses import dataclass

from ..document import Document
from .prompt import BasePrompt


@dataclass(frozen=True)
class PromptFromDocMixin(BasePrompt, ABC):
    parent_doc: Document
    line_nr: int

    @property
    def scheduling_uid(self) -> int:
        ...

    @property
    def update_uid(self) -> int:
        ...

    @property
    def tags(self) -> Sequence[str]:
        ...
