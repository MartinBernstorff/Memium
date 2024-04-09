import re
from collections.abc import Sequence


def get_wikilinks_from_string(string: str) -> Sequence[str]:
    wikilinks = re.findall(r"\[\[[\w\s\|\(\)]+\]\]", string)
    without_alias = [re.sub(r"\|[\w|\s|\d]+\]\]", "]]", link) for link in wikilinks]
    contents = [link.replace("[[", "").replace("]]", "") for link in without_alias]
    return contents
