from pathlib import Path

DOIT_CONFIG = {"backend": "json", "dep_file": "doit-db.json"}

code_files = [Path("pyproject.toml"), Path("uv.lock")] + [
    p for p in Path("memium").rglob("*") if not p.is_dir()
]


def github_signoff(name: str) -> str:
    return f'~/Git/dotfiles/scripts/signoff.sh $PWD "{name}"'


def task_types():
    return {"actions": ["uv run pyright memium"], "file_dep": code_files}


def task_test():
    return {"actions": ["uv run pytest memium"], "file_dep": code_files}


def task_lint():
    return {"actions": ["ruff check memium --fix"], "file_dep": code_files}


def task_validate():
    return {
        "actions": ["git push", github_signoff("local/mergeable")],
        "task_dep": ["lint", "types", "test"],
    }


dockerfiles = list(Path().rglob("**/Dockerfile*"))


def task_image():
    return {
        "actions": ["docker build . -t ghcr.io/martinbernstorff/memium:latest -f Dockerfile"],
        "file_dep": code_files + dockerfiles,
    }


def task_run_image():
    return {
        "actions": ["docker compose -f ~/Git/dotfiles/containers/memium/docker-compose.yml up -d"],
        "task_dep": ["image", "validate"],
        "file_dep": code_files + dockerfiles,
    }
