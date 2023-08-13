import urllib
from pathlib import Path


def get_1writer_uri(source_path: Path) -> str:
    """Get the obsidian URI for the source document."""
    directory = urllib.parse.quote("/iCloud/Life Lessons iCloud")  # type: ignore
    file = urllib.parse.quote(source_path.name)  # type: ignore
    full_path = urllib.parse.quote(f"{directory}/{file}")  # type: ignore

    href = f"onewriter:://x-callback-url/open?path={full_path}"
    return href
