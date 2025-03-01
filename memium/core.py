import datetime
import logging
import os
from pathlib import Path

from joblib import Memory  # type: ignore

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
from memium.source.prompt_source import DocumentPromptSource
from memium.source.transformers import question_rephraser

log = logging.getLogger(__name__)


def main(
    base_deck: str,
    input_dir: Path,
    config_dir: Path,
    max_deletions_per_run: int,
    dry_run: bool,
    push_all: bool,
    rephrase_if_younger_than_days: int | None,
    rephrase_cache_days: int | None,
):
    # Check anthropic setup
    if (rephrase_if_younger_than_days or rephrase_cache_days) and os.getenv(
        "ANTHROPIC_API_KEY"
    ) is None:
        raise ValueError("ANTHROPIC_API_KEY environment variable is not set")

    # Setup gateway as first step. If Anki is not running, no need to parse all the prompts.
    gateway = AnkiConnectGateway(
        ankiconnect_url=ANKICONNECT_URL,
        base_deck=base_deck,
        tmp_read_dir=host_input_dir() if in_docker() else input_dir,
        tmp_write_dir=input_dir,
        max_deletions_per_run=max_deletions_per_run,
        max_wait_seconds=3600,
    )

    # Get the inputs
    source_prompts = DocumentPromptSource(
        document_ingester=MarkdownDocumentSource(directory=input_dir),
        prompt_extractors=[
            QAPromptExtractor(question_prefix="Q.", answer_prefix="A."),
            TableExtractor(),
        ],
    ).get_prompts()

    # refactor: instead of calling get_prompts here, we can perhaps validate that the promptsource exists, and
    # only extract the prompts later. I.e. splitting up into a "setup" phase, which validates assumptions, and an
    # execution phase?

    # feat: instead of rephrasing based on document modification date, I'd love to rephrase the "next up" cards
    # This means we need to get "MaterialisedPrompts" (i.e. those stored in the destination), and order them by when they are
    # due. Then apply transformations only to those which are due.
    # This seems relatively complicated with the current prompt type hierarchy, so look at their refactor first.
    if rephrase_if_younger_than_days is not None:
        # perf: we could rephrase only the prompts which are due within a timedelta by getting them as destinationprompts,
        # and using those to filter which prompts to rephrase
        if not rephrase_cache_days is not None:
            raise ValueError(
                "rephrase_cache_days must be set if rephrase_if_younger_than_days is set"
            )
        rephrase_cache_dir = config_dir / "rephrasings"
        log.info(f"Caching rephrasings in {rephrase_cache_dir}")
        rephrase_cache_dir.mkdir(exist_ok=True, parents=True)
        question_rephraser.memory = Memory(rephrase_cache_dir)

        source_prompts = question_rephraser.rephrase(
            source_prompts,
            max_age=datetime.timedelta(days=rephrase_if_younger_than_days),
            cache_days=rephrase_cache_days,
        )

    # Get the destination
    # refactor: move this to the setup phase. See if there are any assumptions we want to test during setup.
    dest_class = AnkiConnectDestination if not dry_run else DryRunDestination
    destination = dest_class(
        gateway=gateway,
        prompt_converter=AnkiPromptConverter(
            base_deck=base_deck,
            card_css=Path("memium/destination/ankiconnect/default_styling.css").read_text(),
        ),
    )
    destination_prompts = destination.get_all_prompts()

    # Get the updates
    # So, this is where the bug is! If push_all is set, it means it won't delete
    # That's a shame! Instead, I want it to determine the diff anyway, and replace the
    # push part
    diff = PromptDiffDeterminer().sync(
        source_prompts=source_prompts, destination_prompts=destination_prompts
    )

    actions_to_perform: list[PushPrompts | DeletePrompts] = []

    for d in diff:
        match d:
            case PushPrompts(prompts=source_prompts):
                if push_all:
                    actions_to_perform.append(PushPrompts(prompts=source_prompts))
                else:
                    actions_to_perform.append(d)
            case DeletePrompts(prompts=source_prompts):
                actions_to_perform.append(d)

    # Send them
    destination.update(commands=actions_to_perform)
