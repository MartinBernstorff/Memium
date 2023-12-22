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
        return list(re.findall(r"#[\w\/]+", self.content))

    @property
    def title(self) -> str:
        return self.source_path.stem
