from collections.abc import Sequence
from dataclasses import dataclass

from iterpy import Arr

from memium.source.prompt import QAPrompt, QAWithDoc


@dataclass(frozen=True)
class TitleAsAnswerProcessor:
    """Extracts prompts from a document, but does not add the document to the front of the prompt. E.g.:

    # Lion
    Q. Definition?
    A. A large African cat with a mane.

    Results in:
    Q. Term for 'A large African cat with a mane'?
    A. Lion
    """

    question_matcher: str
    reversed_question: str

    def __post_init__(self):
        if "%s" not in self.reversed_question:
            raise ValueError(
                "reversed_question must contain '%s' to be replaced with the document title"
            )

    def _expand_prompt(self, prompt: QAWithDoc) -> QAWithDoc:
        answer = prompt.prompt.answer
        if answer[-1] in ".,!?;:":
            answer = answer[:-1]

        return QAWithDoc(
            prompt=QAPrompt(
                question=self.reversed_question % answer, answer=prompt.parent_doc.source_path.stem
            ),
            parent_doc=prompt.parent_doc,
            line_nr=prompt.line_nr,
            render_parent_doc=False,
        )

    def __call__(self, prompts: Sequence[QAWithDoc]) -> Sequence[QAWithDoc]:
        definition_prompts = (
            Arr(prompts)
            .filter(lambda p: self.question_matcher in p.prompt.question)
            .map(lambda p: self._expand_prompt(p))
        )

        return [*prompts, *definition_prompts]
