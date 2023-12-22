from collections.abc import Sequence

import pytest

from ..prompt_destination.destination_commands import (
    DeletePrompts,
    PushPrompts,
)
from ..prompts.base_prompt import BasePrompt, DestinationPrompt
from ..prompts.qa_prompt import QAPrompt
from .base_diff_determiner import GeneralSyncer, PromptDiffDeterminer


@pytest.fixture()
def diff_determiner() -> PromptDiffDeterminer:
    return PromptDiffDeterminer()


def test_diff_determiner():
    syncer = GeneralSyncer(
        source={"a": 1, "b": 2}, destination={"b": "2", "c": "3"}
    )

    assert syncer.only_in_source() == [1]
    assert syncer.only_in_destination() == ["3"]


@pytest.mark.parametrize(
    (
        "source_prompts",
        "destination_prompts",
        "delete_prompts",
        "push_prompts",
    ),
    [
        (
            [
                QAPrompt(question="a", answer="a"),
                QAPrompt(question="b", answer="b"),
            ],
            [
                DestinationPrompt(
                    QAPrompt(question="b", answer="b"),
                    destination_id="2",
                ),
                DestinationPrompt(
                    QAPrompt(question="c", answer="c"),
                    destination_id="3",
                ),
            ],
            [
                DestinationPrompt(
                    QAPrompt(question="c", answer="c"),
                    destination_id="3",
                )
            ],
            [PushPrompts([QAPrompt(question="a", answer="a")])],
        )
    ],
)
def test_prompt_diff_determiner(
    diff_determiner: PromptDiffDeterminer,
    source_prompts: Sequence[BasePrompt],
    destination_prompts: Sequence[DestinationPrompt],
    delete_prompts: Sequence[DestinationPrompt],
    push_prompts: Sequence[BasePrompt],
):
    source_prompts = [
        QAPrompt(question="a", answer="a"),
        QAPrompt(question="b", answer="b"),
    ]
    destination_prompts = [
        DestinationPrompt(
            QAPrompt(question="b", answer="b"), destination_id="2"
        ),
        DestinationPrompt(
            QAPrompt(question="c", answer="c"), destination_id="3"
        ),
    ]

    diff = diff_determiner.sync(
        source_prompts=source_prompts,
        destination_prompts=destination_prompts,
    )
    assert diff == [
        DeletePrompts(delete_prompts),
        PushPrompts(push_prompts),
    ]
