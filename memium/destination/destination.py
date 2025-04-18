from collections.abc import Sequence
from dataclasses import dataclass
from typing import Protocol, TypeAlias

from memium.source.prompt import QAPrompt, QAWithDoc


@dataclass(frozen=True)
class DestinationPrompt:
    prompt: QAPrompt

    extra: str

    # Destinations can have their own ID-scheme. E.g. Anki assigns a Note id at creation time, which
    # is independent of content. This ID is used to delete or update the note.
    destination_id: str

    @staticmethod
    def dummy(
        prompt: QAWithDoc, extra: str = "DummyExtra", destination_id: str = "DummyDestinationID"
    ) -> "DestinationPrompt":
        return DestinationPrompt(prompt=prompt.prompt, extra=extra, destination_id=destination_id)


@dataclass(frozen=True)
class PushPrompts:
    prompts: Sequence[QAWithDoc]


@dataclass(frozen=True)
class DeletePrompts:
    prompts: Sequence[DestinationPrompt]


PromptDestinationCommand: TypeAlias = PushPrompts | DeletePrompts


class PromptDestination(Protocol):
    def get_all_prompts(self) -> Sequence[DestinationPrompt]: ...

    def update(self, commands: Sequence[PromptDestinationCommand]) -> None: ...
