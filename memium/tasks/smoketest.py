from collections.abc import Sequence
from pathlib import Path

import invoke as inv

from memium.tasks.graphite import submit_pr  # noqa: F401 # type: ignore


def get_code_blocks_from_md(md_path: Path) -> Sequence[str]:
    md = md_path.read_text()
    code_blocks = md.split("```")[1::2]
    return code_blocks


def create_smoketest_dir() -> Path:
    print("💨 Running smoketest")
    input_dir = Path.home() / "smoketest_dir"
    input_dir.mkdir(exist_ok=True)

    test_file = input_dir / "test.md"
    test_file.write_text("Q. Question here\nA. Answer!")
    return input_dir


@inv.task  # type: ignore
def smoketest_docker(c: inv.Context):
    input_dir = create_smoketest_dir()

    code_blocks = get_code_blocks_from_md(Path("readme.md"))
    docker_block = next(block for block in code_blocks if "docker run" in block).strip() + " \\\n"

    # Only keep content after docker line
    docker_block = docker_block[docker_block.index("docker run") :]
    replaced_image_location = docker_block.replace(
        "ghcr.io/martinbernstorff/memium:latest", "memium"
    )
    replaced_input_dir = replaced_image_location.replace("$INPUT_DIR", str(input_dir))

    smoketest_docker_command = replaced_input_dir + "  --dry-run \\\n" + "  --skip-sync"

    print(smoketest_docker_command)

    c.run("docker build . -t memium:latest -f Dockerfile")
    c.run("docker volume create ankidecks")
    c.run(smoketest_docker_command)
    print("💨🎉 Smoketest complete")


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
