from pathlib import Path

from ..prompt_destination.destination_commands import (
    DeletePrompts,
    PushPrompts,
)
from ..prompts.qa_prompt import QAPrompt
from .base_diff_determiner import GeneralSyncer, PromptDiffDeterminer


def test_diff_determiner():
    syncer = GeneralSyncer(
        source={"a": 1, "b": 2}, destination={"b": "2", "c": "3"}
    )

    assert syncer.only_in_source() == [1]
    assert syncer.only_in_destination() == ["3"]


def test_prompt_diff_determiner(tmp_path: Path):
    syncer = PromptDiffDeterminer(
        tmp_read_dir=tmp_path, tmp_write_dir=tmp_path
    )

    source_prompts = [
        QAPrompt(question="a", answer="a"),
        QAPrompt(question="b", answer="b"),
    ]
    destination_prompts = [
        QAPrompt(question="b", answer="b"),
        QAPrompt(question="c", answer="c"),
    ]

    diff = syncer.sync(
        source_prompts=source_prompts,
        destination_prompts=destination_prompts,
    )
    assert diff == [
        DeletePrompts([QAPrompt(question="c", answer="c")]),
        PushPrompts(
            [QAPrompt(question="a", answer="a")],
            tmp_write_dir=tmp_path,
            tmp_read_dir=tmp_path,
        ),
    ]
