from pathlib import Path

code_files = (
    list(Path().rglob("*.toml"))
    + list(Path().rglob("*.lock"))
    + [p for p in Path("memium").rglob("*") if not p.is_dir()]
)


def task_types():
    return {"actions": ["uv run pyright memium"], "file_dep": code_files, "verbosity": 2}


def task_test():
    return {"actions": ["uv run pytest memium"], "file_dep": code_files, "verbosity": 2}


def task_lint():
    return {"actions": ["ruff check memium --fix"], "file_dep": code_files, "verbosity": 2}


def task_validate():
    return {
        "actions": ["echo ✅✅✅ All OK ✅✅✅"],
        "task_dep": ["lint", "types", "test"],
        "verbosity": 2,
    }


dockerfiles = list(Path().rglob("**/Dockerfile*"))


def task_image():
    return {
        "actions": ["docker build . -t ghcr.io/martinbernstorff/memium:latest -f Dockerfile"],
        "verbosity": 2,
        "file_dep": code_files + dockerfiles,
    }


def task_run_image():
    return {
        "actions": ["docker compose -f ~/Git/dotfiles/containers/memium/docker-compose.yml up -d"],
        "task_dep": ["image", "validate"],
        "file_dep": code_files + dockerfiles,
        "verbosity": 2,
    }


def task_deploy():
    return {"actions": None, "task_dep": ["run_image"], "verbosity": 2}
