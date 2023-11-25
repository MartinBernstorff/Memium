from pathlib import Path

from personal_mnemonic_medium.data_access.exporters.anki.sync.ankiconnect.ankiconnect_utils import (
    AnkiConnectParams,
    anki_connect_is_live,
)


def apkg_to_anki(
    apkg_filepath: Path, anki_connect: AnkiConnectParams
) -> None:
    if anki_connect:
        for _ in range(anki_connect.max_wait_seconds):
            if anki_connect_is_live():
                break
            print("Waiting for anki connect to start...")
            sleep(secs=0.5)
        else:
            msg.fail("Unable to connect to anki")
            return
    ...


def remove_diff(
    deck_bundle: DeckBundle, anki_connect: AnkiConnectParams
) -> None:
    diff = calculate_diff(deck_bundle, anki_connect)
    ...


def calculate_diff(
    deck_bundle: DeckBundle, anki_connect: AnkiConnectParams
) -> None:
    ...
