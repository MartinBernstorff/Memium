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
        return hash_cleaned_str(f"{self.question}_{self.answer}")

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

    def __repr__(self) -> str:
        return f"{self.parent_doc.source_path}:{self.line_nr}: \n\tQ. {self.question}\n\tA. {self.answer}"

    @property
    def tags(self) -> Sequence[str]:
        return self.parent_doc.tags
