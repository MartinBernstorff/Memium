from collections.abc import Sequence
from dataclasses import dataclass

from ...utils.hash_cleaned_str import clean_str, hash_str_to_int
from .prompt import BasePrompt
from .prompt_from_doc import PromptFromDocMixin


@dataclass(frozen=True)
class ClozePrompt(BasePrompt):
    text: str

    @property
    def scheduling_uid(self) -> int:
        return hash_str_to_int(clean_str(self.text))

    @property
    def update_uid(self) -> int:
        return hash_str_to_int(f"{(self.text)}{self.tags}")

    @property
    def tags(self) -> Sequence[str]:
        return ()


@dataclass(frozen=True)
class ClozeWithoutDoc(ClozePrompt):
    add_tags: Sequence[str]

    @property
    def tags(self) -> Sequence[str]:
        return self.add_tags

    @property
    def edit_url(self) -> str | None:
        return None


@dataclass(frozen=True)
class ClozeFromDoc(ClozePrompt, PromptFromDocMixin):
    text: str

    @property
    def tags(self) -> Sequence[str]:
        return self.parent_doc.tags
