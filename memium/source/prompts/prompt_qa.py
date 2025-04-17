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
class QAPromptImpl(QAPromptProtocol):
    """Value object for a question-answer prompt. Its identity is determined entirely by its values."""

    question: str
    answer: str

    def __post_init__(self):
        """Styling should not occur in this value object, since any change to style would change its scheduling identity.

        Instead, styling should happen in the destination (e.g. AnkiQA)."""
        forbidden = ["style="]

        errors: list[str] = []
        for tag in forbidden:
            if tag in self.question:
                errors.append(f"'{tag}' found in question")
            if tag in self.answer:
                errors.append(f"'{tag}' found in answer")

        if errors:
            error_str = "\n".join(errors)
            raise ValueError(error_str)

    @staticmethod
    def dummy(question: str = "DummyQuestion", answer: str = "DummyAnswer") -> "QAPromptImpl":
        return QAPromptImpl(question=question, answer=answer)

    @property
    def scheduling_uid_str(self) -> str:
        """Str used for generating the update_uid. Super helpful for debugging."""
        return qa_scheduling_uid_str(self.question, self.answer)

    @property
    def scheduling_uid(self) -> int:
        return hash_str_to_int(self.scheduling_uid_str)


def _update_uid_str(scheduling_uid: str, tags: Sequence[str]) -> str:
    return scheduling_uid + "_" + "_".join(tags)


@dataclass(frozen=True)
class QAWithoutDoc(BasePrompt):
    prompt: QAPromptImpl

    add_tags: Sequence[str]

    @staticmethod
    def dummy(
        question: str = "DummyQuestion",
        answer: str = "DummyAnswer",
        tags: Sequence[str] = ("DummyTag",),
    ) -> "QAWithoutDoc":
        return QAWithoutDoc(QAPromptImpl(question=question, answer=answer), add_tags=tags)

    @property
    def scheduling_uid_str(self) -> str:
        return self.prompt.scheduling_uid_str

    @property
    def scheduling_uid(self) -> int:
        return self.prompt.scheduling_uid

    @property
    def update_uid_str(self) -> str:
        return _update_uid_str(self.scheduling_uid_str, self.tags)

    @property
    def update_uid(self) -> int:
        return hash_str_to_int(self.update_uid_str)

    @property
    def tags(self) -> Sequence[str]:
        return self.add_tags

    @property
    def edit_url(self) -> str | None:
        return None

    def to_qa_from_doc(self, doc: Document, line_nr: int) -> "QAFromDoc":
        return QAFromDoc(prompt=self.prompt, parent_doc=doc, line_nr=line_nr)


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
class QAFromDoc(BasePrompt, PromptFromDoc):
    prompt: QAPromptImpl

    parent_doc: Document

    line_nr: int

    render_parent_doc: bool = True

    @property
    def scheduling_uid_str(self) -> str:
        return self.prompt.scheduling_uid_str

    @property
    def scheduling_uid(self) -> int:
        return self.prompt.scheduling_uid

    @property
    def update_uid_str(self) -> str:
        return _update_uid_str(self.scheduling_uid_str, self.tags)

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
