from collections.abc import Sequence
from typing import Protocol

from personal_mnemonic_medium.data_access.exporters.anki.card_types.base import (
    AnkiCard,
)
from personal_mnemonic_medium.domain.prompt_extractors.prompt import (
    Prompt,
)


class CardExporter(Protocol):
    def prompts_to_cards(
        self, prompts: Sequence[Prompt]
    ) -> Sequence[AnkiCard]:
        ...
