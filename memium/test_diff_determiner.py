from collections.abc import Sequence

import pytest

from memium.source.extractors.test_prompt import FakeQAPrompt

from .destination.destination import DeletePrompts, PushPrompts
from .diff_determiner import GeneralSyncer, PromptDiffDeterminer
from .source.prompts.prompt import BasePrompt, DestinationPrompt
from .source.prompts.prompt_qa import QAWithoutDoc


@pytest.fixture()
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
            example_title="Basic",
            source_prompts=[
                FakeQAPrompt(question="a", answer="a"),
                FakeQAPrompt(question="b", answer="b"),
            ],
            destination_prompts=[
                DestinationPrompt(FakeQAPrompt(question="b", answer="b"), destination_id="2"),
                DestinationPrompt(FakeQAPrompt(question="c", answer="c"), destination_id="3"),
            ],
            delete_prompts=[
                DestinationPrompt(FakeQAPrompt(question="c", answer="c"), destination_id="3")
            ],
            push_prompts=[FakeQAPrompt(question="a", answer="a")],
        ),
        (
            DiffDeterminerExample(
                example_title="Updated tags",
                source_prompts=[QAWithoutDoc(question="a", answer="a", add_tags=["NewTag"])],
                destination_prompts=[
                    DestinationPrompt(
                        QAWithoutDoc(question="a", answer="a", add_tags=["OldTag"]),
                        destination_id="1",
                    )
                ],
                delete_prompts=[],
                push_prompts=[QAWithoutDoc(question="a", answer="a", add_tags=["NewTag"])],
            )
        ),
    ],
)
def test_prompt_diff_determiner(
    diff_determiner: PromptDiffDeterminer, example: DiffDeterminerExample
):
    diff = diff_determiner.sync(
        source_prompts=example.source_prompts, destination_prompts=example.destination_prompts
    )
    assert diff == [DeletePrompts(example.delete_prompts), PushPrompts(example.push_prompts)]
