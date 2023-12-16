from collections.abc import Sequence
from dataclasses import dataclass

from ..prompt_source.document_ingesters.document import Document
from ..utils.hash_cleaned_str import hash_cleaned_str
from .base_prompt import BasePrompt


@dataclass(frozen=True)
class QAPrompt(BasePrompt):
    question: str
    answer: str

    @property
    def uid(self) -> int:
        return hash_cleaned_str(self.question)

    @property
    def tags(self) -> Sequence[str]:
        return ()


@dataclass(frozen=True)
class QAWithoutDoc(QAPrompt):
    add_tags: Sequence[str]

    @property
    def tags(self) -> Sequence[str]:
        return self.add_tags


@dataclass(frozen=True)
class QAFromDoc(QAPrompt):
    parent_doc: Document
    line_nr: int

    @property
    def tags(self) -> Sequence[str]:
        return self.parent_doc.tags
