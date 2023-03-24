from pathlib import Path

from invoke import Context, Result, task


def echo_header(msg: str):
    print(f"\n--- {msg} ---")


@task
def setup(c: Context):
    git_init(c)
    setup_venv(c)


@task
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


@task
def setup_venv(c: Context):
    if not Path(".venv").exists():
        echo_header("🔨 Creating virtual environment")
        c.run("python3.9 -m venv .venv")
        print("✅ Virtual environment created")
    else:
        print("✅ Virtual environment already exists")


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


@task
def pr(c: Context):
    lint(c)
    test(c)

    # Check if pull request exists from current branch using github CLI
    # If none, create one


@task
def lint(c: Context):
    pre_commit(c)
    mypy(c)


@task
def pre_commit(c: Context):
    echo_header("🧹 Running pre-commit checks")
    c.run("pre-commit run --all-files", pty=True)


@task
def mypy(c: Context):
    echo_header("🧹 Running mypy")
    c.run("mypy .", pty=True)
