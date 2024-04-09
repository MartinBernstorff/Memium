import re
from collections.abc import Sequence


def get_terms_surrounded_by_underscores(string: str) -> Sequence[str]:
    wikilinks = re.findall(r"_[\w\s\(\)]+?_", string)
    return [link.replace("_", "") for link in wikilinks]
