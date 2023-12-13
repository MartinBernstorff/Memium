from ..prompt_destination.destination_commands import (
    DeletePrompts,
    PushPrompts,
)
from ..prompts.base_prompt import DestinationPrompt
from ..prompts.qa_prompt import FakeQAPrompt
from .base_diff_determiner import GeneralSyncer, PromptDiffDeterminer


def test_diff_determiner():
    syncer = GeneralSyncer(
        source={"a": 1, "b": 2}, destination={"b": "2", "c": "3"}
    )

    assert syncer.only_in_source() == [1]
    assert syncer.only_in_destination() == ["3"]


def test_prompt_diff_determiner():
    syncer = PromptDiffDeterminer()

    source_prompts = [
        FakeQAPrompt(question="a", answer="a"),
        FakeQAPrompt(question="b", answer="b"),
    ]
    destination_prompts = [
        DestinationPrompt(
            FakeQAPrompt(question="b", answer="b"), destination_id="2"
        ),
        DestinationPrompt(
            FakeQAPrompt(question="c", answer="c"), destination_id="3"
        ),
    ]

    diff = syncer.sync(
        source_prompts=source_prompts,
        destination_prompts=destination_prompts,
    )
    assert diff == [
        DeletePrompts(
            [
                DestinationPrompt(
                    FakeQAPrompt(question="c", answer="c"),
                    destination_id="3",
                )
            ]
        ),
        PushPrompts([FakeQAPrompt(question="a", answer="a")]),
    ]
