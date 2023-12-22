from collections.abc import Sequence
from pathlib import Path

from tqdm import tqdm

from .ingester_base import BaseDocumentIngester
from .document import Document


class MarkdownDocumentIngester(BaseDocumentIngester):
    def __init__(self, directory: Path) -> None:
        self.directory = directory

    def get_note_from_file(self, file_path: Path) -> Document:
        with file_path.open(encoding="utf8") as f:
            file_contents = f.read()

            return Document(
                content=file_contents, source_path=file_path
            )

    def get_documents(self) -> Sequence[Document]:
        md_files = list(self.directory.rglob("*.md"))

        notes: list[Document] = []
        with tqdm(total=len(md_files)) as pbar:
            for filepath in md_files:
                notes.append(self.get_note_from_file(filepath))
                pbar.update(1)

        return notes
