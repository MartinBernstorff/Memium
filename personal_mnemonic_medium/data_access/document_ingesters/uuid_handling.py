import logging
import os
import re
from collections.abc import Callable
from pathlib import Path

log = logging.getLogger(__name__)


def generate_bear_guid() -> str:  # pragma: no cover
    return "<!-- {BearID:" + os.urandom(32).hex()[0:32] + "} -->"


def extract_bear_guid(file_contents: str) -> str:
    matches = re.findall(r"<!-- {BearID:.+? -->", file_contents)

    if not len(matches) == 1:
        raise IndexError(
            "Could not find exactly one BearID in file contents."
        )

    return matches[0]


def append_guid(
    file_path: Path, uuid_generator: Callable[[], str]
) -> str:
    guid_str = uuid_generator()

    log.info(f"{file_path}: appending {guid_str}")

    with file_path.open("a", encoding="utf8") as f:
        f.write("\n")
        f.write(guid_str)

    return guid_str
