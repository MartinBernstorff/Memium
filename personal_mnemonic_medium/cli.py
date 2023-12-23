import logging
from pathlib import Path
from typing import Annotated, Optional

import sentry_sdk
import typer

from personal_mnemonic_medium.data_access.environment import get_env
from personal_mnemonic_medium.main import main

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
        ),
    ],
    apkg_output_dir: Annotated[
        Path,
        typer.Option(
            help="Directory to use for temporary storage of .apkg while syncing.",
            dir_okay=True,
            file_okay=False,
            exists=True,
            writable=True,
        ),
    ],
    host_apkg_dir: Annotated[
        Optional[Path],  # noqa: UP007
        typer.Option(
            help="Directory in which AnkiConnect will look for the .apkg. Can be different from apkg_output_filepath in cases where the script is running in a Docker container. If None, defaults to apkg_output_filepath"
        ),
    ] = None,
    watch: Annotated[
        Optional[int],  # noqa: UP007
        typer.Option(help="Keep running, updating Anki deck every 15 seconds"),
    ] = None,
    deck_name: Annotated[
        str,
        typer.Option(help="Anki path to deck, e.g. 'Parent deck::Child deck'"),
    ] = "Personal Mnemonic Medium",
    max_deletions_per_run: Annotated[
        int,
        typer.Option(
            help="Maximum number of cards to delete per sync to avoid unintentional deletions. If exceeded, raises error."
        ),
    ] = 50,
    dry_run: Annotated[
        bool,
        typer.Option(
            help="Don't update via AnkiConnect, just log what would happen"
        ),
    ] = False,
    skip_sync: Annotated[
        bool, typer.Option(help="Skip all syncing, useful for smoketest")
    ] = False,
):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y/&m/%d %H:%M:%S",
    )

    # Use apkg_output_filepath if host_ankiconnect_dir is not set
    host_apkg_dir = host_apkg_dir if host_apkg_dir else apkg_output_dir

    sentry_sdk.init(
        dsn="https://37f17d6aa7742424652663a04154e032@o4506053997166592.ingest.sentry.io/4506053999984640",
        environment=get_env(default="None"),
    )

    if not skip_sync:
        main(
            base_deck=deck_name,
            input_dir=input_dir,
            apkg_output_dir=apkg_output_dir,
            ankiconnect_read_apkg_from_dir=host_apkg_dir,
            max_deletions_per_run=max_deletions_per_run,
            dry_run=dry_run,
        )

        if watch:
            sleep_seconds = 60
            log.info(f"Sync complete, sleeping for {sleep_seconds} seconds")
            main(
                base_deck=deck_name,
                input_dir=input_dir,
                apkg_output_dir=apkg_output_dir,
                ankiconnect_read_apkg_from_dir=host_apkg_dir,
                max_deletions_per_run=max_deletions_per_run,
                dry_run=dry_run,
            )


if __name__ == "__main__":
    app()
