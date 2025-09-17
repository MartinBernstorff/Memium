import logging
from collections.abc import Sequence

from iterpy import Arr

from .destination import DeletePrompts, PromptDestinationCommand, PushPrompts
from .destination_ankiconnect import AnkiConnectDestination

log = logging.getLogger(__name__)


class DryRunDestination(AnkiConnectDestination):
    def update(self, commands: Sequence[PromptDestinationCommand]) -> None:
        # for command in commands:
        #     match command:
        #         case DeletePrompts(prompts):
        #             for prompt in prompts:
        #                 log.info(f"Deleting prompt: {prompt}\n")
        #         case PushPrompts(prompts):
        #             for prompt in prompts:
        #                 log.info(f"Pushing prompt: {prompt}\n")

        deletions = (
            Arr(commands)
            .filter(lambda c: isinstance(c, DeletePrompts))
            .map(lambda x: len(x.prompts))
        )
        pushes = (
            Arr(commands).filter(lambda c: isinstance(c, PushPrompts)).map(lambda x: len(x.prompts))
        )

        log.info(f"Deleted {deletions}, pushed {pushes} prompts in dry run mode.")
