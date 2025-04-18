from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

from memium.source.document import Document

from ..utils.hash_cleaned_str import clean_str, hash_str_to_int


def obsidian_url(file_title: str, line_nr: int | None) -> str:
    url = f"obsidian://advanced-uri?filename={quote(file_title)}"
    if line_nr:
        url += f"&line={line_nr}"
    return url


@dataclass(frozen=True)
class QAPrompt:
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
    def dummy(question: str = "DummyQuestion", answer: str = "DummyAnswer") -> "QAPrompt":
        return QAPrompt(question=question, answer=answer)

    @property
    def scheduling_uid_str(self) -> str:
        """Str used for generating the update_uid. Super helpful for debugging."""
        return cleaned_qa_scheduling_uid_str(self.question, self.answer)

    @property
    def scheduling_uid(self) -> int:
        return hash_str_to_int(self.scheduling_uid_str)


@dataclass(frozen=True)
class QAWithDoc:
    prompt: QAPrompt

    parent_doc: Document

    line_nr: int

    render_parent_doc: bool = True

    @staticmethod
    def dummy(
        question: str = "FakeQuestion",
        answer: str = "FakeAnswer",
        parent_doc: Document | None = None,
        line_nr: int = 0,
    ) -> "QAWithDoc":
        return QAWithDoc(
            prompt=QAPrompt.dummy(question, answer),
            parent_doc=Document("DummyContent", Path("DummyPath"))
            if parent_doc is None
            else parent_doc,
            line_nr=line_nr,
        )

    @property
    def scheduling_str(self) -> str:
        return self.prompt.scheduling_uid_str

    @property
    def scheduling_id(self) -> int:
        return self.prompt.scheduling_uid

    @property
    def tags(self) -> Sequence[str]:
        return self.parent_doc.tags

    @property
    def edit_url(self) -> str:
        return obsidian_url(self.parent_doc.title, self.line_nr)


def cleaned_qa_scheduling_uid_str(question: str, answer: str) -> str:
    return f"{clean_str(question)}_{clean_str(answer)}"


def qa_update_uid_str(question: str, answer: str, tags: Sequence[str]) -> str:
    return f"{question}_{answer}_{tags}"
