from collections.abc import Sequence
from dataclasses import dataclass

from personal_mnemonic_medium.v2.domain.prompts.hash_str import (
    int_hash_str,
)

from ....data_access.document_ingesters.document import Document
from .base_prompt import BasePrompt


@dataclass(frozen=True)
class QAPrompt(BasePrompt):
    question: str
    answer: str
    add_tags: Sequence[str]

    @property
    def uid(self) -> int:
        return int_hash_str(self.question)

    @property
    def tags(self) -> Sequence[str]:
        return self.add_tags


@dataclass(frozen=True)
class QAPromptFromDoc(QAPrompt):
    parent_doc: Document
    line_nr: int

    @property
    def tags(self) -> Sequence[str]:
        return self.parent_doc.tags
