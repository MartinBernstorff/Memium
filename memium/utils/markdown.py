import re
from collections.abc import Sequence
from typing import Protocol

from markdown import Markdown


class MarkdownParser(Protocol):
    def __call__(self, markdown: str) -> str: ...


def md_to_html(markdown: str) -> str:
    return Markdown(
        output_format="html", extensions=["legacy_em", "fenced_code", "tables", "nl2br"]
    ).convert(markdown)


def get_terms_surrounded_by_underscores(string: str) -> Sequence[str]:
    wikilinks = re.findall(r"_[\w\s\(\)]+?_", string)
    return [link.replace("_", "") for link in wikilinks]
