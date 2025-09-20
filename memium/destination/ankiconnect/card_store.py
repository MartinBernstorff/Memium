from collections.abc import Sequence
from dataclasses import dataclass

from iterpy import Arr
from pydantic import BaseModel

from memium.destination.ankiconnect.anki_model import AnkiCardID, AnkiNoteID
from memium.destination.ankiconnect.ankiconnect_requester import AnkiConnectCommand, AnkiRequester


class CardDTO(BaseModel):
    deck_name: str
    model_name: str
    card_id: AnkiCardID
    interval: int
    note: AnkiNoteID


@dataclass
class AnkiCardStore:
    anki_requester: AnkiRequester
    root_deck: str

    def get_all_ids(self) -> Sequence[AnkiCardID]:
        anki_card_ids: Sequence[int] = self.anki_requester.invoke(
            AnkiConnectCommand.FIND_CARDS, query=f'"deck:{self.root_deck}"'
        )
        return Arr(anki_card_ids).map(lambda it: AnkiCardID(it)).to_list()

    def read(self, card_id: AnkiCardID) -> CardDTO:
        anki_cards_info: list[dict[str, str]] = self.anki_requester.invoke(
            AnkiConnectCommand.CARD_INFO, cards=[card_id]
        )

        if len(anki_cards_info) == 0:
            return None

        return CardDTO(
            deck_name=anki_cards_info[0]["deckName"],
            model_name=anki_cards_info[0]["modelName"],
            css=anki_cards_info[0]["css"],
            card_id=AnkiCardID(anki_cards_info[0]["cardId"]),
            interval=anki_cards_info[0]["interval"],
            note=AnkiNoteID(anki_cards_info[0]["note"]),
        )
