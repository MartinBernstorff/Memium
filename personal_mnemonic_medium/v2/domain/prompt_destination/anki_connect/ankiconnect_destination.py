from collections.abc import Sequence

from personal_mnemonic_medium.v2.domain.prompt_source.destination_commands import (
    DeletePrompts,
    PromptDestinationCommand,
    PushPrompts,
)

from ....data_access.ankiconnect import AnkiConnectGateway
from ...prompts.base_prompt import BasePrompt
from ..base_prompt_destination import PromptDestination


class AnkiConnectDestination(PromptDestination):
    def __init__(self, gateway: AnkiConnectGateway) -> None:
        self.gateway = gateway

    def get_all_prompts(self) -> Sequence[BasePrompt]:
        note_infos = self.gateway.get_all_note_infos()
        return BasePrompt()

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
