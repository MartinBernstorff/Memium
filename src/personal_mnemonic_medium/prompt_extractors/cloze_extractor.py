import hashlib
import re
from typing import List

from personal_mnemonic_medium.note_factories.note import Note
from personal_mnemonic_medium.prompt_extractors.prompt import Prompt


class ClozePrompt(Prompt):
    def __init__(self, content: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.content = content


class ClozePromptExtractor:
    def __init__(self) -> None:
        pass

    @staticmethod
    def break_string_by_two_or_more_newlines(string: str) -> List[str]:
        """Break string into a list by 2+ newlines in a row."""
        return re.split(r"(\n\n)+", string)

    @staticmethod
    def has_cloze(string: str) -> bool:
        if (
            len(re.findall(r"{.*}", string)) > 0
            and "BearID" not in string
            and "$$" not in string
        ):
            return True
        return False

    @staticmethod
    def replace_cloze_id_with_unique(string, selected_cloze=None) -> str:
        """Each cloze deletion in a note is numbered sequentially.

        This function ensures that the numbering is based on the content of the cloze deletion, essentially ensuring that if you modify the contents of a cloze, only the scheduling of that specific cloze is changed.


        Args:
            string (str): The string to replace the cloze id with a unique id.
            selected_cloze (str, optional): If you only want to replace a specific cloze, pass it here. Defaults to None.
        """
        if selected_cloze is not None:
            selected_clozes = [selected_cloze]
        else:
            selected_clozes = re.findall(r"{(?!BearID).[^}]*}", string)

        for cloze in selected_clozes:
            hash = int(hashlib.sha256(cloze.encode("utf-8")).hexdigest(), 16) % 10**3

            new_cloze = f"{{{{c{hash}::{cloze[1:-1]}}}}}"

            string = string.replace(cloze, new_cloze)

        return string

    def extract_prompts(self, note: Note) -> List[ClozePrompt]:
        prompts = []

        blocks = self.break_string_by_two_or_more_newlines(note.content)

        for block_string in blocks:
            if self.has_cloze(block_string):
                clozes = re.findall(r"{(?!BearID).[^}]*}", block_string)

                for selected_cloze in clozes:
                    prompt_content = self.replace_cloze_id_with_unique(
                        block_string, selected_cloze=selected_cloze
                    )

                    prompts.append(
                        ClozePrompt(
                            content=prompt_content,
                            tags=note.tags,
                            uuid=note.uuid,
                            source_note=note,
                        )
                    )

        return prompts
