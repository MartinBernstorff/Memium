from collections.abc import Sequence
from dataclasses import dataclass

from memium.source.document import Document
from memium.source.prompts.prompt_qa import (
    QAFromDoc,
    QAPrompt,
    QAWithoutDoc,
    qa_scheduling_uid_str,
    qa_update_uid_str,
)
from memium.utils.hash_cleaned_str import hash_str_to_int


@dataclass(frozen=True)
class DummyQAPrompt(QAWithoutDoc):
    question: str = "DummyQuestion"
    answer: str = "DummyAnswer"

    add_tags: Sequence[str] = ("DummyTag",)

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

    def to_qa_from_doc(self, doc: Document, line_nr: int) -> QAPrompt:
        return QAFromDoc(
            parent_doc=doc, line_nr=line_nr, question=self.question, answer=self.answer
        )

    def __repr__(self) -> str:
        return f"{self.question!r}\n{self.answer!r})"
