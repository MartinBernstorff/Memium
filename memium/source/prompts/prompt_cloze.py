from collections.abc import Sequence
from dataclasses import dataclass

from ...utils.hash_cleaned_str import clean_str, hash_str_to_int
from ..document import Document
from .prompt import BasePrompt


@dataclass(frozen=True)
class ClozePrompt(BasePrompt):
    text: str

    @property
    def scheduling_uid(self) -> int:
        return hash_str_to_int(clean_str(self.text))

    @property
    def update_uid(self) -> int:
        return hash_str_to_int(f"{(self.text)}{self.tags}")

    @property
    def tags(self) -> Sequence[str]:
        return ()


@dataclass(frozen=True)
class ClozeWithoutDoc(ClozePrompt):
    add_tags: Sequence[str]

    @property
    def tags(self) -> Sequence[str]:
        return self.add_tags


@dataclass(frozen=True)
class ClozeFromDoc(ClozePrompt):
    text: str
    source_doc: Document

    @property
    def scheduling_uid(self) -> int:
        return hash_str_to_int(self.text)

    @property
    def tags(self) -> Sequence[str]:
        return self.source_doc.tags
