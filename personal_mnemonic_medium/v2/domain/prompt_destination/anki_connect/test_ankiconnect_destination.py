from .....data_access.exporters.anki.globals import ANKICONNECT_URL
from .ankiconnect_destination import AnkiConnectDestination


def test_ankiconnect_get_all_prompts():
    dest = AnkiConnectDestination(
        ankiconnect_url=ANKICONNECT_URL,
        deck_name="0. Don't click me::1. Active::Personal Mnemonic Medium",
    )

    prompts = dest.get_all_prompts()

    assert len(prompts) == 0
