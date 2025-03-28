import logging
import sys
import time
from datetime import datetime
from functools import partial
from pathlib import Path
from typing import Annotated, Optional

import typer

from memium.core import core

log = logging.getLogger(__name__)

app = typer.Typer()


@app.command()
def cli(
    input_dir: Annotated[
        Path,
        typer.Option(
            help="Where to extract prompts from.",
            dir_okay=True,
            file_okay=False,
            exists=True,
            readable=True,
            writable=False,
        ),
    ],
    watch_seconds: Annotated[
        Optional[int],  # noqa: UP007
        typer.Option(help="Keep running, updating Anki deck every [ARG] seconds"),
    ] = None,
    deck_name: Annotated[
        str, typer.Option(help="Anki path to deck, e.g. 'Parent deck::Child deck'")
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
            help="Push all prompts to Anki, not just the diff. Useful if you have e.g. changed your CSS template. Note that this does not change scheduling, nor delete prompts that no longer exist in your markdown."
        ),
    ] = False,
    dry_run: Annotated[
        bool, typer.Option(help="Don't update via AnkiConnect, just log what would happen")
    ] = False,
    skip_sync: Annotated[
        bool, typer.Option(help="Skip all syncing, useful for smoketesting of the interface")
    ] = False,
):
    start_time = datetime.now()
    config_dir = input_dir / ".memium"
    config_dir.mkdir(exist_ok=True)

    logging.basicConfig(
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(config_dir / "memium.log"),
        ],
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S",
    )

    if skip_sync:
        log.info("Skipping sync")
        return

    main_fn = partial(
        core,
        base_deck=deck_name,
        input_dir=input_dir,
        max_deletions_per_run=max_deletions_per_run,
        dry_run=dry_run,
        push_all=push_all,
    )
    main_fn()

    if watch_seconds:
        log.info(
            f"Sync complete in {(datetime.now() - start_time).total_seconds()} seconds, sleeping for {watch_seconds} seconds"
        )
        time.sleep(watch_seconds)
        main_fn()


if __name__ == "__main__":
    app()
