import hashlib
import logging
import re
from collections.abc import Sequence

from ..document import Document
from ..prompts.prompt_cloze import ClozeFromDoc, ClozePrompt
from .extractor import BasePromptExtractor

log = logging.getLogger(__name__)


class ClozePromptExtractor(BasePromptExtractor):
    @staticmethod
    def _get_blocks(string: str) -> list[str]:
        """Break string into a list by 2+ newlines in a row."""
        # Exclude entire code blocks
        string_sans_code_blocks = re.sub(r"```.*?```", "", string, flags=re.DOTALL)
        return re.split(r"(\n\n)+", string_sans_code_blocks)

    @staticmethod
    def _has_cloze(string: str) -> bool:
        if len(re.findall(r"{.*}", string)) > 0:
            return True
        return False

    @staticmethod
    def _is_math_block(string: str) -> bool:
        if string.startswith("$$"):
            return True
        return False

    @staticmethod
    def _is_html_comment(string: str) -> bool:
        if string.startswith("<!--"):
            return True
        return False

    @staticmethod
    def _replace_cloze_id_with_unique(string: str, selected_cloze: str | None = None) -> str:
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
            output_hash = int(hashlib.sha256(cloze.encode("utf-8")).hexdigest(), 16) % 10**3

            new_cloze = f"{{{{c{output_hash}::{cloze[1:-1]}}}}}"

            string = string.replace(cloze, new_cloze)

        return string

    def extract_prompts(self, document: Document) -> Sequence[ClozePrompt]:
        prompts: list[ClozeFromDoc] = []
        blocks = self._get_blocks(document.content)

        block_starting_line_nr = 1
        for block_string in blocks:
            if any(
                exclusion_criterion(block_string)
                for exclusion_criterion in (self._is_html_comment, self._is_math_block)
            ):
                continue

            if self._has_cloze(block_string):
                clozes = re.findall(r"{(?!BearID).[^}]*}", block_string)

                for selected_cloze in clozes:
                    prompt_content = self._replace_cloze_id_with_unique(
                        block_string, selected_cloze=selected_cloze
                    )

                    prompts.append(
                        ClozeFromDoc(
                            text=prompt_content, parent_doc=document, line_nr=block_starting_line_nr
                        )
                    )

            n_block_lines = len(re.findall(r"\n", block_string, flags=re.DOTALL))
            block_starting_line_nr += n_block_lines

        return prompts
