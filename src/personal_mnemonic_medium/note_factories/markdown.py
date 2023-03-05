import os
import re
from pathlib import Path
from typing import List, Optional

from tqdm import tqdm

from personal_mnemonic_medium.note_factories.note import Note


class MarkdownNoteFactory:
    def __init__(self, cut_note_after: str = "# Backlinks"):
        """Create a new MarkdownNoteFactory.

        Args:
            cut_note_after: Cut everything in the note after this string.
        """
        self.cut_note_after = cut_note_after

    def append_new_uuid_to_file(self, file_path: Path):
        guid = os.urandom(32).hex()

        with open(file_path, "a", encoding="utf8") as f:
            f.write("\n")
            f.write("<!-- {BearID:" + guid + "} -->")

        return guid

    def get_bear_id(self, file_string: str) -> str:
        return re.findall(r"BearID:.+", file_string)[0]

    def get_note_from_file(self, file_path: Path) -> Optional[Note]:
        with open(file_path, "r", encoding="utf8") as f:
            file_contents = f.read()

            try:
                uuid = self.get_bear_id(file_contents)
            except IndexError:
                uuid = self.append_new_uuid_to_file(file_path)

            note_title = file_path.stem

            if self.cut_note_after in file_contents:
                file_contents = file_contents.split(self.cut_note_after)[0]

            return Note(title=note_title, content=file_contents, uuid=uuid)

    def get_notes_from_dir(self, dir_path: Path) -> List[Note]:
        notes = []

        for parent_dir, _, files in os.walk(dir_path):
            with tqdm(total=len(files)) as pbar:
                for file_name in sorted(files):
                    if file_name.endswith(".md") or file_name.endswith(".markdown"):
                        file_path = Path(os.path.join(parent_dir, file_name))

                        note = self.get_note_from_file(file_path)

                        if note is not None:
                            notes.append(note)

                        pbar.update(1)

        return notes
