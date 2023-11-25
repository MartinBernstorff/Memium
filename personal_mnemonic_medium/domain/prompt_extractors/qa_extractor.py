import logging
import re
from collections.abc import Sequence
from dataclasses import dataclass

from personal_mnemonic_medium.data_access.document_ingesters.document import (
    Document,
)
from personal_mnemonic_medium.domain.prompt_extractors.base import (
    PromptExtractor,
)
from personal_mnemonic_medium.domain.prompt_extractors.prompt import (
    Prompt,
)

log = logging.getLogger(__name__)
# Log to disk, not to console.
logging.basicConfig(
    filename="qa_extractor.log", filemode="w", level=logging.DEBUG
)


@dataclass
class QAPrompt(Prompt):
    question: str
    answer: str
    source_doc: Document
    line_nr: int | None = None

    @property
    def note_uuid(self) -> str:
        return self.source_doc.uuid

    @property
    def tags(self) -> Sequence[str]:
        return self.source_doc.tags


# TODO: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues/245 remove defaults from extractors to make signature easier to understand
class QAPromptExtractor(PromptExtractor):
    def __init__(
        self, question_prefix: str, answer_prefix: str
    ) -> None:
        self.question_prefix = question_prefix
        self.answer_prefix = answer_prefix

    def _get_first_question(self, string: str) -> str:
        question = re.findall(
            self.question_prefix + r"{0,1}\.(?:(?!A\.).)*",
            string,
            flags=re.DOTALL,
        )[0]

        return question[len(self.question_prefix) + 1 :].rstrip()

    def _get_first_answer(self, string: str) -> str:
        # I have to use positive lookahead to match code-blocks - to ensure the last answer is matched as well, I add 2 newlines to string. A little hacky.
        string_padded = f"{string.rstrip()}\n\n"

        answer = re.findall(
            r"\n" + self.answer_prefix + r"[ \n]+\n*.+",
            string_padded,
            re.DOTALL,
        )[0]

        return answer[len(self.answer_prefix) + 2 :].rstrip()

    @staticmethod
    def _break_string_by_two_or_more_newlines(
        string: str
    ) -> list[str]:
        """Break string into a list by 2+ newlines in a row."""
        return re.split(r"(\n\n)+", string)

    def _has_qa(self, string: str) -> bool:
        """Check whether a string contains a qa prompt"""
        if (
            len(
                re.findall(
                    r"^(?![:>]).*"
                    + self.question_prefix
                    + r"{0,1}\. ",
                    string,
                    flags=re.DOTALL,
                )
            )
            != 0
        ):
            return True
        return False

    def extract_prompts(self, note: Document) -> Sequence[QAPrompt]:
        prompts: list[QAPrompt] = []

        blocks = self._break_string_by_two_or_more_newlines(
            note.content
        )

        block_starting_line_nr = 1
        for block_string in blocks:
            if self._has_qa(block_string):
                question = self._get_first_question(block_string)
                try:
                    answer = self._get_first_answer(block_string)
                except IndexError:
                    logging.warn(
                        f"Could not find answer in {note.title} for {question}"
                    )
                    continue

                prompts.append(
                    QAPrompt(
                        question=question,
                        answer=answer,
                        source_doc=note,
                        line_nr=block_starting_line_nr,
                    )
                )

            block_lines = len(
                re.findall(r"\n", block_string, flags=re.DOTALL)
            )
            block_starting_line_nr += block_lines

        return prompts  # type: ignore
