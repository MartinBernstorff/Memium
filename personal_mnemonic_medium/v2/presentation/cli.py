from pathlib import Path
from typing import Annotated

import sentry_sdk
import typer
from wasabi import Printer

from personal_mnemonic_medium.data_access.exporters.anki.anki_css import (
    CARD_MODEL_CSS,
)
from personal_mnemonic_medium.data_access.exporters.anki.globals import (
    ANKICONNECT_URL,
)

from ...main import get_env
from ..data_access.ankiconnect_gateway import AnkiConnectGateway
from ..domain.diff_determiner.base_diff_determiner import (
    PromptDiffDeterminer,
)
from ..domain.prompt_destination.anki_connect.ankiconnect_destination import (
    AnkiConnectDestination,
)
from ..domain.prompt_destination.anki_connect.prompt_converter.anki_prompt_converter import (
    AnkiPromptConverter,
)
from ..domain.prompt_source.base_prompt_source import FakePromptSource

msg = Printer(timestamp=True)


def _sync_deck(
    deck_name: str, input_dir: Path, apkg_output_filepath: Path
):
    # TODO: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues/309 feat: use markdown promptsource
    source_prompts = FakePromptSource().get_prompts()

    destination = AnkiConnectDestination(
        gateway=AnkiConnectGateway(
            ankiconnect_url=ANKICONNECT_URL,
            deck_name=deck_name,
            tmp_read_dir=input_dir,
            tmp_write_dir=apkg_output_filepath,
        ),
        prompt_converter=AnkiPromptConverter(
            base_deck=deck_name, card_css=CARD_MODEL_CSS
        ),
    )
    destination_prompts = destination.get_all_prompts()

    update_commands = PromptDiffDeterminer().sync(
        source_prompts=source_prompts,
        destination_prompts=destination_prompts,
    )

    destination.update(commands=update_commands)


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
    deck_name: str = typer.Option(
        "0. Don't click me::1. Active::Personal Mnemonic Medium",
        help="Name of the Anki deck to sync to",
    ),
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

    _sync_deck(
        deck_name=deck_name,
        input_dir=input_dir,
        apkg_output_filepath=apkg_output_filepath,
    )

    if watch:
        sleep_seconds = 60
        msg.good(
            f"Sync complete, sleeping for {sleep_seconds} seconds"
        )
        _sync_deck(
            deck_name=deck_name,
            input_dir=input_dir,
            apkg_output_filepath=apkg_output_filepath,
        )


if __name__ == "__main__":
    typer.run(main)
