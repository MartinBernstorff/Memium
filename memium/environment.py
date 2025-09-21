from pathlib import Path


def in_docker() -> bool:
    return Path("/.dockerenv").exists()
