from collections.abc import Mapping, Sequence

import genanki
from functionalpy._sequence import Seq

from ..data_access.ankiconnect_gateway import AnkiConnectGateway, NoteInfo
from ..source.prompts.prompt import DestinationPrompt
from ..source.prompts.prompt_cloze import ClozeWithoutDoc
from ..source.prompts.prompt_qa import QAWithoutDoc
from ..utils.hash_cleaned_str import hash_cleaned_str
from .ankiconnect.anki_card import AnkiCard
from .ankiconnect.anki_converter import AnkiPromptConverter
from .destination import PromptDestination
from .destination_commands import (
    DeletePrompts,
    PromptDestinationCommand,
    PushPrompts,
)


class AnkiConnectDestination(PromptDestination):
    def __init__(
        self, gateway: AnkiConnectGateway, prompt_converter: AnkiPromptConverter
    ) -> None:
        self.gateway = gateway
        self.prompt_converter = prompt_converter

    def _note_info_to_prompt(self, note_info: NoteInfo) -> DestinationPrompt:
        if "Question" in note_info.fields and "Answer" in note_info.fields:
            return DestinationPrompt(
                QAWithoutDoc(
                    question=note_info.fields["Question"].value,
                    answer=note_info.fields["Answer"].value,
                    add_tags=note_info.tags,
                ),
                destination_id=str(note_info.noteId),
            )

        if "Text" in note_info.fields:
            return DestinationPrompt(
                ClozeWithoutDoc(
                    text=note_info.fields["Text"].value, add_tags=note_info.tags
                ),
                destination_id=str(note_info.noteId),
            )

        raise ValueError(
            f"NoteInfo {note_info} has neither Question nor Text field"
        )

    def get_all_prompts(self) -> Sequence[DestinationPrompt]:
        return (
            Seq(self.gateway.get_all_note_infos())
            .map(self._note_info_to_prompt)
            .to_list()
        )

    def _delete_prompts(self, prompts: Sequence[DestinationPrompt]) -> None:
        prompt_ids = {
            int(remote_prompt.destination_id) for remote_prompt in prompts
        }
        self.gateway.delete_notes(list(prompt_ids))

    def _grouped_cards_to_deck(
        self, grouped_cards: Mapping[str, Sequence[AnkiCard]]
    ) -> genanki.Deck:
        deck_name = next(iter(grouped_cards.keys()))
        deck = genanki.Deck(name=deck_name, deck_id=hash_cleaned_str(deck_name))

        for card in grouped_cards[deck_name]:
            deck.add_note(card.to_genanki_note())  # type: ignore

        return deck

    def _create_package(self, cards: Sequence[AnkiCard]) -> genanki.Package:
        cards_grouped_by_deck = Seq(cards).groupby(lambda card: card.deck)
        decks = [
            self._grouped_cards_to_deck({group: cards_grouped_by_deck[group]})
            for group in cards_grouped_by_deck
        ]

        return genanki.Package(deck_or_decks=decks)

    def _push_prompts(self, command: PushPrompts) -> None:
        cards = self.prompt_converter.prompts_to_cards(command.prompts)

        models = [card.genanki_model for card in cards]
        unique_models: dict[int, genanki.Model] = {
            model.model_id: model  # type: ignore
            for model in models  # type: ignore
        }

        for model in unique_models.values():
            self.gateway.update_model(model)

        package = self._create_package(cards)

        self.gateway.import_package(package)

    def update(self, commands: Sequence[PromptDestinationCommand]) -> None:
        for command in commands:
            match command:
                case DeletePrompts(prompts):
                    self._delete_prompts(prompts)
                case PushPrompts(prompts):
                    self._push_prompts(command)
