def task_types():
    return {"actions": ["uv run pyright memium"], "verbosity": 2}


def task_test():
    return {"actions": ["uv run pytest memium"], "verbosity": 2}


def task_image():
    return {
        "actions": ["docker build . -t ghcr.io/martinbernstorff/memium:latest -f Dockerfile"],
        "verbosity": 2,
    }


def task_lint():
    return {"actions": ["ruff check memium --fix"], "verbosity": 2}


def task_validate():
    return {"actions": ["test", "types", "lint"], "verbosity": 2}


def task_run_image():
    return {
        "actions": ["docker compose -f ~/Git/dotfiles/containers/memium/docker-compose.yml up -d"],
        "task_dep": ["image", "validate"],
        "verbosity": 2,
    }


def task_deploy():
    return {"actions": None, "task_dep": ["run_image"], "verbosity": 2}
