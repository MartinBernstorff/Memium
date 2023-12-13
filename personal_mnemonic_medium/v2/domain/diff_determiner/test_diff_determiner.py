from ..prompt_destination.destination_commands import (
    DeletePrompts,
    PushPrompts,
)
from ..prompts.base_prompt import DestinationPrompt
from ..prompts.qa_prompt import QAPrompt
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

    diff = syncer.sync(
        source_prompts=source_prompts,
        destination_prompts=destination_prompts,
    )
    assert diff == [
        DeletePrompts(
            [
                DestinationPrompt(
                    QAPrompt(question="c", answer="c"),
                    destination_id="3",
                )
            ]
        ),
        PushPrompts([QAPrompt(question="a", answer="a")]),
    ]
