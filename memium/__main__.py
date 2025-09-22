import logging
import sys
import time
from collections.abc import Sequence
from datetime import datetime
from functools import partial
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Annotated

import typer
from iterpy import Arr

from memium.destination.ankiconnect.anki_converter import AnkiPromptConverter
from memium.destination.ankiconnect.ankiconnect_requester import ANKICONNECT_URL, AnkiRequester
from memium.destination.ankiconnect.note_store import AnkiNoteStore
from memium.destination.ankiconnect.syncer import Syncer
from memium.raw_processors.categoriser import Categoriser
from memium.raw_processors.title_as_answer import TitleAsAnswerProcessor
from memium.source.document_source import MarkdownDocumentSource
from memium.source.extractors.extractor_qa import QAPromptExtractor
from memium.source.extractors.extractor_table import TableExtractor
from memium.source.prompt import QAWithDoc
from memium.source.prompt_source import DocumentPromptSource

log = logging.getLogger(__name__)

app = typer.Typer()


def _log_with_prefix(prefix: str, prompts: Sequence[QAWithDoc]) -> Sequence[QAWithDoc]:
    log.info(f"{prefix}: {len(prompts)}")
    return prompts


def main(root_deck: str, input_dir: Path, skip_categorisation: bool = False) -> None:
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
            lambda x: x
            if skip_categorisation
            else Categoriser(cache_dir=input_dir / ".memium" / ".cache")
        )
        .map(lambda x: _log_with_prefix("After categorisations: ", x))
        .map(
            TitleAsAnswerProcessor(
                question_matcher="Definition?", reversed_question="Term for '%s'?"
            )
        )
        .map(lambda x: _log_with_prefix("After definition: ", x))
        .map(
            TitleAsAnswerProcessor(
                question_matcher="Use when?", reversed_question="What should we use for '%s'?"
            )
        )
        .map(lambda x: _log_with_prefix("After use: ", x))
        .map(
            TitleAsAnswerProcessor(
                question_matcher="Avoid when?", reversed_question="What should we avoid when '%s'?"
            )
        )
        .map(lambda x: _log_with_prefix("After when: ", x))
        .map(
            TitleAsAnswerProcessor(
                question_matcher="Antonym?", reversed_question="What is the antonym of '%s'?"
            )
        )
        .map(lambda x: _log_with_prefix("After antonym: ", x))
        .flatten()
        .to_list()
    )

    # Determine diff
    note_store = AnkiNoteStore(
        anki_requester=AnkiRequester(ankiconnect_url=ANKICONNECT_URL, max_wait_seconds=300),
        root_deck=root_deck,
    )

    syncer = Syncer(
        source_prompts=transformed_source_prompts,
        destination_prompts=note_store.get_all_sans_decks(),
        converter=AnkiPromptConverter(root_deck=root_deck),
        note_store=note_store,
    )
    syncer.sync()


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
        int | None, typer.Option(help="Keep running, updating Anki deck every [ARG] seconds")
    ] = None,
    deck_name: Annotated[
        str, typer.Option(help="Anki path to deck, e.g. 'Parent deck::Child deck'")
    ] = "Memium",
    skip_sync: Annotated[
        bool, typer.Option(help="Skip all syncing, useful for smoketesting of the interface")
    ] = False,
    skip_categorisation: Annotated[
        bool, typer.Option(help="Skip categorisation step, useful for debugging")
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
        main, root_deck=deck_name, input_dir=input_dir, skip_categorisation=skip_categorisation
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
