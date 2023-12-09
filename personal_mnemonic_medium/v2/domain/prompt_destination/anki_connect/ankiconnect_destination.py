from collections.abc import Sequence

from functionalpy._sequence import Seq

from personal_mnemonic_medium.v2.domain.prompt_source.destination_commands import (
    DeletePrompts,
    PromptDestinationCommand,
    PushPrompts,
)

from ....data_access.ankiconnect_gateway import (
    AnkiConnectGateway,
    NoteInfo,
)
from ...prompts.base_prompt import BasePrompt
from ...prompts.cloze_prompt import ClozePrompt
from ...prompts.qa_prompt import QAPrompt
from ..base_prompt_destination import PromptDestination


class AnkiConnectDestination(PromptDestination):
    def __init__(self, gateway: AnkiConnectGateway) -> None:
        self.gateway = gateway

    def _note_info_to_prompt(self, note_info: NoteInfo) -> BasePrompt:
        if (
            "Question" in note_info.fields
            and "Answer" in note_info.fields
        ):
            return QAPrompt(
                question=note_info.fields["Question"].value,
                answer=note_info.fields["Answer"].value,
                add_tags=note_info.tags,
            )

        if "Text" in note_info.fields:
            return ClozePrompt(
                text=note_info.fields["Text"].value,
                add_tags=note_info.tags,
            )

        raise ValueError(
            f"NoteInfo {note_info} has neither Question nor Text field"
        )

    def get_all_prompts(self) -> Sequence[BasePrompt]:
        return (
            Seq(self.gateway.get_all_note_infos())
            .map(self._note_info_to_prompt)
            .to_list()
        )

    def _delete_prompts(self, prompts: Sequence[BasePrompt]) -> None:
        prompt_ids = {int(prompt.uid) for prompt in prompts}

        # TODO: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues/284 Figure out how NoteIDs are generated, and how they map to PromptIDs
        self.gateway.delete_notes(list(prompt_ids))

    def _push_prompts(self, prompts: Sequence[BasePrompt]) -> None:
        ...

    def update(
        self, commands: Sequence[PromptDestinationCommand]
    ) -> None:
        for command in commands:
            match command:
                case DeletePrompts(prompts):
                    self._delete_prompts(prompts)
                case PushPrompts(prompts):
                    self._push_prompts(prompts)
