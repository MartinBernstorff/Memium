import urllib
from pathlib import Path


def get_obsidian_url(
    source_path: Path, line_nr: int | None = None
) -> str:
    """Get the obsidian URI for the source document."""
    vault: str = urllib.parse.quote(source_path.parent.name)  # type: ignore
    file: str = urllib.parse.quote(source_path.name)  # type: ignore

    href = f"obsidian://advanced-uri?vault={vault}&filepath={file}"

    if line_nr is not None:
        href += f"&line={line_nr}"

    return f'<h4 class="right"><a href="{href}">Open</a></h4>'
