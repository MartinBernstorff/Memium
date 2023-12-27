import urllib.parse
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from ..source.prompts.prompt import BasePrompt
from ..source.prompts.prompt_cloze import ClozeFromDoc
from ..source.prompts.prompt_qa import QAFromDoc


class ExtraGenerator(Protocol):
    def __call__(self, prompt: BasePrompt) -> str:
        ...


@dataclass(frozen=True)
class ObsidianURIGenerator(ExtraGenerator):
    vault: Path

    def __call__(self, prompt: BasePrompt) -> str:
        if not isinstance(prompt, QAFromDoc | ClozeFromDoc):
            return ""

        vault = urllib.parse.quote(str(self.vault))  # type: ignore
        file = urllib.parse.quote(prompt.source_doc)  # type: ignore

        href = f"obsidian://advanced-uri?vault={vault}&filepath={file}&line={prompt.line_nr}"

        return f'<h4 class="right"><a href="{href}">Open</a></h4>'
