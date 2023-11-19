from collections import defaultdict
from pathlib import Path
from time import sleep
from typing import Annotated, Any

import sentry_sdk
import typer
from wasabi import Printer

from personal_mnemonic_medium.data_access.document_ingesters.markdown_ingester import (
    MarkdownNoteFactory,
)
from personal_mnemonic_medium.data_access.exporters.anki.card_types.base import (
    AnkiCard,
)
from personal_mnemonic_medium.data_access.exporters.anki.package_generator import (
    AnkiPackageGenerator,
)
from personal_mnemonic_medium.data_access.exporters.anki.sync import (
    sync_deck,
)
from personal_mnemonic_medium.domain.card_pipeline import CardPipeline
from personal_mnemonic_medium.domain.prompt_extractors.cloze_extractor import (
    ClozePromptExtractor,
)
from personal_mnemonic_medium.domain.prompt_extractors.qa_extractor import (
    QAPromptExtractor,
)

msg = Printer(timestamp=True)


# helper for creating anki connect requests
def request(action: Any, **params: Any) -> dict[str, Any]:
    return {"action": action, "params": params, "version": 6}


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
    """Run the thing."""
    if not input_dir.exists():
        raise FileNotFoundError(
            f"Input directory {input_dir} does not exist"
        )

    if not host_output_dir.exists():
        msg.info(f"Creating output directory {host_output_dir}")
        host_output_dir.mkdir(parents=True, exist_ok=True)

    sentry_sdk.init(
        dsn="https://37f17d6aa7742424652663a04154e032@o4506053997166592.ingest.sentry.io/4506053999984640",
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        traces_sample_rate=1.0,
        # Set profiles_sample_rate to 1.0 to profile 100%
        # of sampled transactions.
        # We recommend adjusting this value in production.
        profiles_sample_rate=1.0,
    )

    cards = CardPipeline(
        document_factory=MarkdownNoteFactory(),  # Step 1, get the documents
        prompt_extractors=[  # Step 2, get the prompts from the documents
            QAPromptExtractor(),
            ClozePromptExtractor(),
        ],
        card_exporter=AnkiPackageGenerator(),  # Step 3, get the cards from the prompts
    ).run(input_path=input_dir)

    decks: dict[str, list[AnkiCard]] = defaultdict(list)

    for card in cards:
        decks[card.deckname] += [card]

    for deck in decks:
        cards = decks[deck]
        deck_bundle = AnkiPackageGenerator().cards_to_deck_bundle(
            cards=cards
        )
        sync_deck(
            deck_bundle=deck_bundle,
            sync_dir_path=host_output_dir,
            save_dir_path=Path("/output"),
            max_wait_for_ankiconnect=30,
            use_anki_connect=use_anki_connect,
        )

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
