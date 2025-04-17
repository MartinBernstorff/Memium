from collections.abc import Sequence
from dataclasses import dataclass
from typing import cast

from iterpy import Arr

from memium.source.document import Document
from memium.source.extractors.extractor import BasePromptExtractor
from memium.source.extractors.extractor_qa import QAPromptExtractor
from memium.source.prompts.prompt_qa import QAFromDoc, QAPrompt, QAPromptImpl


@dataclass
class TitleAsAnswerExtractor(BasePromptExtractor):
    """Extracts prompts from a document, but does not add the document to the front of the prompt. E.g.:

    # Lion
    Q. Definition?
    A. A large African cat with a mane.

    Results in:
    Q. Term for 'A large African cat with a mane'?
    A. Lion
    """

    qa_extractor: QAPromptExtractor
    matcher: str
    reversed_question: str

    def extract_prompts(self, document: Document) -> Sequence[QAPrompt]:
        qa_prompts = self.qa_extractor.extract_prompts(document)
        definition_prompts = Arr(qa_prompts).filter(
            lambda prompt: self.matcher in prompt.prompt.question
        )

        if definition_prompts.len() == 0:
            return []

        prompt = cast(QAFromDoc, definition_prompts[0])
        answer = prompt.prompt.answer.rstrip()
        if answer[-1] in ".,!?;:":
            answer = answer[:-1]

        return [
            QAFromDoc(
                prompt=QAPromptImpl(
                    question=self.reversed_question % answer, answer=document.source_path.stem
                ),
                parent_doc=document,
                line_nr=prompt.line_nr,
                render_parent_doc=False,
            )
        ]
