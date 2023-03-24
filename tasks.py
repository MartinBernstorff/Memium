from pathlib import Path

from invoke import Context, Result, task


def echo_header(msg: str):
    print(f"\n--- {msg} ---")


@task
def setup(c: Context, python_version: str = "3.9"):
    git_init(c)
    setup_venv(c, python_version=python_version)
    install(c)


def git_init(c: Context):
    # If no .git directory exits
    if not Path(".git").exists():
        echo_header("🔨 Initializing Git repository")
        c.run("git init")
        c.run("git add .")
        c.run("git commit -m 'Initial commit'")
        print("✅ Git repository initialized")
    else:
        print("✅ Git repository already initialized")


def setup_venv(
    c: Context,
    python_version: str,
):
    venv_name = f'.venv{python_version.replace(".", "")}'

    if not Path(venv_name).exists():
        echo_header("🔨 Creating virtual environment")
        c.run(f"python{python_version} -m venv {venv_name}")
        print("✅ Virtual environment created")
    else:
        print("✅ Virtual environment already exists")

    c.run(f"source {venv_name}/bin/activate")


@task
def install(c: Context):
    echo_header("🔨 Installing project")
    c.run("pip install -e '.[dev,tests]'")


@task
def update(c: Context):
    echo_header("🔨 Updating project")
    c.run("pip install --upgrade -e '.[dev,tests]'")


@task
def test(c: Context):
    echo_header("🧪 Running tests")
    test_result: Result = c.run(
        "pytest -x -n auto -rfE --failed-first -p no:typeguard -p no:cov --disable-warnings -q",
        warn=True,
        pty=True,
    )

    # If "failed" in the pytest results
    if "failed" in test_result.stdout:
        print("\n\n\n")
        echo_header("Failed tests")

        # Get lines with "FAILED" in them from the .pytest_results file
        failed_tests = [
            line
            for line in Path("tests/.pytest_results").read_text().splitlines()
            if line.startswith("FAILED")
        ]

        for line in failed_tests:
            # Remove from start of line until /test_
            line_sans_prefix = line[line.find("test_") :]

            # Keep only that after ::
            line_sans_suffix = line_sans_prefix[line_sans_prefix.find("::") + 2 :]
            print(f"FAILED 🚨 #{line_sans_suffix}     ")

        exit(0)


def add_commit(c: Context):
    print("🔨 Adding and committing changes")
    c.run("git add .")
    commit_msg = input("Commit message: ")
    c.run(f'git commit -m "{commit_msg}"')


def confirm_uncommitted_changes(c: Context):
    git_status_result: Result = c.run(
        "git status --porcelain",
        warn=True,
        pty=True,
    )

    uncommitted_changes = git_status_result.stdout != ""
    uncommitted_changes_descr = git_status_result.stdout

    if uncommitted_changes:
        echo_header(
            "🚧 Uncommitted changes detected:",
        )
        print(
            f"{uncommitted_changes_descr}\n",
        )
        add_commit(c)


@task
def pr(c: Context):
    confirm_uncommitted_changes(c)
    lint(c)
    test(c)

    # Get current branch name
    branch_name = Path(".git/HEAD").read_text().split("/")[-1].strip()

    pr_result: Result = c.run(
        "gh pr list --state OPEN --search $(git rev-parse --abbrev-ref HEAD)",
        warn=True,
        pty=True,
        hide=True,
    )

    if branch_name not in pr_result.stdout:
        create_pr(c)
    else:
        print("🚂 Pushing to existing PR...")
        c.run("git push")
        open_web = input("🔨 PR already exists. Open in browser? [y/n] ")
        if "y" in open_web.lower():
            c.run("gh pr view --web", pty=True)


def create_pr(c: Context):
    echo_header("🔨 Creating PR")
    # Check if branch already exists on remote, if not, push it
    branch_name = Path(".git/HEAD").read_text().split("/")[-1].strip()
    branch_exists_result: Result = c.run(
        f"git ls-remote --heads origin {branch_name}",
        warn=True,
        pty=True,
        hide=True,
    )

    if branch_exists_result.stdout == "":
        echo_header("🚂 Pushing new branch to remote")
        c.run("git push --set-upstream origin HEAD")

    # Create PR
    echo_header("🔨 Creating PR")
    c.run(
        "gh pr create --web",
    )


@task
def lint(c: Context):
    pre_commit(c)
    mypy(c)


def pre_commit(c: Context):
    echo_header("🧹 Running pre-commit checks")
    c.run("pre-commit run --all-files", pty=True)


def mypy(c: Context):
    echo_header("🧹 Running mypy")
    c.run("mypy .", pty=True)
