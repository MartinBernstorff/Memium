import logging
import re
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from tqdm import tqdm

from .document import Document

log = logging.getLogger(__name__)


@dataclass(frozen=True)
class FileNotRetrievedError(Exception):
    path: Path
    error: Exception


class BaseDocumentSource(Protocol):
    def get_documents(self) -> Sequence[Document]:
        ...


class MarkdownDocumentSource(BaseDocumentSource):
    """Gets markdown documents. Returns valid markdown."""

    def __init__(self, directory: Path) -> None:
        self.directory = directory

    def _replace_wikilinks_with_styling(self, input_str: str) -> str:
        return input_str.replace("[[", "_").replace("]]", "_")

    @staticmethod
    def _replace_alias_wiki_links(text: str) -> str:
        regex_pattern = r"\[\[[\w|\s|\d|\(|\)]+\|[\w|\s|\d]+\]\]"
        pattern_matches = re.findall(
            pattern=regex_pattern, string=text, flags=re.DOTALL
        )

        for match in pattern_matches:
            link_name = (
                re.findall(pattern=r"\|[\w|\s|\d]+\]\]", string=match)[0]
                .replace("|", "")
                .replace("]", "")
                .strip()
            )
            replacement_str = f"[[{link_name}]]"
            text = text.replace(match, replacement_str)

        return text

    def _sanitize_to_valid_markdown(self, input_str: str) -> str:
        aliases_handled = self._replace_alias_wiki_links(input_str)
        wikilinks_replaced = self._replace_wikilinks_with_styling(
            aliases_handled
        )
        return wikilinks_replaced

    def _get_document_from_file(
        self, file_path: Path
    ) -> Document | FileNotRetrievedError:
        try:
            with file_path.open("r", encoding="utf8") as f:
                return Document(
                    content=self._sanitize_to_valid_markdown(f.read()),
                    source_path=file_path,
                )
        except Exception as e:
            log.warning(f"Could not retrieve {file_path}: {e}")
            return FileNotRetrievedError(file_path, e)

    def get_documents(self) -> Sequence[Document]:
        md_files = list(self.directory.rglob("*.md"))

        notes: list[Document | FileNotRetrievedError] = []

        with tqdm(total=len(md_files)) as pbar:
            for filepath in md_files:
                notes.append(self._get_document_from_file(filepath))
                pbar.update(1)

        return [
            note
            for note in notes
            if not isinstance(note, FileNotRetrievedError)
        ]
