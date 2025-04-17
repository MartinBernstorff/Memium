from collections.abc import Mapping
from pathlib import Path

import pytest

from ..source.prompts.prompt_qa import QAWithoutDoc
from .ankiconnect.anki_converter import AnkiPromptConverter
from .ankiconnect.ankiconnect_gateway import (
    ANKICONNECT_URL,
    AnkiConnectGateway,
    AnkiField,
    ImportPackage,
    SpieAnkiconnectGateway,
    UpdateModel,
)
from .ankiconnect.test_ankiconnect_gateway import MockNoteInfo
from .destination import PushPrompts
from .destination_ankiconnect import AnkiConnectDestination


@pytest.mark.parametrize(
    ("fields"),
    [
        (
            {
                "Question": AnkiField(value="MockQuestion", order=0),
                "Answer": AnkiField(value="MockAnswer", order=1),
            }
        ),
        pytest.param(
            ({"UnknownField": AnkiField(value="MockText", order=0)}), marks=pytest.mark.xfail
        ),
    ],
)
def test_ankiconnect_get_all_prompts(fields: Mapping[str, AnkiField]):
    dest = AnkiConnectDestination(
        gateway=SpieAnkiconnectGateway(note_infos=[MockNoteInfo(fields=fields)]),
        prompt_converter=AnkiPromptConverter(base_deck="FakeDeck", card_css="FakeCSS"),
    )
    prompts = dest.get_all_prompts()

    assert len(prompts) == 1


def test_ankiconnect_push_prompts():
    gateway = SpieAnkiconnectGateway()
    dest = AnkiConnectDestination(
        gateway=gateway,
        prompt_converter=AnkiPromptConverter(base_deck="FakeDeck", card_css="FakeCSS"),
    )
    dest.update(
        [
            PushPrompts(
                prompts=[
                    QAWithoutDoc.dummy(
                        question="FakeQuestion",
                        answer="FakeAnswer",
                        tags=["anki/deck/FakeSubdeck/FakeSubSubdeck"],
                    )
                ]
            )
        ]
    )

    expected_commands = [(ImportPackage, 1), (UpdateModel, 1)]
    import_package_command = next(
        c for c in gateway.executed_commands if isinstance(c, ImportPackage)
    )
    assert (
        import_package_command.package.decks[0].name  # type: ignore
        == "FakeDeck::FakeSubdeck::FakeSubSubdeck"
    )
    assert len(import_package_command.package.decks) == 1  # type: ignore

    for command in expected_commands:
        assert (
            len([c for c in gateway.executed_commands if isinstance(c, command[0])]) == command[1]
        )


def test_getting_all_prompts(tmp_path: Path):
    gateway = AnkiConnectGateway(
        ankiconnect_url=ANKICONNECT_URL,
        base_deck="Memium",
        tmp_read_dir=tmp_path,
        tmp_write_dir=tmp_path,
        max_deletions_per_run=10,
        max_wait_seconds=3600,
    )
    dest = AnkiConnectDestination(
        gateway=gateway,
        prompt_converter=AnkiPromptConverter(base_deck="FakeDeck", card_css="FakeCSS"),
    )
    dest.get_all_prompts()
