from collections.abc import Sequence
from pathlib import Path

import invoke as inv


def get_code_blocks_from_md(md_path: Path) -> Sequence[str]:
    md = md_path.read_text()
    code_blocks = md.split("```")[1::2]
    return code_blocks


def create_smoketest_dir() -> Path:
    print("💨 Running smoketest")
    input_dir = Path() / ".smoketest_dir"
    input_dir.mkdir(exist_ok=True)

    test_file = input_dir / "test.md"
    test_file.write_text("Q. Question here\nA. Answer!")
    return input_dir


@inv.task  # type: ignore
def smoketest_cli(c: inv.Context):
    smoketest_dir = create_smoketest_dir()
    code_blocks = get_code_blocks_from_md(Path("readme.md"))
    cli_block = next(block for block in code_blocks if "cli-block" in block)
    sanitised_cli_block = cli_block.splitlines()[1].replace("> ", "")

    cli_smoketest_cmd = sanitised_cli_block.replace("[YOUR_INPUT_DIR]", str(smoketest_dir))
    print(cli_smoketest_cmd)
    c.run(cli_smoketest_cmd + "  --dry-run \\\n" + "  --skip-sync")
    print("💨🎉 Smoketest complete")
