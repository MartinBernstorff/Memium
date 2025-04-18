from collections.abc import Mapping

import pytest

from memium.source.document import Document

from ..source.prompt import QAWithDoc
from .ankiconnect.ankiconnect_gateway import (
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
                "raw_question": AnkiField(value="MockQuestion", order=2),
                "raw_answer": AnkiField(value="MockAnswer", order=3),
                "Extra": AnkiField(value="MockExtra", order=4),
            }
        ),
        pytest.param(
            ({"UnknownField": AnkiField(value="MockText", order=0)}), marks=pytest.mark.xfail
        ),
    ],
)
def test_ankiconnect_get_all_prompts(fields: Mapping[str, AnkiField]):
    dest = AnkiConnectDestination.dummy(
        gateway=SpieAnkiconnectGateway(note_infos=[MockNoteInfo(fields=fields)])
    )
    prompts = dest.get_all_prompts()

    assert len(prompts) == 1


def test_ankiconnect_push_prompts():
    gateway = SpieAnkiconnectGateway()
    dest = AnkiConnectDestination.dummy(gateway=gateway)
    dest.update(
        [
            PushPrompts(
                prompts=[
                    QAWithDoc.dummy(
                        question="FakeQuestion",
                        answer="FakeAnswer",
                        parent_doc=Document.dummy(tags=["anki/deck/FakeSubdeck/FakeSubSubdeck"]),
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
        == "FakeBaseDeck::FakeSubdeck::FakeSubSubdeck"
    )
    assert len(import_package_command.package.decks) == 1  # type: ignore

    for command in expected_commands:
        assert (
            len([c for c in gateway.executed_commands if isinstance(c, command[0])]) == command[1]
        )
