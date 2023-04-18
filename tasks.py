"""
This project uses Invoke (pyinvoke.org) for task management.
Install it via:

```
pip install invoke
```

And then run:

```
inv --list
```

If you do not wish to use invoke you can simply delete this file.
"""


import platform
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from invoke import Context, Result, task

NOT_WINDOWS = platform.system() != "Windows"


def echo_header(msg: str):
    print(f"\n--- {msg} ---")


@dataclass
class Msg:
    DOING = "DOING:"
    GOOD = "DONE:"
    FAIL = "FAILED:"
    WARN = "WARNING:"
    SYNC = "SYNCING:"
    PY = ""
    CLEAN = "CLEANING:"
    TEST = "TESTING:"
    COMMUNICATE = "COMMUNICATING:"
    EXAMINE = "VIEWING:"


def git_init(c: Context, branch: str = "main"):
    """Initialize a git repository if it does not exist yet."""
    # If no .git directory exits
    if not Path(".git").exists():
        echo_header(f"{Msg.DOING} Initializing Git repository")
        c.run(f"git init -b {branch}")
        c.run("git add .")
        c.run("git commit -m 'Init'")
        print(f"{Msg.GOOD} Git repository initialized")
    else:
        print(f"{Msg.GOOD} Git repository already initialized")


def setup_venv(
    c: Context,
    python_version: str,
) -> Optional[str]:
    venv_name = f'.venv{python_version.replace(".", "")}'

    if not Path(venv_name).exists():
        if NOT_WINDOWS:
            echo_header(
                f"{Msg.DOING} Creating virtual environment for {python_version}{Msg.PY}",
            )
            c.run(f"python{python_version} -m venv {venv_name}")
            print(f"{Msg.GOOD} Virtual environment created")
            return venv_name

        # Getting at the correct python executable is a bit of a pain on Windows,
        # so we'll just skip this step for now.
        print(f"{Msg.WARN} Virtual environment creation not supported on Windows")
        return None

    print(f"{Msg.GOOD} Virtual environment already exists")
    return None


def _add_commit(c: Context, msg: Optional[str] = None):
    print("🔨 Adding and committing changes")
    c.run("git add .")

    if msg is None:
        msg = input("Commit message: ")

    c.run(f'git commit -m "{msg}"', pty=NOT_WINDOWS, hide=True)
    print("\n🤖 Changes added and committed\n")


def is_uncommitted_changes(c: Context) -> bool:
    git_status_result: Result = c.run(
        "git status --porcelain",
        pty=NOT_WINDOWS,
        hide=True,
    )

    uncommitted_changes = git_status_result.stdout != ""
    return uncommitted_changes


def add_and_commit(c: Context, msg: Optional[str] = None):
    """Add and commit all changes."""
    if is_uncommitted_changes(c):
        uncommitted_changes_descr = c.run(
            "git status --porcelain",
            pty=NOT_WINDOWS,
            hide=True,
        ).stdout

        echo_header(
            f"{Msg.WARN} Uncommitted changes detected",
        )

        for line in uncommitted_changes_descr.splitlines():
            print(f"    {line.strip()}")
        print("\n")
        _add_commit(c, msg=msg)


def branch_exists_on_remote(c: Context) -> bool:
    branch_name = Path(".git/HEAD").read_text().split("/")[-1].strip()

    branch_exists_result: Result = c.run(
        f"git ls-remote --heads origin {branch_name}",
        hide=True,
    )

    return branch_name in branch_exists_result.stdout


def update_branch(c: Context):
    echo_header(f"{Msg.SYNC} Syncing branch with remote")

    if not branch_exists_on_remote(c):
        c.run("git push --set-upstream origin HEAD")
    else:
        print("Pulling")
        c.run("git pull")
        print("Pushing")
        c.run("git push")


def create_pr(c: Context):
    c.run(
        "gh pr create --web",
        pty=NOT_WINDOWS,
    )


def update_pr(c: Context):
    echo_header(f"{Msg.COMMUNICATE} Syncing PR")
    # Get current branch name
    branch_name = Path(".git/HEAD").read_text().split("/")[-1].strip()
    pr_result: Result = c.run(
        "gh pr list --state OPEN",
        pty=False,
        hide=True,
    )

    if branch_name not in pr_result.stdout:
        create_pr(c)
    else:
        open_web = input("Open in browser? [y/n] ")
        if "y" in open_web.lower():
            c.run("gh pr view --web", pty=NOT_WINDOWS)


def exit_if_remaining_errors(result: Result):
    # Find N remaining using regex

    if "error" in result.stdout:
        errors_remaining = re.findall(r"\d+(?=( remaining))", result.stdout)[0]
        if errors_remaining != "0":
            exit(1)


