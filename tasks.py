import json
from collections.abc import Sequence

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


from dataclasses import dataclass


@dataclass(frozen=True)
class GithubIssue:
    number: int
    title: str


def sanitise_issue_title(issue_title: str) -> str:
    characters_to_replace = [
        " ",
        ":",
        ",",
        "'",
        '"',
        "(",
        ")",
        "[",
        "]",
    ]

    for character in characters_to_replace:
        issue_title = issue_title.replace(character, "-")

    issue_title = issue_title.replace("--", "-")
    return issue_title


@inv.task(aliases=("next",))  # type: ignore
def select_next_issue(c: inv.Context):
    my_issues = get_issues_assigned_to_me(c)

    if my_issues is None:
        print("No issues found")
        return

    terminal_output = "\n".join(
        f"[{i+1}] {issue.title} #{issue.number}"
        for i, issue in enumerate(my_issues)
    )
    print(f"{terminal_output}\n")

    issue_index = (
        int(
            input(
                f"Which issue do you want to work on? [1-{len(my_issues)}]\n"
            )
        )
        - 1
    )
    selected_issue = my_issues[issue_index]
    sanitised_title = sanitise_issue_title(selected_issue.title)

    branch_title = f"{selected_issue.number}-{sanitised_title}"
    c.run(f"gt create {branch_title}")
    c.run(
        f"git commit --allow-empty -m 'Fixes #{selected_issue.number}'"
    )


@inv.task(aliases=("submit",))  # type: ignore
def submit_pr(c: inv.Context):
    c.run("gt submit --restack -m --no-edit")


def get_issues_assigned_to_me(
    c: inv.Context
) -> Sequence[GithubIssue] | None:
    """Get issues assigned to current user on current repo"""
    my_issues = c.run(
        "gh issue list --assignee='@me' --json number,title",
        hide=True,
    )
    if my_issues is None:
        return None

    output = my_issues.stdout
    parsed_output = [
        GithubIssue(**value) for value in json.loads(output)
    ]
    return parsed_output


@inv.task  # type: ignore
def validate_ci(c: inv.Context):
    print("--- Validating CI ---")
    lint(c)
    types(c)
    generate_coverage(c)
    print("✅✅✅ CI valid ✅✅✅")
