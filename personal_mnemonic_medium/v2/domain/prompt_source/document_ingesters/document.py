import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Document:
    content: str
    source_path: Path


@dataclass(frozen=True)
class MarkdownDocument(Document):
    content: str
    source_path: Path

    @property
    def title(self) -> str:
        return self.source_path.stem

    @property
    def tags(self) -> list[str]:
        return list(re.findall(r"#anki\/tag\/\S+", self.content))
