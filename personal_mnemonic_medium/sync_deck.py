from pathlib import Path

from .data_access.ankiconnect_gateway import (
    ANKICONNECT_URL,
    AnkiConnectGateway,
)
from .diff_determiner import PromptDiffDeterminer
from .prompt_destination.ankiconnect_converter import (
    AnkiPromptConverter,
)
from .prompt_destination.ankiconnect_css import CARD_MODEL_CSS
from .prompt_destination.destination_ankiconnect import (
    AnkiConnectDestination,
)
from .prompt_destination.dryrun import DryRunDestination
from .prompt_source.extractor_cloze import ClozePromptExtractor
from .prompt_source.extractor_qa import QAPromptExtractor
from .prompt_source.facade_document import DocumentPromptSource
from .prompt_source.ingester_markdown import MarkdownDocumentIngester


def sync_deck(
    base_deck: str,
    input_dir: Path,
    apkg_output_dir: Path,
    ankiconnect_read_apkg_from_dir: Path,
    max_deletions_per_run: int,
    dry_run: bool,
):
    source_prompts = DocumentPromptSource(
        document_ingester=MarkdownDocumentIngester(
            directory=input_dir
        ),
        prompt_extractors=[
            QAPromptExtractor(
                question_prefix="Q.", answer_prefix="A."
            ),
            ClozePromptExtractor(),
        ],
    ).get_prompts()

    dest_class = (
        AnkiConnectDestination if not dry_run else DryRunDestination
    )
    destination = dest_class(
        gateway=AnkiConnectGateway(
            ankiconnect_url=ANKICONNECT_URL,
            base_deck=base_deck,
            tmp_read_dir=ankiconnect_read_apkg_from_dir,
            tmp_write_dir=apkg_output_dir,
            max_deletions_per_run=max_deletions_per_run,
            max_wait_seconds=0,
        ),
        prompt_converter=AnkiPromptConverter(
            base_deck=base_deck, card_css=CARD_MODEL_CSS
        ),
    )
    destination_prompts = destination.get_all_prompts()

    update_commands = PromptDiffDeterminer().sync(
        source_prompts=source_prompts,
        destination_prompts=destination_prompts,
    )

    destination.update(commands=update_commands)
