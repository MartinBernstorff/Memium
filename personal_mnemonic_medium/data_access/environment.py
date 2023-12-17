import os
from pathlib import Path


def get_env(default: str) -> str:
    if os.getenv("GITHUB_ACTIONS"):
        return "GITHUB_ACTIONS"
    return os.getenv("ENV", default)


def get_host_home_dir() -> Path:
    host_home_dir = os.getenv("HOST_HOME")
    home_dir = os.getenv("HOME", ".")
    return Path(host_home_dir) if host_home_dir else Path(home_dir)
