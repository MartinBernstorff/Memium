from collections.abc import Sequence
from typing import Protocol

from .document import Document


class BaseDocumentIngester(Protocol):
    def get_documents(self) -> Sequence[Document]:
        ...
