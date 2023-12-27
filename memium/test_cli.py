from pathlib import Path

from .cli import cli


def test_cli(tmp_path: Path):
    test_file = tmp_path / "test.md"
    test_file.write_text("Q. Question here\nA. Answer!")
    cli(
        input_dir=Path("/root/input"),
        watch=None,
        deck_name="Test CLI",
        max_deletions_per_run=50,
        push_all=False,
        dry_run=False,
        sentry_dsn=None,
    )
