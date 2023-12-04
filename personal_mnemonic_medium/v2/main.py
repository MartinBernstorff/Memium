from .diff_determiner.base_diff_determiner import FakeDiffDeterminer
from .prompt_destination.base_prompt_destination import (
    FakePromptDestination,
)
from .prompt_source.base_prompt_source import FakePromptSource

if __name__ == "__main__":
    source_prompts = FakePromptSource().get_prompts()

    destination = FakePromptDestination()
    destination_prompts = destination.get_all_prompts()

    sync_commands = FakeDiffDeterminer().sync(
        source_prompts=source_prompts,
        destination_prompts=destination_prompts,
    )
    destination.update(sync_commands)
