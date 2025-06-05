import logging
import sys
import time
from datetime import datetime
from functools import partial
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Annotated, Optional

import typer
from iterpy import Arr

from memium.destination.ankiconnect.anki_converter import AnkiPromptConverter
from memium.destination.ankiconnect.anki_formatter import AnkiQAFormatter
from memium.destination.ankiconnect.ankiconnect_gateway import ANKICONNECT_URL, AnkiConnectGateway
from memium.destination.destination import DeletePrompts, PushPrompts
from memium.destination.destination_ankiconnect import AnkiConnectDestination
from memium.destination.destination_dryrun import DryRunDestination
from memium.diff_determiner import PromptDiffDeterminer
from memium.environment import host_input_dir, in_docker
from memium.raw_processors.title_as_answer import TitleAsAnswerProcessor
from memium.source.document_source import MarkdownDocumentSource
from memium.source.extractors.extractor_qa import QAPromptExtractor
from memium.source.extractors.extractor_table import TableExtractor
from memium.source.prompt_source import DocumentPromptSource

log = logging.getLogger(__name__)

app = typer.Typer()


def main(root_deck: str, input_dir: Path, max_deletions_per_run: int, dry_run: bool):
    # Setup gateway as first step. If Anki is not running, no need to parse all the prompts.
    gateway = AnkiConnectGateway(
        ankiconnect_url=ANKICONNECT_URL,
        root_deck=root_deck,
        tmp_read_dir=host_input_dir() if in_docker() else input_dir,
        tmp_write_dir=input_dir,
        max_deletions_per_run=max_deletions_per_run,
        max_wait_seconds=3600,
    )

    # Get the inputs
    qa_extractor = QAPromptExtractor(question_prefix="Q.", answer_prefix="A.")
    source_prompts = DocumentPromptSource(
        document_ingester=MarkdownDocumentSource(directory=input_dir),
        prompt_extractors=[qa_extractor, TableExtractor()],
    ).get_prompts()

    # Apply transformations
    transformed_source_prompts = (
        Arr([source_prompts])
        .map(
            TitleAsAnswerProcessor(
                question_matcher="Definition?", reversed_question="Term for '%s'?"
            )
        )
        .map(
            TitleAsAnswerProcessor(
                question_matcher="Use when?", reversed_question="What should we use for '%s'?"
            )
        )
        .map(
            TitleAsAnswerProcessor(
                question_matcher="Avoid when?", reversed_question="What should we avoid when '%s'?"
            )
        )
        .map(
            TitleAsAnswerProcessor(
                question_matcher="Antonym?", reversed_question="What is the antonym of '%s'?"
            )
        )
        .flatten()
        .to_list()
    )

    # Determine diff
    dest_class = AnkiConnectDestination if not dry_run else DryRunDestination
    destination = dest_class(
        gateway=gateway,
        prompt_converter=AnkiPromptConverter(root_deck=root_deck),
        formatter=AnkiQAFormatter(
            Path("memium/destination/ankiconnect/default_styling.css").read_text()
        ),
    )
    delete_prompts = PromptDiffDeterminer().to_delete(
        source_prompts=transformed_source_prompts, destination_prompts=destination.get_all_prompts()
    )

    # Synchronise
    destination.update(
        commands=[DeletePrompts(delete_prompts), PushPrompts(transformed_source_prompts)]
    )


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

    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = config_dir / f"{date}-memium.log"

    logging.basicConfig(
        handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler(log_path)],
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S",
    )

    if skip_sync:
        log.info("Skipping sync")
        return

    try:
        pkg_version = version("memium")
        log.info(f"Running memium version {pkg_version}")
    except PackageNotFoundError:
        log.info("Running memium from local source")
    log.info(f"Logging to {log_path}")

    # The watching logic requires having a "core" which can terminate.
    # Alternatively, we could do a recursive call, but that would result in
    # an infinitely growing stack.
    main_fn = partial(
        main,
        root_deck=deck_name,
        input_dir=input_dir,
        max_deletions_per_run=max_deletions_per_run,
        dry_run=dry_run,
    )
    main_fn()

    log.info(f"Logged to {log_path}")

    if watch_seconds:
        log.info(
            f"Sync complete in {(datetime.now() - start_time).total_seconds()} seconds, sleeping for {watch_seconds} seconds"
        )
        time.sleep(watch_seconds)
        main_fn()


if __name__ == "__main__":
    app()
