import re
from multiprocessing.sharedctypes import Value
from typing import Any, List

from personal_mnemonic_medium.note_factories.note import Document
from personal_mnemonic_medium.prompt_extractors.prompt import Prompt


class QAPrompt(Prompt):
    def __init__(self, question: str, answer: str, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.question = question
        self.answer = answer


class QAPromptExtractor:
    def __init__(self, question_prefix: str = "Q.", answer_prefix: str = "A.") -> None:
        self.question_prefix = question_prefix
        self.answer_prefix = answer_prefix

    def get_first_question(self, string: str) -> str:
        question = re.findall(
            self.question_prefix + r"{0,1}\.(?:(?!A\.).)*",
            string,
            flags=re.DOTALL,
        )[0]

        return question[len(self.question_prefix) + 1 :].rstrip()

    def get_first_answer(self, string: str) -> str:
        # I have to use positive lookahead to match code-blocks - to ensure the last answer is matched as well, I add 2 newlines to string. A little hacky.
        string_padded = f"{string.rstrip()}\n\n"

        answer = re.findall(
            r"\n" + self.answer_prefix + r"[ \n]+\n*.+",
            string_padded,
            re.DOTALL,
        )[0]

        return answer[len(self.answer_prefix) + 2 :].rstrip()

    @staticmethod
    def break_string_by_two_or_more_newlines(string: str) -> List[str]:
        """Break string into a list by 2+ newlines in a row."""
        return re.split(r"(\n\n)+", string)

    def has_qa(self, string: str) -> bool:
        """Check whether a string contains a qa prompt"""
        if (
            len(
                re.findall(
                    r"^(?![:>]).*" + self.question_prefix + r"{0,1}\. ",
                    string,
                    flags=re.DOTALL,
                ),
            )
            != 0
        ):
            return True
        return False

    def extract_prompts(self, note: Document) -> List[QAPrompt]:
        prompts = []

        blocks = self.break_string_by_two_or_more_newlines(note.content)

        for block_string in blocks:
            if self.has_qa(block_string):
                question = self.get_first_question(block_string)
                try:
                    answer = self.get_first_answer(block_string)
                except IndexError as e:
                    print(
                        f"Could not find answer in {note.title} for {question}",
                    )
                    continue

                prompts.append(
                    QAPrompt(
                        question=question,
                        answer=answer,
                        tags=note.tags,
                        note_uuid=note.uuid,
                        source_note=note,
                    ),
                )

        return prompts
