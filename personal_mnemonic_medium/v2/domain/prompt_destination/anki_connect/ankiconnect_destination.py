from collections.abc import Mapping, Sequence

import genanki
from functionalpy._sequence import Seq

from personal_mnemonic_medium.v2.domain.prompt_destination.destination_commands import (
    DeletePrompts,
    PromptDestinationCommand,
    PushPrompts,
)

from ....data_access.ankiconnect_gateway import (
    AnkiConnectGateway,
    NoteInfo,
)
from ...prompts.base_prompt import RemotePrompt
from ...prompts.cloze_prompt import ClozeWithoutDoc
from ...prompts.qa_prompt import QAWithoutDoc
from ..base_prompt_destination import PromptDestination
from .prompt_converter.anki_prompt_converter import (
    AnkiPromptConverter,
)
from .prompt_converter.prompts.base_anki_prompt import AnkiCard


class AnkiConnectDestination(PromptDestination):
    def __init__(
        self,
        gateway: AnkiConnectGateway,
        prompt_converter: AnkiPromptConverter,
    ) -> None:
        self.gateway = gateway
        self.prompt_converter = prompt_converter

    def _note_info_to_prompt(
        self, note_info: NoteInfo
    ) -> RemotePrompt:
        if (
            "Question" in note_info.fields
            and "Answer" in note_info.fields
        ):
            return RemotePrompt(
                QAWithoutDoc(
                    question=note_info.fields["Question"].value,
                    answer=note_info.fields["Answer"].value,
                    add_tags=note_info.tags,
                ),
                remote_id=str(note_info.noteId),
            )

        if "Text" in note_info.fields:
            return RemotePrompt(
                ClozeWithoutDoc(
                    text=note_info.fields["Text"].value,
                    add_tags=note_info.tags,
                ),
                remote_id=str(note_info.noteId),
            )

        raise ValueError(
            f"NoteInfo {note_info} has neither Question nor Text field"
        )

    def get_all_prompts(self) -> Sequence[RemotePrompt]:
        return (
            Seq(self.gateway.get_all_note_infos())
            .map(self._note_info_to_prompt)
            .to_list()
        )

    def _delete_prompts(
        self, prompts: Sequence[RemotePrompt]
    ) -> None:
        prompt_ids = {
            int(remote_prompt.prompt.uid) for remote_prompt in prompts
        }
        self.gateway.delete_notes(list(prompt_ids))

    def _grouped_cards_to_deck(
        self, cards: Mapping[str, Sequence[AnkiCard]]
    ) -> genanki.Deck:
        deck_name = next(iter(cards.keys()))
        deck = genanki.Deck(name=deck_name, deck_id=deck_name)

        for card in cards[deck_name]:
            deck.add_note(card.to_genanki_note())  # type: ignore

        return deck

    def _create_package(
        self, cards: Sequence[AnkiCard]
    ) -> genanki.Package:
        cards_grouped_by_deck = Seq(cards).groupby(
            lambda card: card.deck
        )
        decks = (
            Seq([cards_grouped_by_deck])
            .map(self._grouped_cards_to_deck)
            .to_list()
        )

        return genanki.Package(deck_or_decks=decks)

    def _push_prompts(self, command: PushPrompts) -> None:
        cards = self.prompt_converter.prompts_to_cards(
            command.prompts
        )

        models = {card.genanki_model for card in cards}
        for model in models:
            self.gateway.update_model(model)

        package = self._create_package(cards)

        self.gateway.import_package(package)

    def update(
        self, commands: Sequence[PromptDestinationCommand]
    ) -> None:
        for command in commands:
            match command:
                case DeletePrompts(prompts):
                    self._delete_prompts(prompts)
                case PushPrompts(prompts):
                    self._push_prompts(command)
