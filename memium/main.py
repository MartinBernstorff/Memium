from pathlib import Path

from .data_access.ankiconnect_gateway import ANKICONNECT_URL, AnkiConnectGateway
from .data_access.environment import host_input_dir, in_docker
from .destination.ankiconnect.anki_converter import AnkiPromptConverter
from .destination.ankiconnect.ankiconnect_css import CARD_MODEL_CSS
from .destination.destination_ankiconnect import AnkiConnectDestination
from .destination.destination_commands import PushPrompts
from .destination.destination_dryrun import DryRunDestination
from .diff_determiner import PromptDiffDeterminer
from .source.document_ingester import MarkdownDocumentIngester
from .source.extractors.extractor_cloze import ClozePromptExtractor
from .source.extractors.extractor_qa import QAPromptExtractor
from .source.facade import DocumentPromptSource


def main(
    base_deck: str,
    input_dir: Path,
    max_deletions_per_run: int,
    dry_run: bool,
    push_all: bool = False,
):
    source_prompts = DocumentPromptSource(
        document_ingester=MarkdownDocumentIngester(directory=input_dir),
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
            base_deck=base_deck, card_css=CARD_MODEL_CSS
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
