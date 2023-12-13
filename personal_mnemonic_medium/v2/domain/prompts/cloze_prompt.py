from collections.abc import Sequence
from dataclasses import dataclass

from ..prompt_source.document_ingesters.document import Document
from ..utils.int_hash_str import int_hash_str
from .base_prompt import BasePrompt

# TODO: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues/299 refactor: clean up doc type inheritance


@dataclass(frozen=True)
class ClozePrompt(BasePrompt):
    text: str

    @property
    def uid(self) -> int:
        return int_hash_str(self.text)

    @property
    def tags(self) -> Sequence[str]:
        return ()


@dataclass(frozen=True)
class ClozeWithoutDoc(ClozePrompt):
    remote_id: str
    add_tags: Sequence[str]

    @property
    def tags(self) -> Sequence[str]:
        return self.add_tags


@dataclass(frozen=True)
class ClozeFromDoc(ClozePrompt):
    text: str
    source_doc: Document

    @property
    def uid(self) -> int:
        return int_hash_str(self.text)

    @property
    def tags(self) -> Sequence[str]:
        return self.source_doc.tags
