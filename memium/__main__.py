import logging
from functools import partial
from pathlib import Path
from typing import Annotated, Optional

import sentry_sdk
import typer

from .destination.ankiconnect.anki_converter import AnkiPromptConverter
from .destination.ankiconnect.ankiconnect_gateway import (
    ANKICONNECT_URL,
    AnkiConnectGateway,
)
from .destination.destination import PushPrompts
from .destination.destination_ankiconnect import AnkiConnectDestination
from .destination.destination_dryrun import DryRunDestination
from .diff_determiner import PromptDiffDeterminer
from .environment import get_env, host_input_dir, in_docker
from .source.document_source import MarkdownDocumentSource
from .source.extractors.extractor_cloze import ClozePromptExtractor
from .source.extractors.extractor_qa import QAPromptExtractor
from .source.source import DocumentPromptSource

log = logging.getLogger(__name__)

app = typer.Typer()


def main(
    base_deck: str,
    input_dir: Path,
    max_deletions_per_run: int,
    dry_run: bool,
    push_all: bool = False,
):
    source_prompts = DocumentPromptSource(
        document_ingester=MarkdownDocumentSource(directory=input_dir),
        prompt_extractors=[
            QAPromptExtractor(question_prefix="Q.", answer_prefix="A."),
            ClozePromptExtractor(),
        ],
    ).get_prompts()

    dest_class = AnkiConnectDestination if not dry_run else DryRunDestination
    destination = dest_class(
        gateway=AnkiConnectGateway(
            ankiconnect_url=ANKICONNECT_URL,
            base_deck=base_deck,
            tmp_read_dir=host_input_dir() if in_docker() else input_dir,
            tmp_write_dir=input_dir,
            max_deletions_per_run=max_deletions_per_run,
            max_wait_seconds=0,
        ),
        prompt_converter=AnkiPromptConverter(
            base_deck=base_deck,
            card_css=Path(
                "memium/destination/ankiconnect/default_styling.css"
            ).read_text(),
        ),
    )
    if not push_all:
        destination_prompts = destination.get_all_prompts()
        update_commands = PromptDiffDeterminer().sync(
            source_prompts=source_prompts,
            destination_prompts=destination_prompts,
        )
        destination.update(commands=update_commands)
    else:
        destination.update([PushPrompts(prompts=source_prompts)])


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
