import shlex
from pathlib import Path

from typer.testing import CliRunner

from memium.__main__ import app

README_PATH = Path(__file__).parent.parent / "readme.md"


def _readme_cli_args(input_dir: Path) -> list[str]:
    code_blocks = README_PATH.read_text().split("```")[1::2]
    cli_block = next(block for block in code_blocks if block.startswith("cli-block"))
    command = cli_block.splitlines()[1].removeprefix("> ")
    command = command.replace("[YOUR_INPUT_DIR]", str(input_dir)).replace(
        "[YOUR_VAULT_NAME]", "SmoketestVault"
    )
    program, *args = shlex.split(command)
    assert program == "memium"
    return args


def test_readme_cli_command_runs(tmp_path: Path):
    (tmp_path / "test.md").write_text("Q. Question here\nA. Answer!")

    result = CliRunner().invoke(app, [*_readme_cli_args(tmp_path), "--skip-sync"])

    assert result.exit_code == 0, result.output
