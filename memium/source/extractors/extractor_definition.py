from collections.abc import Sequence
from typing import cast

from iterpy import Arr

from memium.source.document import Document
from memium.source.extractors.extractor import BasePromptExtractor
from memium.source.extractors.extractor_qa import QAPromptExtractor
from memium.source.prompts.prompt_qa import QAFromDoc, QAPrompt


class ReversedDefinitionExtractor(BasePromptExtractor):
    def __init__(self, qa_extractor: QAPromptExtractor) -> None:
        self.qa_extractor = qa_extractor

    def extract_prompts(self, document: Document) -> Sequence[QAPrompt]:
        qa_prompts = self.qa_extractor.extract_prompts(document)
        definition_prompts = Arr(qa_prompts).filter(lambda prompt: "Definition?" in prompt.question)

        if definition_prompts.len() == 0:
            return []

        prompt = cast(QAFromDoc, definition_prompts[0])
        answer = prompt.answer.rstrip()
        if answer[-1] in ".,!?;:":
            answer = answer[:-1]

        return [
            QAFromDoc(
                parent_doc=document,
                line_nr=prompt.line_nr,
                question=f"Term for '{answer}'?",
                answer=document.source_path.stem,
                render_parent_doc=False,
            )
        ]
