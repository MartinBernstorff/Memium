from ....data_access.ankiconnect import FakeAnkiconnectGateway
from .ankiconnect_destination import AnkiConnectDestination


def test_ankiconnect_get_all_prompts():
    dest = AnkiConnectDestination(gateway=FakeAnkiconnectGateway())
    prompts = dest.get_all_prompts()

    assert len(prompts) > 0
