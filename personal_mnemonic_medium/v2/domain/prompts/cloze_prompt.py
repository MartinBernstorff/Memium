from collections.abc import Sequence
from dataclasses import dataclass

from ..prompt_source.document_ingesters.document import Document
from ..utils.clean_str import hash_cleaned_str
from ..utils.int_hash_str import int_hash_str
from .base_prompt import BasePrompt

# TODO: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues/299 refactor: clean up doc type inheritance


@dataclass(frozen=True)
class ClozePrompt(BasePrompt):
    text: str
    manual_tags: Sequence[str]

    @property
    def uid(self) -> int:
        return int_hash_str(self.text)

    @property
    def tags(self) -> Sequence[str]:
        return self.manual_tags


@dataclass(frozen=True)
class ClozeFromDoc(ClozePrompt):
    text: str
    source_doc: Document
    manual_tags: Sequence[str] = ()  # A bit hacky to have

    @property
    def uid(self) -> int:
        return hash_cleaned_str(self.text)

    @property
    def tags(self) -> Sequence[str]:
        return self.source_doc.tags


@dataclass(frozen=True)
class FakeClozePrompt(ClozePrompt):
    text: str = "FakeText"
    manual_tags: Sequence[str] = ("FakeTag",)
