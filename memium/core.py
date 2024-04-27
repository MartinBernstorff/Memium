from pathlib import Path

from memium.destination.ankiconnect.anki_converter import AnkiPromptConverter
from memium.destination.ankiconnect.ankiconnect_gateway import ANKICONNECT_URL, AnkiConnectGateway
from memium.destination.destination import PushPrompts
from memium.destination.destination_ankiconnect import AnkiConnectDestination
from memium.destination.destination_dryrun import DryRunDestination
from memium.diff_determiner import PromptDiffDeterminer
from memium.environment import host_input_dir, in_docker
from memium.source.document_source import MarkdownDocumentSource
from memium.source.extractors.extractor_qa import QAPromptExtractor
from memium.source.extractors.extractor_table import TableExtractor
from memium.source.prompt_source import DocumentPromptSource


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
            TableExtractor(),
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
            max_wait_seconds=30,
        ),
        prompt_converter=AnkiPromptConverter(
            base_deck=base_deck,
            card_css=Path("memium/destination/ankiconnect/default_styling.css").read_text(),
        ),
    )

    if push_all:
        update_commands = [PushPrompts(prompts=source_prompts)]
    else:
        destination_prompts = destination.get_all_prompts()
        update_commands = PromptDiffDeterminer().sync(
            source_prompts=source_prompts, destination_prompts=destination_prompts
        )

    destination.update(commands=update_commands)
