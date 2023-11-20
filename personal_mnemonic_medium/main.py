import os
from pathlib import Path
from time import sleep
from typing import Annotated

import sentry_sdk
import typer
from wasabi import Printer

from personal_mnemonic_medium.data_access.document_ingesters.markdown_ingester import (
    MarkdownIngester,
)
from personal_mnemonic_medium.data_access.document_ingesters.uuid_handling import (
    extract_bear_guid,
    generate_bear_guid,
)
from personal_mnemonic_medium.data_access.exporters.anki.package_generator import (
    AnkiPackageGenerator,
)
from personal_mnemonic_medium.data_access.exporters.anki.sync.anki_sync import (
    sync_decks,
)
from personal_mnemonic_medium.domain.card_pipeline import CardPipeline
from personal_mnemonic_medium.domain.prompt_extractors.cloze_extractor import (
    ClozePromptExtractor,
)
from personal_mnemonic_medium.domain.prompt_extractors.qa_extractor import (
    QAPromptExtractor,
)

msg = Printer(timestamp=True)


def get_env(default: str) -> str:
    if os.getenv("GITHUB_ACTIONS"):
        return "GITHUB_ACTIONS"
    else os.getenv("ENV"):
        return os.getenv("ENV", default)


def main(
    input_dir: Path,
    host_output_dir: Path,
    watch: Annotated[
        bool,
        typer.Option(
            help="Keep running, updating Anki deck every 15 seconds"
        ),
    ],
    use_anki_connect: Annotated[
        bool,
        typer.Option(
            help="Use AnkiConnect to sync with Anki. If not set, will just write to the output directory"
        ),
    ],
):
    if not input_dir.exists():
        raise FileNotFoundError(
            f"Input directory {input_dir} does not exist"
        )

    if not host_output_dir.exists():
        msg.info(f"Creating output directory {host_output_dir}")
        host_output_dir.mkdir(parents=True, exist_ok=True)

    sentry_sdk.init(
        dsn="https://37f17d6aa7742424652663a04154e032@o4506053997166592.ingest.sentry.io/4506053999984640",
        environment=get_env(default="None"),
    )

    cards = CardPipeline(
        document_factory=MarkdownIngester(
            cut_note_after="# Backlinks",
            uuid_extractor=extract_bear_guid,
            uuid_generator=generate_bear_guid,
        ),  # Step 1, get the documents
        prompt_extractors=[  # Step 2, get the prompts from the documents
            QAPromptExtractor(
                question_prefix="Q.", answer_prefix="A."
            ),
            ClozePromptExtractor(),
        ],
        card_exporter=AnkiPackageGenerator(),  # Step 3, get the cards from the prompts
    ).run(input_path=input_dir)

    sync_decks(host_output_dir, use_anki_connect, cards)

    if watch:
        sleep_seconds = 60
        msg.good(
            f"Sync complete, sleeping for {sleep_seconds} seconds"
        )
        sleep(sleep_seconds)
        main(
            input_dir=input_dir,
            watch=watch,
            host_output_dir=host_output_dir,
            use_anki_connect=use_anki_connect,
        )


if __name__ == "__main__":
    main(
        input_dir=Path("/input"),
        host_output_dir=Path("/Users/au484925/ankidecks/"),
        watch=True,
        use_anki_connect=True,
    )
