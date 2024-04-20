import logging
from collections.abc import Mapping, Sequence

import genanki
import pytest
from iterpy import Iter

from ..source.prompts.prompt import DestinationPrompt
from ..source.prompts.prompt_cloze import ClozeWithoutDoc
from ..source.prompts.prompt_qa import QAWithoutDoc
from ..str_utils.cleaner import clean_str
from ..str_utils.hasher import hash_str_to_int
from .ankiconnect.anki_converter import AnkiPromptConverter
from .ankiconnect.anki_gateway import (
    AnkiConnectGateway,
    AnkiField,
    ImportPackage,
    MockNoteInfo,
    SpieAnkiconnectGateway,
    UpdateModel,
)
from .ankiconnect.anki_prompt import AnkiPrompt
from .destination import DeletePrompts, PromptDestination, PromptDestinationCommand, PushPrompts

log = logging.getLogger(__name__)


class AnkiConnectDestination(PromptDestination):
    def __init__(self, gateway: AnkiConnectGateway, prompt_converter: AnkiPromptConverter) -> None:
        self.gateway = gateway
        self.prompt_converter = prompt_converter

    def get_all_prompts(self) -> Sequence[DestinationPrompt]:
        return (
            Iter(self.gateway.get_all_note_infos())
            .map(self.prompt_converter.note_info_to_prompt)
            .to_list()
        )

    def _delete_prompts(self, prompts: Sequence[DestinationPrompt]) -> None:
        prompt_ids = {int(remote_prompt.destination_id) for remote_prompt in prompts}
        self.gateway.delete_notes(list(prompt_ids))

    def _grouped_cards_to_deck(
        self, grouped_cards: tuple[str, Sequence[AnkiPrompt]]
    ) -> genanki.Deck:
        deck_name = grouped_cards[0]
        deck = genanki.Deck(name=deck_name, deck_id=hash_str_to_int(clean_str(deck_name)))

        for card in grouped_cards[1]:
            deck.add_note(card.to_genanki_note())  # type: ignore

        return deck

    def _create_package(self, cards: Sequence[AnkiPrompt]) -> genanki.Package:
        decks = (
            Iter(cards).groupby(lambda card: card.deck).map(self._grouped_cards_to_deck).to_list()
        )

        return genanki.Package(deck_or_decks=decks)

    def _push_prompts(self, command: PushPrompts) -> None:
        cards = [self.prompt_converter.prompt_to_card(e) for e in command.prompts]

        models = [card.genanki_model for card in cards]
        unique_models: dict[int, genanki.Model] = {
            model.model_id: model  # type: ignore
            for model in models  # type: ignore
        }

        for model in unique_models.values():
            self.gateway.update_model(model)

        package = self._create_package(cards)

        log.info(f"Pushing {len(cards)} cards to Anki")
        self.gateway.import_package(package)

    def update(self, commands: Sequence[PromptDestinationCommand]) -> None:
        for command in commands:
            match command:
                case DeletePrompts(prompts):
                    self._delete_prompts(prompts)
                case PushPrompts(prompts):
                    self._push_prompts(command)


@pytest.mark.parametrize(
    ("fields"),
    [
        ({"Text": AnkiField(value="MockText", order=0)}),
        (
            {
                "Question": AnkiField(value="MockQuestion", order=0),
                "Answer": AnkiField(value="MockAnswer", order=1),
            }
        ),
        pytest.param(
            ({"UnknownField": AnkiField(value="MockText", order=0)}), marks=pytest.mark.xfail
        ),
    ],
)
def test_ankiconnect_get_all_prompts(fields: Mapping[str, AnkiField]):
    dest = AnkiConnectDestination(
        gateway=SpieAnkiconnectGateway(note_infos=[MockNoteInfo(fields=fields)]),
        prompt_converter=AnkiPromptConverter(base_deck="FakeDeck", card_css="FakeCSS"),
    )
    prompts = dest.get_all_prompts()

    assert len(prompts) == 1


def test_ankiconnect_push_prompts():
    gateway = SpieAnkiconnectGateway()
    dest = AnkiConnectDestination(
        gateway=gateway,
        prompt_converter=AnkiPromptConverter(base_deck="FakeDeck", card_css="FakeCSS"),
    )
    dest.update(
        [
            PushPrompts(
                prompts=[
                    QAWithoutDoc(
                        question="FakeQuestion",
                        answer="FakeAnswer",
                        add_tags=["anki/deck/FakeSubdeck/FakeSubSubdeck"],
                    ),
                    ClozeWithoutDoc(text="FakeText", add_tags=["FakeTag"]),
                ]
            )
        ]
    )

    expected_commands = [(ImportPackage, 1), (UpdateModel, 2)]
    import_package_command = next(
        c for c in gateway.executed_commands if isinstance(c, ImportPackage)
    )
    assert (
        import_package_command.package.decks[0].name  # type: ignore
        == "FakeDeck::FakeSubdeck::FakeSubSubdeck"
    )
    assert len(import_package_command.package.decks) == 2  # type: ignore

    for command in expected_commands:
        assert (
            len([c for c in gateway.executed_commands if isinstance(c, command[0])]) == command[1]
        )
