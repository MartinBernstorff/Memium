from collections.abc import Sequence

import pytest

from .destination.destination import DeletePrompts, PushPrompts
from .diff_determiner import GeneralSyncer, PromptDiffDeterminer
from .source.prompts.prompt import BasePrompt, DestinationPrompt
from .source.prompts.prompt_qa import QAWithoutDoc


@pytest.fixture
def diff_determiner() -> PromptDiffDeterminer:
    return PromptDiffDeterminer()


def test_diff_determiner():
    syncer = GeneralSyncer(source={"a": 1, "b": 2}, destination={"b": "2", "c": "3"})

    assert syncer.only_in_source() == [1]
    assert syncer.only_in_destination() == ["3"]


from dataclasses import dataclass


@dataclass(frozen=True)
class DiffDeterminerExample:
    example_title: str
    source_prompts: Sequence[BasePrompt]
    destination_prompts: Sequence[DestinationPrompt]
    delete_prompts: Sequence[DestinationPrompt]
    push_prompts: Sequence[BasePrompt]


@pytest.mark.parametrize(
    "example",
    [
        DiffDeterminerExample(
            source_prompts=[
                QAWithoutDoc.dummy(question="a", answer="a"),
                QAWithoutDoc.dummy(question="b", answer="b"),
            ],
            destination_prompts=[
                DestinationPrompt(QAWithoutDoc.dummy(question="b", answer="b"), destination_id="2"),
                DestinationPrompt(QAWithoutDoc.dummy(question="c", answer="c"), destination_id="3"),
            ],
            delete_prompts=[
                DestinationPrompt(QAWithoutDoc.dummy(question="c", answer="c"), destination_id="3")
            ],
            push_prompts=[QAWithoutDoc.dummy(question="a", answer="a")],
            example_title="Should push 'a' only in source and delete 'c' only in destination",
        ),
        (
            DiffDeterminerExample(
                source_prompts=[QAWithoutDoc.dummy(tags=["NewTag"])],
                destination_prompts=[
                    DestinationPrompt(QAWithoutDoc.dummy(tags=["OldTag"]), destination_id="1")
                ],
                delete_prompts=[],
                push_prompts=[QAWithoutDoc.dummy(tags=["NewTag"])],
                example_title="Updated tags should result in pushing the prompt",
            )
        ),
    ],
    ids=lambda example: example.example_title,
)
def test_prompt_diff_determiner(
    diff_determiner: PromptDiffDeterminer, example: DiffDeterminerExample
):
    diff = diff_determiner.sync(
        source_prompts=example.source_prompts, destination_prompts=example.destination_prompts
    )
    assert diff[0] == DeletePrompts(example.delete_prompts)
    assert diff[1] == PushPrompts(example.push_prompts)
