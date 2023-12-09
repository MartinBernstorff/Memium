from collections.abc import Sequence
from dataclasses import dataclass

from personal_mnemonic_medium.v2.domain.prompts.doc_mixin import (
    DocMixin,
)

from ..int_hash_str import int_hash_str
from .base_prompt import BasePrompt


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
class ClozePromptWithoutDoc(ClozePrompt):
    add_tags: Sequence[str]

    @property
    def tags(self) -> Sequence[str]:
        return self.add_tags


class ClozePromptFromDoc(ClozePrompt, DocMixin):
    ...
