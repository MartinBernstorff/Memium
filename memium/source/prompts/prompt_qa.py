from collections.abc import Sequence
from dataclasses import dataclass
from typing import Protocol
from urllib.parse import quote

from memium.source.document import Document
from memium.source.prompts.prompt import BasePrompt

from ...utils.hash_cleaned_str import clean_str, hash_str_to_int


class QAPromptProtocol(Protocol):
    question: str
    answer: str


@dataclass(frozen=True)
class QAWithoutDoc(BasePrompt, QAPromptProtocol):
    question: str
    answer: str

    add_tags: Sequence[str]

    @property
    def scheduling_uid_str(self) -> str:
        """Str used for generating the update_uid. Super helpful for debugging."""
        return qa_scheduling_uid_str(self.question, self.answer)

    @property
    def scheduling_uid(self) -> int:
        return hash_str_to_int(self.scheduling_uid_str)

    @property
    def update_uid_str(self) -> str:
        """Str used for generating the update_uid. Super helpful for debugging."""
        return qa_update_uid_str(self.question, self.answer, self.tags)

    @property
    def update_uid(self) -> int:
        return hash_str_to_int(self.update_uid_str)

    @property
    def tags(self) -> Sequence[str]:
        return self.add_tags

    @property
    def edit_url(self) -> str | None:
        return None


def obsidian_url(file_title: str, line_nr: int | None) -> str:
    url = f"obsidian://advanced-uri?filename={quote(file_title)}"
    if line_nr:
        url += f"&line={line_nr}"
    return url


class PromptFromDoc(Protocol):
    parent_doc: Document
    line_nr: int

    @property
    def edit_url(self) -> str | None: ...


@dataclass(frozen=True)
class QAFromDoc(BasePrompt, QAPromptProtocol, PromptFromDoc):
    question: str
    answer: str

    parent_doc: Document

    line_nr: int

    render_parent_doc: bool = True

    @property
    def scheduling_uid_str(self) -> str:
        return qa_scheduling_uid_str(self.question, self.answer)

    @property
    def scheduling_uid(self) -> int:
        return hash_str_to_int(self.scheduling_uid_str)

    @property
    def update_uid_str(self) -> str:
        return qa_update_uid_str(self.question, self.answer, self.parent_doc.tags)

    @property
    def update_uid(self) -> int:
        return hash_str_to_int(self.update_uid_str)

    @property
    def tags(self) -> Sequence[str]:
        return self.parent_doc.tags

    @property
    def edit_url(self) -> str | None:
        return obsidian_url(self.parent_doc.title, self.line_nr)


def qa_scheduling_uid_str(question: str, answer: str) -> str:
    return f"{clean_str(question)}_{clean_str(answer)}"


def qa_update_uid_str(question: str, answer: str, tags: Sequence[str]) -> str:
    return f"{question}_{answer}_{tags}"


QAPrompt = QAWithoutDoc | QAFromDoc
