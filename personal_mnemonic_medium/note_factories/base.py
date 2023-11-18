from abc import ABC, abstractmethod
from collections.abc import Sequence
from pathlib import Path

from personal_mnemonic_medium.note_factories.note import Document


class DocumentFactory(ABC):
    @abstractmethod
    def get_notes_from_dir(
        self, dir_path: Path
    ) -> Sequence[Document]:
        pass

    @abstractmethod
    def get_note_from_file(self, file_path: Path) -> Document:
        pass
