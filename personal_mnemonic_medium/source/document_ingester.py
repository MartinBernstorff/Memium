import logging
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


class BaseDocumentIngester(Protocol):
    def get_documents(self) -> Sequence[Document]:
        ...


class MarkdownDocumentIngester(BaseDocumentIngester):
    def __init__(self, directory: Path) -> None:
        self.directory = directory

    def _get_note_from_file(
        self, file_path: Path
    ) -> Document | FileNotRetrievedError:
        try:
            with file_path.open("r", encoding="utf8") as f:
                return Document(content=f.read(), source_path=file_path)
        except Exception as e:
            log.warning(f"Could not retrieve {file_path}: {e}")
            return FileNotRetrievedError(file_path, e)

    def get_documents(self) -> Sequence[Document]:
        md_files = list(self.directory.rglob("*.md"))

        notes: list[Document | FileNotRetrievedError] = []

        with tqdm(total=len(md_files)) as pbar:
            for filepath in md_files:
                notes.append(self._get_note_from_file(filepath))
                pbar.update(1)

        return [
            note
            for note in notes
            if not isinstance(note, FileNotRetrievedError)
        ]
