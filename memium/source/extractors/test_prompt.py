from dataclasses import dataclass

from memium.source.document import Document
from memium.source.prompts.prompt_qa import QAFromDoc, QAPrompt


@dataclass(frozen=True)
class FakeQAPrompt(QAPrompt):
    @property
    def edit_url(self) -> str:
        return ""

    def to_qa_from_doc(self, doc: Document, line_nr: int) -> QAPrompt:
        return QAFromDoc(
            parent_doc=doc, line_nr=line_nr, question=self.question, answer=self.answer
        )

    def __repr__(self) -> str:
        return f"{self.question!r}\n{self.answer!r})"
