from collections.abc import Sequence
from dataclasses import dataclass

from ...utils.hash_cleaned_str import hash_cleaned_str, int_hash_str
from ..document import Document
from .prompt import BasePrompt


@dataclass(frozen=True)
class QAPrompt(BasePrompt):
    question: str
    answer: str

    @property
    def scheduling_uid(self) -> int:
        return hash_cleaned_str(f"{self.question}_{self.answer}")

    @property
    def update_uid(self) -> int:
        return int_hash_str(f"{self.question}_{self.answer}_{self.tags}")

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
