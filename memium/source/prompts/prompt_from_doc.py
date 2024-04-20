from abc import ABC
from collections.abc import Sequence
from dataclasses import dataclass
from urllib.parse import quote

from ..document import Document
from .prompt import BasePrompt


@dataclass(frozen=True)
class PromptFromDocMixin(BasePrompt, ABC):
    parent_doc: Document
    line_nr: int

    @property
    def scheduling_uid(self) -> int: ...

    @property
    def update_uid(self) -> int: ...

    @property
    def tags(self) -> Sequence[str]: ...

    @property
    def edit_url(self) -> str | None:
        return obsidian_url(self.parent_doc.title, self.line_nr)


def obsidian_url(file_title: str, line_nr: int | None) -> str:
    url = f"obsidian://advanced-uri?filename={quote(file_title)}"
    if line_nr:
        url += f"&line={line_nr}"
    return url
