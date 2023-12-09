from collections.abc import Mapping
from pathlib import Path

import pytest

from ....data_access.ankiconnect_gateway import (
    AnkiField,
    ImportPackage,
    SpieAnkiconnectGateway,
    UpdateModel,
)
from ....data_access.test_ankiconnect import MockNoteInfo
from ...prompt_source.destination_commands import PushPrompts
from ...prompts.cloze_prompt import ClozePromptWithoutDoc
from ...prompts.qa_prompt import QAPromptWithoutDoc
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


def test_ankiconnect_push_prompts(tmpdir: Path):
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
                    QAPromptWithoutDoc(
                        question="FakeQuestion",
                        answer="FakeAnswer",
                        add_tags=["FakeTag"],
                    ),
                    ClozePromptWithoutDoc(
                        text="FakeText", add_tags=["FakeTag"]
                    ),
                ],
                tmp_write_dir=tmpdir,
                tmp_read_dir=tmpdir,
            )
        ]
    )

    expected_commands = [(ImportPackage, 1), (UpdateModel, 2)]
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
