import re
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Document:
    content: str
    source_path: Path

    @staticmethod
    def dummy(
        content: str | None = None, source_path: Path = Path("DummyPath"), tags: Sequence[str] = ()
    ) -> "Document":
        return Document(
            content=content
            if content is not None
            else "dummy content with tags: " + ", ".join(f"#{tag}" for tag in tags),
            source_path=source_path,
        )

    @property
    def tags(self) -> Sequence[str]:
        tag_strings: list[str] = list(re.findall(r"#[\w\/]+", self.content))
        return [tag_string.replace("#", "") for tag_string in tag_strings]

    @property
    def title(self) -> str:
        return self.source_path.stem

    def __repr__(self) -> str:
        return f"{self.title}: {self.content[0:10]}..."


@dataclass(frozen=True)
class DummyDocument(Document):
    content: str = "dummy content"
    source_path: Path = Path("dummy_path")
