from collections.abc import Sequence

from .document import Document
from .ingester_base import BaseDocumentIngester


class FakeDocumentIngester(BaseDocumentIngester):
    def __init__(self, documents: Sequence[Document]):
        self.documents = documents

    def get_documents(self) -> Sequence[Document]:
        return self.documents
