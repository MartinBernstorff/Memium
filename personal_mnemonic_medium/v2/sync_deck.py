from pathlib import Path

from personal_mnemonic_medium.data_access.exporters.anki.anki_css import (
    CARD_MODEL_CSS,
)

from ..data_access.exporters.anki.globals import ANKICONNECT_URL
from .data_access.ankiconnect_gateway import AnkiConnectGateway
from .domain.diff_determiner.base_diff_determiner import (
    PromptDiffDeterminer,
)
from .domain.prompt_destination.anki_connect.ankiconnect_destination import (
    AnkiConnectDestination,
)
from .domain.prompt_destination.anki_connect.prompt_converter.anki_prompt_converter import (
    AnkiPromptConverter,
)
from .domain.prompt_destination.dryrun_destination import (
    DryRunDestination,
)
from .domain.prompt_source.document_ingesters.markdown_document_ingester import (
    MarkdownDocumentIngester,
)
from .domain.prompt_source.document_prompt_source import (
    DocumentPromptSource,
)
from .domain.prompt_source.prompt_extractors.cloze_prompt_extractor import (
    ClozePromptExtractor,
)
from .domain.prompt_source.prompt_extractors.qa_prompt_extractor import (
    QAPromptExtractor,
)


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
