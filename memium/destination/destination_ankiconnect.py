import logging
import warnings
from collections.abc import Sequence
from pathlib import Path

import genanki
from iterpy import Iter

from memium.destination.ankiconnect.anki_formatter import AnkiQAFormatter
from memium.destination.ankiconnect.anki_model import AnkiQAModel

from ..utils.hash_cleaned_str import clean_str, hash_str_to_int
from .ankiconnect.anki_converter import AnkiPromptConverter
from .ankiconnect.ankiconnect_gateway import AnkiConnectGateway
from .destination import (
    DeletePrompts,
    DestinationPrompt,
    PromptDestination,
    PromptDestinationCommand,
    PushPrompts,
)

log = logging.getLogger(__name__)


class AnkiConnectDestination(PromptDestination):
    def __init__(
        self,
        gateway: AnkiConnectGateway,
        prompt_converter: AnkiPromptConverter,
        formatter: AnkiQAFormatter,
    ) -> None:
        self.gateway = gateway
        self.prompt_converter = prompt_converter
        self.formatter = formatter

        # Don't care about genanki warnings, have our own tests
        warnings.filterwarnings(
            "ignore", module="genanki", message="^Field contained the following invalid HTML tags"
        )

    @staticmethod
    def dummy(
        gateway: AnkiConnectGateway | None = None,
        prompt_converter: AnkiPromptConverter | None = None,
        formatter: AnkiQAFormatter | None = None,
    ) -> "AnkiConnectDestination":
        return AnkiConnectDestination(
            gateway=AnkiConnectGateway.dummy() if gateway is None else gateway,
            prompt_converter=AnkiPromptConverter.dummy()
            if prompt_converter is None
            else prompt_converter,
            formatter=AnkiQAFormatter(
                Path("memium/destination/ankiconnect/default_styling.css").read_text()
            )
            if formatter is None
            else formatter,
        )

    def get_all_prompts(self) -> Sequence[DestinationPrompt]:
        return (
            Iter(self.gateway.get_all_note_infos())
            .map(self.prompt_converter.from_destination)
            .to_list()
        )

    def _delete_prompts(self, prompts: Sequence[DestinationPrompt]) -> None:
        prompt_ids = {int(remote_prompt.destination_id) for remote_prompt in prompts}
        log.info(f"Deleting {len(prompt_ids)} prompts from Anki")
        for prompt in prompts:
            log.info(f"Deleting prompt: {prompt}")

        self.gateway.delete_notes(list(prompt_ids))

    def _grouped_cards_to_deck(
        self, grouped_cards: tuple[str, Sequence[AnkiQAModel]]
    ) -> genanki.Deck:
        deck_name = grouped_cards[0]
        deck = genanki.Deck(name=deck_name, deck_id=hash_str_to_int(clean_str(deck_name)))

        for card in grouped_cards[1]:
            note = self.formatter.format(card)
            deck.add_note(note)  # type: ignore

        return deck

    def _create_package(self, cards: Sequence[AnkiQAModel]) -> genanki.Package:
        decks = (
            Iter(cards).groupby(lambda card: card.deck).map(self._grouped_cards_to_deck).to_list()
        )

        return genanki.Package(deck_or_decks=decks)

    def _push_prompts(self, command: PushPrompts) -> None:
        notes = [self.prompt_converter.to_destination(e) for e in command.prompts]

        package = self._create_package(notes)

        self._update_models([self.formatter.format(card) for card in notes])

        log.info(f"Pushing {len(notes)} cards to Anki")
        self.gateway.import_package(package)

    def _update_models(self, formatted_cards: Sequence[genanki.Note]) -> None:
        unique_models: dict[int, genanki.Model] = {
            model.model_id: model  # type: ignore
            for model in [n.model for n in formatted_cards]  # type: ignore
        }

        for model in unique_models.values():
            self.gateway.update_model(model)

    def update(self, commands: Sequence[PromptDestinationCommand]) -> None:
        for command in commands:
            match command:
                case DeletePrompts(prompts):
                    self._delete_prompts(prompts)
                case PushPrompts(prompts):
                    self._push_prompts(command)
