from personal_mnemonic_medium.v2.prompt_destination.base_prompt_destination import (
    FakePromptDestination,
)
from personal_mnemonic_medium.v2.prompt_source.base_prompt_source import (
    FakePromptSource,
)
from personal_mnemonic_medium.v2.syncer.base_syncer import FakeSyncer

if __name__ == "__main__":
    source_prompts = FakePromptSource().get_prompts()

    destination = FakePromptDestination()
    destination_prompts = destination.get_all_prompts()

    sync_commands = FakeSyncer().sync(
        source_prompts=source_prompts,
        destination_prompts=destination_prompts,
    )
    destination.update(sync_commands)
