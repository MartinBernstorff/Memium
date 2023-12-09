from collections.abc import Mapping

import pytest

from ....data_access.ankiconnect_gateway import (
    AnkiField,
    FakeAnkiconnectGateway,
)
from ....data_access.test_ankiconnect import MockNoteInfo
from .ankiconnect_destination import AnkiConnectDestination


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
        gateway=FakeAnkiconnectGateway(
            note_infos=[MockNoteInfo(fields=fields)]
        )
    )
    prompts = dest.get_all_prompts()

    assert len(prompts) == 1
