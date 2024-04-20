import logging
import re
from collections.abc import Sequence
from pathlib import Path

from ..document import Document
from ..prompts.prompt_qa import QAFromDoc, QAPrompt
from .extractor import BasePromptExtractor

log = logging.getLogger(__name__)


class QAPromptExtractor(BasePromptExtractor):
    def __init__(self, question_prefix: str, answer_prefix: str) -> None:
        self.question_prefix = question_prefix
        self.answer_prefix = answer_prefix

    def _get_first_question(self, content: str) -> str:
        question = re.findall(
            self.question_prefix + r"{0,1}\.(?:(?!A\.).)*", content, flags=re.DOTALL
        )[0]

        return question[len(self.question_prefix) + 1 :].rstrip()

    def _get_first_answer(self, content: str) -> str:
        # Have to use positive lookahead to match code-blocks
        # To ensure the last answer is matched as well, we add 2 newlines to string.
        string_padded = f"{content.rstrip()}\n\n"

        answer = re.findall(r"\n" + self.answer_prefix + r"[ \n]+\n*.+", string_padded, re.DOTALL)[
            0
        ]

        return answer[len(self.answer_prefix) + 2 :].rstrip()

    @staticmethod
    def _string_to_blocks_by_newlines(string: str) -> list[str]:
        """Break string into a list by 2+ newlines in a row."""
        return re.split(r"(\n\n)+", string)

    def _has_qa(self, string: str) -> bool:
        """Check whether a string contains a qa prompt"""
        return (
            len(
                re.findall(
                    r"^(?![:>]).*" + self.question_prefix + r"{0,1}\. ", string, flags=re.DOTALL
                )
            )
            != 0
        )

    def extract_prompts(self, document: Document) -> Sequence[QAPrompt]:
        prompts: list[QAPrompt] = []
        blocks = self._string_to_blocks_by_newlines(document.content)
        block_starting_line_nr = 1

        for block_string in blocks:
            if self._has_qa(block_string):
                question = self._get_first_question(block_string)
                try:
                    answer = self._get_first_answer(block_string)
                except IndexError:
                    logging.warn(f"Could not find answer in {document.title} for {question}")
                    continue

                prompts.append(
                    QAFromDoc(
                        question=question,
                        answer=answer,
                        parent_doc=document,
                        line_nr=block_starting_line_nr,
                    )
                )

            block_lines = len(re.findall(r"\n", block_string, flags=re.DOTALL))
            block_starting_line_nr += block_lines

        return prompts


def test_qa_prompt_extractor(tmpdir: Path):
    doc = Document(
        content="""

Q. What is the meaning of life?
A. 42

#anki/tag/test_tag

""",
        source_path=tmpdir / "test.md",
    )

    extractor = QAPromptExtractor(question_prefix="Q.", answer_prefix="A.").extract_prompts(doc)

    assert len(extractor) == 1
    prompt = extractor[0]
    assert prompt.question == "What is the meaning of life?"
    assert prompt.answer == "42"
    assert prompt.tags == ["anki/tag/test_tag"]
    assert prompt.scheduling_uid == 3643087944
