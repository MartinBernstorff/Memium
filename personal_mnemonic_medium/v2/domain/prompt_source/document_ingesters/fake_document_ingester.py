from collections.abc import Sequence

from ..document_ingesters.document import Document
from .base_document_ingester import BaseDocumentIngester


class FakeDocumentIngester(BaseDocumentIngester):
    def __init__(self, documents: Sequence[Document]):
        self.documents = documents

    def get_documents(self) -> Sequence[Document]:
        return self.documents
