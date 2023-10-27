import os
import re
from collections.abc import Sequence
from pathlib import Path

from tqdm import tqdm

from personal_mnemonic_medium.note_factories.base import (
    DocumentFactory,
)
from personal_mnemonic_medium.note_factories.note import Document


class MarkdownNoteFactory(DocumentFactory):
    def __init__(self, cut_note_after: str = "# Backlinks"):
        """Create a new MarkdownNoteFactory.

        Args:
            cut_note_after: Cut everything in the note after this string.
        """
        self.cut_note_after = cut_note_after

    def get_and_append_new_uuid(self, file_path: Path) -> str:
        guid = os.urandom(32).hex()[0:32]

        with file_path.open("a", encoding="utf8") as f:
            f.write("\n")
            f.write("<!-- {BearID:" + guid + "} -->")

        return guid

    def get_note_id(self, file_string: str) -> str:
        return re.findall(r"<!-- {BearID:.+", file_string)[0]

    def get_note_from_file(self, file_path: Path) -> Document:
        with file_path.open(encoding="utf8") as f:
            file_contents = f.read()

            try:
                uuid = self.get_note_id(file_contents)
            except IndexError:
                uuid = self.get_and_append_new_uuid(file_path)

            note_title = file_path.stem

            if self.cut_note_after in file_contents:
                file_contents = file_contents.split(
                    self.cut_note_after
                )[0]

            return Document(
                title=note_title,
                content=file_contents,
                uuid=uuid,
                source_path=file_path,
            )

    def get_notes_from_dir(
        self, dir_path: Path
    ) -> Sequence[Document]:
        notes: list[Document] = []

        for parent_dir, _, files in os.walk(dir_path):
            md_files = list(filter(self.is_markdown_file, files))
            if not md_files:
                continue

            with tqdm(total=len(md_files)) as pbar:
                for file_name in sorted(md_files):
                    file_path = Path(parent_dir) / file_name
                    note = self.get_note_from_file(file_path)

                    notes.append(note)
                    pbar.update(1)

        return notes

    def is_markdown_file(self, string: str) -> bool:
        return string.endswith((".md", ".markdown"))
