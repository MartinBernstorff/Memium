import invoke as inv

from tasks.github import get_issues_assigned_to_me, issue_dialog
from tasks.graphite import create_branch_from_issue

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


@inv.task(aliases=("next",))  # type: ignore
def branch_from_next_issue(c: inv.Context):
    my_issues = get_issues_assigned_to_me(c)

    if my_issues is None:
        print("No issues found")
        return

    selected_issue_index = issue_dialog(my_issues)
    create_branch_from_issue(
        c=c, selected_issue=my_issues[selected_issue_index]
    )


@inv.task  # type: ignore
def validate_ci(c: inv.Context):
    print("--- Validating CI ---")
    lint(c)
    types(c)
    generate_coverage(c)
    print("✅✅✅ CI valid ✅✅✅")


@inv.task(aliases=("new",))  # type: ignore
def new_branch_from_issue(c: inv.Context):
    my_issues = get_issues_assigned_to_me(c)

    if my_issues is None:
        print("No issues found")
        return

    selected_issue_index = issue_dialog(my_issues)
    c.run("git checkout main")
    c.run("git pull")
    create_branch_from_issue(
        c=c, selected_issue=my_issues[selected_issue_index]
    )
