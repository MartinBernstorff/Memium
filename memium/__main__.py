import logging
import sys
import time
from datetime import datetime
from functools import partial
from pathlib import Path
from typing import Annotated, Optional

import typer

from memium.destination.ankiconnect.anki_converter import AnkiPromptConverter
from memium.destination.ankiconnect.ankiconnect_gateway import ANKICONNECT_URL, AnkiConnectGateway
from memium.destination.destination import DeletePrompts, PushPrompts
from memium.destination.destination_ankiconnect import AnkiConnectDestination
from memium.destination.destination_dryrun import DryRunDestination
from memium.diff_determiner import PromptDiffDeterminer
from memium.environment import host_input_dir, in_docker
from memium.source.document_source import MarkdownDocumentSource
from memium.source.extractors.extractor_qa import QAPromptExtractor
from memium.source.extractors.extractor_table import TableExtractor
from memium.source.extractors.extractor_title_as_answer import TitleAsAnswerExtractor
from memium.source.prompt_source import DocumentPromptSource

log = logging.getLogger(__name__)

app = typer.Typer()


def main(
    base_deck: str,
    input_dir: Path,
    max_deletions_per_run: int,
    dry_run: bool,
    push_all: bool = False,
):
    # Setup gateway as first step. If Anki is not running, no need to parse all the prompts.
    gateway = AnkiConnectGateway(
        ankiconnect_url=ANKICONNECT_URL,
        base_deck=base_deck,
        tmp_read_dir=host_input_dir() if in_docker() else input_dir,
        tmp_write_dir=input_dir,
        max_deletions_per_run=max_deletions_per_run,
        max_wait_seconds=3600,
    )

    dest_class = AnkiConnectDestination if not dry_run else DryRunDestination
    destination = dest_class(
        gateway=gateway,
        prompt_converter=AnkiPromptConverter(
            base_deck=base_deck,
            card_css=Path("memium/destination/ankiconnect/default_styling.css").read_text(),
        ),
    )

    # Get the inputs
    qa_extractor = QAPromptExtractor(question_prefix="Q.", answer_prefix="A.")
    source_prompts = DocumentPromptSource(
        document_ingester=MarkdownDocumentSource(directory=input_dir),
        prompt_extractors=[
            qa_extractor,
            TitleAsAnswerExtractor(
                qa_extractor, matcher="Definition?", reversed_question="Term for '%s'?"
            ),
            TitleAsAnswerExtractor(
                qa_extractor, matcher="Use when?", reversed_question="What should we use for '%s'?"
            ),
            TitleAsAnswerExtractor(
                qa_extractor,
                matcher="Avoid when?",
                reversed_question="What should we avoid when '%s'?",
            ),
            TableExtractor(),
        ],
    ).get_prompts()

    diff = PromptDiffDeterminer().sync(
        source_prompts=source_prompts, destination_prompts=destination.get_all_prompts()
    )

    delete_prompts = [command for command in diff if isinstance(command, DeletePrompts)]
    push_prompts = (
        [command for command in diff if isinstance(command, PushPrompts)]
        if not push_all
        else [PushPrompts(prompts=source_prompts)]
    )

    destination.update(commands=[*delete_prompts, *push_prompts])


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

    # The watching logic requires having a "core" which can terminate.
    # Alternatively, we could do a recursive call, but that would result in
    # an infinitely growing stack.
    main_fn = partial(
        main,
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
