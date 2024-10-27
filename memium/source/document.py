import re
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Document:
    content: str
    source_path: Path

    @property
    def tags(self) -> Sequence[str]:
        tag_strings: list[str] = list(re.findall(r"#[\w\/]+", self.content))
        return [tag_string.replace("#", "") for tag_string in tag_strings]

    @property
    def title(self) -> str:
        return self.source_path.stem

    def __repr__(self) -> str:
        return f"{self.title}: {self.content[0:10]}..."
