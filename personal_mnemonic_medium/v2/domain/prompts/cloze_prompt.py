from collections.abc import Sequence
from dataclasses import dataclass

from ....data_access.document_ingesters.document import Document
from ..int_hash_str import int_hash_str
from .base_prompt import BasePrompt


@dataclass(frozen=True)
class ClozePrompt(BasePrompt):
    text: str
    add_tags: Sequence[str]

    @property
    def uid(self) -> int:
        return int_hash_str(self.text)

    @property
    def tags(self) -> Sequence[str]:
        return self.add_tags


from dataclasses import dataclass


@dataclass(frozen=True)
class ClozePromptFromDoc(ClozePrompt):
    parent_doc: Document
    line_nr: int

    @property
    def tags(self) -> Sequence[str]:
        return self.parent_doc.tags
