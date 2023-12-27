from pathlib import Path

from .cli import app
from .destination.ankiconnect.anki_converter import AnkiPromptConverter
from .destination.ankiconnect.ankiconnect_gateway import (
    ANKICONNECT_URL,
    AnkiConnectGateway,
)
from .destination.destination import PushPrompts
from .destination.destination_ankiconnect import AnkiConnectDestination
from .destination.destination_dryrun import DryRunDestination
from .diff_determiner import PromptDiffDeterminer
from .environment import host_input_dir, in_docker
from .source.document_source import MarkdownDocumentSource
from .source.extractors.extractor_cloze import ClozePromptExtractor
from .source.extractors.extractor_qa import QAPromptExtractor
from .source.source import DocumentPromptSource

app()


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
