import logging
from functools import partial
from pathlib import Path
from typing import Annotated, Optional

import sentry_sdk
import typer

from memium.data_access.environment import get_env
from memium.main import main

log = logging.getLogger(__name__)

app = typer.Typer()


@app.command()
def cli(
    input_dir: Annotated[
        Path,
        typer.Option(
            help="Directory containing markdown prompts to sync to Anki.",
            dir_okay=True,
            file_okay=False,
            exists=True,
            readable=True,
            writable=True,
        ),
    ],
    watch: Annotated[
        Optional[int],  # noqa: UP007
        typer.Option(help="Keep running, updating Anki deck every 15 seconds"),
    ] = None,
    deck_name: Annotated[
        str,
        typer.Option(help="Anki path to deck, e.g. 'Parent deck::Child deck'"),
    ] = "Memium",
    max_deletions_per_run: Annotated[
        int,
        typer.Option(
            help="Maximum number of cards to delete per sync to avoid unintentional deletions. If exceeded, raises error."
        ),
    ] = 50,
    push_all: Annotated[
        bool,
        typer.Option(
            help="Push all prompts to Anki, whether or not they exist in Anki. Useful if you have e.g. changed your CSS template. Note that this does not change scheduling, nor delete prompts that no longer exist in your markdown."
        ),
    ] = False,
    dry_run: Annotated[
        bool,
        typer.Option(
            help="Don't update via AnkiConnect, just log what would happen"
        ),
    ] = False,
    sentry_dsn: Annotated[
        Optional[str],  # noqa: UP007
        typer.Option(
            help="Sentry DSN for error reporting. If not provided, no error reporting will be done."
        ),
    ] = None,
    skip_sync: Annotated[
        bool, typer.Option(help="Skip all syncing, useful for smoketest")
    ] = False,
):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y/&m/%d %H:%M:%S",
    )

    if sentry_dsn:
        sentry_sdk.init(dsn=sentry_dsn, environment=get_env(default="None"))

    main_fn = partial(
        main,
        base_deck=deck_name,
        input_dir=input_dir,
        max_deletions_per_run=max_deletions_per_run,
        dry_run=dry_run,
        push_all=push_all,
    )

    if not skip_sync:
        main_fn()
        if watch:
            sleep_seconds = 60
            log.info(f"Sync complete, sleeping for {sleep_seconds} seconds")
            main_fn()


if __name__ == "__main__":
    app()
