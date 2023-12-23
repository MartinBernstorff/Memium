import logging
from collections.abc import Sequence

from .destination_ankiconnect import AnkiConnectDestination
from .destination_commands import (
    DeletePrompts,
    PromptDestinationCommand,
    PushPrompts,
)

log = logging.getLogger(__name__)


class DryRunDestination(AnkiConnectDestination):
    def update(self, commands: Sequence[PromptDestinationCommand]) -> None:
        for command in commands:
            match command:
                case DeletePrompts(prompts):
                    for prompt in prompts:
                        log.info(f"Deleting prompt: {prompt}\n")
                case PushPrompts(prompts):
                    for prompt in prompts:
                        log.info(f"Pushing prompt: {prompt}\n")
