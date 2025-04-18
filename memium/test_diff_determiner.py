from collections.abc import Sequence

import pytest

from memium.source.document import Document
from memium.source.prompt import QAWithDoc

from .destination.destination import DestinationPrompt
from .diff_determiner import GeneralSyncer, PromptDiffDeterminer


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
    source_prompts: Sequence[QAWithDoc]
    destination_prompts: Sequence[DestinationPrompt]
    should_delete_prompts: Sequence[DestinationPrompt]


@pytest.mark.parametrize(
    "example",
    [
        DiffDeterminerExample(
            source_prompts=[
                QAWithDoc.dummy(question="a", answer="a"),
                QAWithDoc.dummy(question="b", answer="b"),
            ],
            destination_prompts=[
                DestinationPrompt.dummy(
                    QAWithDoc.dummy(question="b", answer="b"), destination_id="2"
                ),
                DestinationPrompt.dummy(
                    QAWithDoc.dummy(question="c", answer="c"), destination_id="3"
                ),
            ],
            should_delete_prompts=[
                DestinationPrompt.dummy(
                    QAWithDoc.dummy(question="c", answer="c"), destination_id="3"
                )
            ],
            example_title="Should delete 'c' only in destination",
        ),
        (
            DiffDeterminerExample(
                source_prompts=[QAWithDoc.dummy(parent_doc=Document.dummy(tags=["#NewTag"]))],
                destination_prompts=[
                    DestinationPrompt.dummy(
                        QAWithDoc.dummy(parent_doc=Document.dummy(tags=["OldTag"])),
                        destination_id="1",
                    )
                ],
                should_delete_prompts=[],
                example_title="Updated tags should not delete",
            )
        ),
    ],
    ids=lambda example: example.example_title,
)
def test_prompt_diff_determiner(
    diff_determiner: PromptDiffDeterminer, example: DiffDeterminerExample
):
    to_delete = diff_determiner.to_delete(
        source_prompts=example.source_prompts, destination_prompts=example.destination_prompts
    )
    assert to_delete == example.should_delete_prompts
