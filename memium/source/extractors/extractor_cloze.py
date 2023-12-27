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
        return re.split(r"(\n\n)+", string)

    @staticmethod
    def _has_cloze(string: str) -> bool:
        if (
            len(re.findall(r"{.*}", string)) > 0
            and "BearID" not in string  # Exclude BearID
            and "$$" not in string  # Exclude math
            and r"```" not in string  # Exclude code
            and "Q." not in string  # Exclude Q&A
            and "A." not in string  # Exclude Q&A
        ):
            return True
        return False

    @staticmethod
    def _is_code_block(string: str) -> bool:
        if string.startswith("```"):
            return True
        return False

    @staticmethod
    def _is_html_comment(string: str) -> bool:
        if string.startswith("<!--"):
            return True
        return False

    @staticmethod
    def _replace_cloze_id_with_unique(
        string: str, selected_cloze: str | None = None
    ) -> str:
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
            output_hash = (
                int(hashlib.sha256(cloze.encode("utf-8")).hexdigest(), 16)
                % 10**3
            )

            new_cloze = f"{{{{c{output_hash}::{cloze[1:-1]}}}}}"

            string = string.replace(cloze, new_cloze)

        return string

    def extract_prompts(self, document: Document) -> Sequence[ClozePrompt]:
        prompts: list[ClozeFromDoc] = []
        blocks = self._get_blocks(document.content)

        for block_string in blocks:
            if self._is_code_block(block_string) or self._is_html_comment(
                block_string
            ):
                continue
            if self._has_cloze(block_string):
                clozes = re.findall(r"{(?!BearID).[^}]*}", block_string)

                for selected_cloze in clozes:
                    prompt_content = self._replace_cloze_id_with_unique(
                        block_string, selected_cloze=selected_cloze
                    )

                    prompts.append(
                        ClozeFromDoc(text=prompt_content, source_doc=document)
                    )

        return prompts
