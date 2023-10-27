from pathlib import Path
from time import sleep
from typing import Annotated, Any

import sentry_sdk
import typer
from functionalpy import Seq
from personal_mnemonic_medium.card_pipeline import CardPipeline
from personal_mnemonic_medium.exporters.anki.package_generator import (
    AnkiPackageGenerator,
)
from personal_mnemonic_medium.exporters.anki.sync import sync_deck
from personal_mnemonic_medium.note_factories.markdown import (
    MarkdownNoteFactory,
)
from personal_mnemonic_medium.prompt_extractors.cloze_extractor import (
    ClozePromptExtractor,
)
from personal_mnemonic_medium.prompt_extractors.qa_extractor import (
    QAPromptExtractor,
)
from wasabi import Printer

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

    grouped_cards = (
        Seq(cards).group_by(lambda card: card.deckname).to_iter()
    )

    for group in grouped_cards:
        cards = group.group_contents.to_list()
        deck_bundle = AnkiPackageGenerator().cards_to_deck_bundle(
            cards=cards
        )
        sync_deck(
            deck_bundle=deck_bundle,
            sync_dir_path=host_output_dir,
            save_dir_path=Path("/output"),
            max_wait_for_ankiconnect=30,
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
        )


if __name__ == "__main__":
    typer.run(main)
