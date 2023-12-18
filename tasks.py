import invoke as inv

SRC_PATH = "personal_mnemonic_medium"
PYTEST_CMD = "pytest --durations=5 --cov=personal_mnemonic_medium personal_mnemonic_medium --cov-report xml:.coverage.xml --cov-report lcov:.coverage.lcov"


@inv.task  # type: ignore
def install_dev(c: inv.Context):
    print("--- Installing development dependencies ---")
    c.run("pip install --upgrade .[dev]")
    print("✅✅✅ Development dependencies installed ✅✅✅")


@inv.task  # type: ignore
def install_test(c: inv.Context):
    print("--- Installing development dependencies ---")
    c.run("pip install --upgrade .[dev,tests]")
    print("✅✅✅ Development dependencies installed ✅✅✅")


@inv.task  # type: ignore
def install(c: inv.Context):
    print("--- Installing dependencies ---")
    c.run("pip install --upgrade .")
    print("✅✅✅ Installed package ✅✅✅")


@inv.task  # type: ignore
def generate_coverage(c: inv.Context):
    c.run(PYTEST_CMD)


@inv.task  # type: ignore
def test(c: inv.Context):
    print("--- Testing ---")
    generate_coverage(c)
    c.run("diff-cover .coverage.xml --fail-under=80")
    print("✅✅✅ Tests passed ✅✅✅")


@inv.task  # type: ignore
def lint(c: inv.Context):
    print("--- Linting ---")
    c.run("ruff format .")
    c.run("ruff . --fix --extend-select F401 --extend-select F841")
    print("✅✅✅ Lint ✅✅✅")


@inv.task  # type: ignore
def types(c: inv.Context):
    print("--- Type-checking ---")
    c.run(f"pyright {SRC_PATH}")
    print("✅✅✅ Types ✅✅✅")
