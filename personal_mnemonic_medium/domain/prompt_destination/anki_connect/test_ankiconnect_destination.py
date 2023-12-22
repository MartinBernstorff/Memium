from collections.abc import Mapping

import pytest

from ....data_access.ankiconnect_gateway import (
    AnkiField,
    ImportPackage,
    SpieAnkiconnectGateway,
    UpdateModel,
)
from ....data_access.test_ankiconnect import MockNoteInfo
from ...prompts.cloze_prompt import ClozeWithoutDoc
from ...prompts.qa_prompt import QAWithoutDoc
from ..destination_commands import PushPrompts
from .ankiconnect_destination import AnkiConnectDestination
from .prompt_converter.anki_prompt_converter import (
    AnkiPromptConverter,
)


@pytest.mark.parametrize(
    ("fields"),
    [
        ({"Text": AnkiField(value="MockText", order=0)}),
        (
            {
                "Question": AnkiField(value="MockQuestion", order=0),
                "Answer": AnkiField(value="MockAnswer", order=1),
            }
        ),
        pytest.param(
            ({"UnknownField": AnkiField(value="MockText", order=0)}),
            marks=pytest.mark.xfail,
        ),
    ],
)
def test_ankiconnect_get_all_prompts(fields: Mapping[str, AnkiField]):
    dest = AnkiConnectDestination(
        gateway=SpieAnkiconnectGateway(
            note_infos=[MockNoteInfo(fields=fields)]
        ),
        prompt_converter=AnkiPromptConverter(
            base_deck="FakeDeck", card_css="FakeCSS"
        ),
    )
    prompts = dest.get_all_prompts()

    assert len(prompts) == 1


def test_ankiconnect_push_prompts():
    gateway = SpieAnkiconnectGateway()
    dest = AnkiConnectDestination(
        gateway=gateway,
        prompt_converter=AnkiPromptConverter(
            base_deck="FakeDeck", card_css="FakeCSS"
        ),
    )
    dest.update(
        [
            PushPrompts(
                prompts=[
                    QAWithoutDoc(
                        question="FakeQuestion",
                        answer="FakeAnswer",
                        add_tags=["#anki/deck/FakeSubdeck"],
                    ),
                    ClozeWithoutDoc(
                        text="FakeText", add_tags=["FakeTag"]
                    ),
                ]
            )
        ]
    )

    expected_commands = [(ImportPackage, 1), (UpdateModel, 2)]
    import_package_command = next(
        c
        for c in gateway.executed_commands
        if isinstance(c, ImportPackage)
    )
    assert (
        import_package_command.package.decks[0].name  # type: ignore
        == "FakeDeck::FakeSubdeck"
    )

    for command in expected_commands:
        assert (
            len(
                [
                    c
                    for c in gateway.executed_commands
                    if isinstance(c, command[0])
                ]
            )
            == command[1]
        )
