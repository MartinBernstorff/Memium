from typing import Protocol

from markdown import Markdown


class MarkdownParser(Protocol):
    def __call__(self, markdown: str) -> str: ...


def markdown_parser(markdown: str) -> str:
    return Markdown(
        output_format="html", extensions=["legacy_em", "fenced_code", "tables", "nl2br"]
    ).convert(markdown)
