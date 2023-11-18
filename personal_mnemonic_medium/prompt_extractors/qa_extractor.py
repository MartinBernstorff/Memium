import logging
import re
from collections.abc import Sequence
from typing import Any

from personal_mnemonic_medium.note_factories.note import Document
from personal_mnemonic_medium.prompt_extractors.base import (
    PromptExtractor,
)
from personal_mnemonic_medium.prompt_extractors.prompt import Prompt

log = logging.getLogger(__name__)
# Log to disk, not to console.
logging.basicConfig(
    filename="qa_extractor.log", filemode="w", level=logging.DEBUG
)


class QAPrompt(Prompt):
    def __init__(
        self, question: str, answer: str, *args: Any, **kwargs: Any
    ) -> None:
        super().__init__(*args, **kwargs)
        self.question = question
        self.answer = answer


class QAPromptExtractor(PromptExtractor):
    def __init__(
        self, question_prefix: str = "Q.", answer_prefix: str = "A."
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
        prompts = []

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

                prompts.append(  # type: ignore
                    QAPrompt(
                        question=question,
                        answer=answer,
                        tags=note.tags,
                        note_uuid=note.uuid,
                        source_note=note,
                        line_nr=block_starting_line_nr,
                    )
                )

            block_lines = len(
                re.findall(r"\n", block_string, flags=re.DOTALL)
            )
            block_starting_line_nr += block_lines

        return prompts  # type: ignore
