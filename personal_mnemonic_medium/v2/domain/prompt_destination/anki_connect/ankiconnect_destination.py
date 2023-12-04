from collections.abc import Sequence

from personal_mnemonic_medium.domain.prompt_extractors.prompt import (
    Prompt,
)
from personal_mnemonic_medium.v2.domain.prompt_source.destination_commands import (
    DeletePrompts,
    PromptDestinationCommand,
    PushPrompts,
)

from ....data_access.ankiconnect import AnkiConnectGateway
from ..base_prompt_destination import PromptDestination


class AnkiConnectDestination(PromptDestination):
    def __init__(self, ankiconnect_url: str, deck_name: str):
        self.gateway = AnkiConnectGateway(
            ankiconnect_url=ankiconnect_url
        )
        self.deck_name = deck_name

    def get_all_prompts(self) -> Sequence[Prompt]:
        note_infos = self.gateway.get_note_infos(
            deck_name=self.deck_name
        )
        return note_infos

    def _delete_prompts(self, prompts: Sequence[Prompt]) -> None:
        ...

    def _push_prompts(self, prompts: Sequence[Prompt]) -> None:
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
