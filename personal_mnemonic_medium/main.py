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
from personal_mnemonic_medium.data_access.exporters.anki.anki_exporter import (
    AnkiPackageGenerator,
)
from personal_mnemonic_medium.data_access.exporters.anki.sync.anki_sync import (
    AnkiConnectParams,
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
    return os.getenv("ENV", default)


def main(
    input_dir: Path,
    apkg_output_filepath: Path,
    host_ankiconnect_dir: Path,
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

    if not apkg_output_filepath.parent.exists():
        apkg_output_filepath.parent.mkdir(exist_ok=True, parents=True)
        msg.info(f"Creating output directory {host_ankiconnect_dir}")

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

    # TODO: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues/263 refactor: separate writing decks to disk and ankiconnect sync

    sync_decks(
        local_output_dir=apkg_output_filepath,
        anki_connect=None
        if not use_anki_connect
        else AnkiConnectParams(
            apkg_dir=host_ankiconnect_dir,
            max_wait_seconds=15,
            delete_cards=True,
        ),
        cards=cards,
    )

    if watch:
        sleep_seconds = 60
        msg.good(
            f"Sync complete, sleeping for {sleep_seconds} seconds"
        )
        sleep(sleep_seconds)
        main(
            apkg_output_filepath=apkg_output_filepath,
            input_dir=input_dir,
            watch=watch,
            host_ankiconnect_dir=host_ankiconnect_dir,
            use_anki_connect=use_anki_connect,
        )


if __name__ == "__main__":
    main(
        input_dir=Path("/input"),
        host_ankiconnect_dir=Path("/Users/au484925/ankidecks/"),
        watch=True,
        use_anki_connect=True,
        apkg_output_filepath=Path("/output/deck.apkg"),
    )
