import logging
from pathlib import Path
from typing import Annotated

import sentry_sdk
import typer

from personal_mnemonic_medium.v2.sync_deck import sync_deck

from ...main import get_env

log = logging.getLogger(__name__)


def main(
    input_dir: Path,
    apkg_output_filepath: Path,
    host_ankiconnect_dir: Path,
    watch: Annotated[
        bool,
        typer.Option(
            help="Keep running, updating Anki deck every 15 seconds"
        ),
    ],
    deck_name: str = typer.Option(
        "Personal Mnemonic Medium",
        help="Name of the Anki deck to sync to",
    ),
    max_deletions_per_run: int = typer.Option(
        50, help="Maximum number of cards to delete per sync"
    ),
    dry_run: bool = typer.Option(
        False,
        help="Don't update via AnkiConnect, just log what would happen",
    ),
    log_file: Path | None = typer.Option(  # noqa: B008
        None, help="File to log to, defaults to stdout"
    ),
):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y/&m/%d %H:%M:%S",
        filename=log_file,
    )

    if not input_dir.exists():
        raise FileNotFoundError(
            f"Input directory {input_dir} does not exist"
        )

    if not apkg_output_filepath.parent.exists():
        apkg_output_filepath.parent.mkdir(exist_ok=True, parents=True)
        log.info(f"Creating output directory {host_ankiconnect_dir}")

    sentry_sdk.init(
        dsn="https://37f17d6aa7742424652663a04154e032@o4506053997166592.ingest.sentry.io/4506053999984640",
        environment=get_env(default="None"),
    )

    sync_deck(
        base_deck=deck_name,
        input_dir=input_dir,
        apkg_output_dir=apkg_output_filepath,
        ankiconnect_read_apkg_from_dir=host_ankiconnect_dir,
        max_deletions_per_run=max_deletions_per_run,
        dry_run=dry_run,
    )

    if watch:
        sleep_seconds = 60
        log.info(
            f"Sync complete, sleeping for {sleep_seconds} seconds"
        )
        sync_deck(
            base_deck=deck_name,
            input_dir=input_dir,
            apkg_output_dir=apkg_output_filepath,
            ankiconnect_read_apkg_from_dir=host_ankiconnect_dir,
            max_deletions_per_run=max_deletions_per_run,
            dry_run=dry_run,
        )


if __name__ == "__main__":
    typer.run(main)
