from collections.abc import Sequence
from dataclasses import dataclass

from ....data_access.document_ingesters.document import Document


@dataclass(frozen=True)
class DocMixin:
    parent_doc: Document
    line_nr: int

    @property
    def tags(self) -> Sequence[str]:
        return self.parent_doc.tags
