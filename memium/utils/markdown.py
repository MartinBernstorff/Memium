import re
from collections.abc import Sequence
from typing import NewType

from markdown import Markdown as MDLibMarkdown

Markdown = NewType("Markdown", str)


def md_to_html(markdown: Markdown) -> Markdown:
    return Markdown(
        MDLibMarkdown(
            output_format="html", extensions=["legacy_em", "fenced_code", "tables", "nl2br"]
        ).convert(markdown)
    )


def get_terms_surrounded_by_underscores(string: str) -> Sequence[str]:
    wikilinks = re.findall(r"_[\w\s\(\)]+?_", string)
    return [link.replace("_", "") for link in wikilinks]
