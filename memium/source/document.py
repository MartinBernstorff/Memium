import re
from collections.abc import Sequence
from dataclasses import dataclass, replace
from pathlib import Path


@dataclass(frozen=True)
class Document:
    content: str
    source_path: Path
    # Optional, since prompts cached before vaults were modelled deserialise into this
    vault_name: str | None = None

    @staticmethod
    def dummy(
        content: str | None = None,
        source_path: Path = Path("DummyPath"),
        tags: Sequence[str] = (),
        vault_name: str | None = "DummyVault",
    ) -> "Document":
        return Document(
            content=content
            if content is not None
            else "dummy content with tags: " + ", ".join(f"#{tag}" for tag in tags),
            source_path=source_path,
            vault_name=vault_name,
        )

    def with_tags(self, tags: Sequence[str]) -> "Document":
        content_with_tags = self.content + "\n\n\n" + " ".join(f"#{tag}" for tag in tags)
        return replace(self, content=content_with_tags)

    @property
    def tags(self) -> Sequence[str]:
        tag_strings: list[str] = list(re.findall(r"#[\w\/]+", self.content))
        return [tag_string.replace("#", "") for tag_string in tag_strings]

    @property
    def title(self) -> str:
        return self.source_path.stem

    def __repr__(self) -> str:
        return f"{self.title}: {self.content[0:10]}..."