def pre_commit(c: Context, auto_fix: bool):
    """Run pre-commit checks."""

    # Essential to have a clean working directory before pre-commit to avoid committing
    # heterogenous files under a "style: linting" commit
    if is_uncommitted_changes(c):
        print(
            f"{Msg.WARN} Your git working directory is not clean. Stash or commit before running pre-commit.",
        )
        exit(1)

    echo_header(f"{Msg.CLEAN} Running pre-commit checks")
    pre_commit_cmd = "pre-commit run --all-files"
    result = c.run(pre_commit_cmd, pty=NOT_WINDOWS, warn=True)

    exit_if_remaining_errors(result)

    if ("fixed" in result.stdout or "reformatted" in result.stdout) and auto_fix:
        _add_commit(c, msg="style: Auto-fixes from pre-commit")

        print(f"{Msg.DOING} Fixed errors, re-running pre-commit checks")
        second_result = c.run(pre_commit_cmd, pty=NOT_WINDOWS, warn=True)
        exit_if_remaining_errors(second_result)
    else:
        if result.return_code != 0:
            print(f"{Msg.FAIL} Pre-commit checks failed")
            exit(1)


def mypy(c: Context):
    echo_header(f"{Msg.CLEAN} Running mypy")
    c.run("mypy .", pty=NOT_WINDOWS)


@task
def install(c: Context, args: str = "", msg: bool = True):
    """Install the project in editable mode using pip install"""
    if msg:
        echo_header(f"{Msg.DOING} Installing project")

    if NOT_WINDOWS:
        c.run(f"pip install -e '.[dev,tests,docs]' {args}")
    else:
        c.run(f"pip install -e .[dev,tests,docs] {args}")


@task
def setup(c: Context, python_version: str = "3.9"):
    """Confirm that a git repo exists and setup a virtual environment."""
    git_init(c)

    venv_name = setup_venv(c, python_version=python_version)

    if venv_name is not None:
        print(
            f"{Msg.DOING} Activate your virtual environment by running: \n\n\t\t source {venv_name}/bin/activate \n",
        )
        print(
            f"{Msg.DOING} Then install the project by running: \n\n\t\t inv install\n",
        )


@task
def update(c: Context):
    """Update dependencies."""
    echo_header(f"{Msg.DOING} Updating project")
    install(c, args="--upgrade", msg=False)


@task
def test(c: Context):
    """Run tests"""
    echo_header(f"{Msg.TEST} Running tests")
    test_result: Result = c.run(
        "pytest tests/ -n auto -rfE --failed-first -p no:cov --disable-warnings -q",
        warn=True,
        pty=NOT_WINDOWS,
    )

    # If "failed" in the pytest results
    if "failed" in test_result.stdout:
        print("\n\n\n")
        echo_header("Failed tests")

        # Get lines with "FAILED" in them from the .pytest_results file
        failed_tests = [
            line for line in test_result.stdout if line.startswith("FAILED")
        ]

        for line in failed_tests:
            # Remove from start of line until /test_
            line_sans_prefix = line[line.find("test_") :]

            # Keep only that after ::
            line_sans_suffix = line_sans_prefix[line_sans_prefix.find("::") + 2 :]
            print(f"FAILED {Msg.FAIL} #{line_sans_suffix}     ")

    if test_result.return_code != 0:
        exit(0)


def test_for_rej():
    # Get all paths in current directory or subdirectories that end in .rej
    rej_files = list(Path(".").rglob("*.rej"))

    if len(rej_files) > 0:
        print(f"\n{Msg.FAIL} Found .rej files leftover from cruft update.\n")
        for file in rej_files:
            print(f"    /{file}")
        print("\nResolve the conflicts and try again. \n")
        exit(1)


@task
def lint(c: Context, auto_fix: bool = False):
    """Lint the project using the pre-commit hooks and mypy."""
    test_for_rej()
    pre_commit(c=c, auto_fix=auto_fix)
    mypy(c)


@task
def pr(c: Context, auto_fix: bool = False):
    """Run all checks and update the PR."""
    add_and_commit(c)
    lint(c, auto_fix=auto_fix)
    test(c)
    update_branch(c)
    update_pr(c)


@task
def docs(c: Context, view: bool = False, view_only: bool = False):
    """
    Build and view docs. If neither build or view are specified, both are run.
    """
    if not view_only:
        echo_header(f"{Msg.DOING}: Building docs")
        c.run("sphinx-build -b html docs docs/_build/html")
    if view or view_only:
        echo_header(f"{Msg.EXAMINE}: Opening docs in browser")
        # check the OS and open the docs in the browser
        if NOT_WINDOWS:
            c.run("open docs/_build/html/index.html")
        else:
            c.run("start docs/_build/html/index.html")
