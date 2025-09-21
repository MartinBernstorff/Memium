from collections.abc import Sequence
from dataclasses import dataclass

from iterpy import Arr
from pydantic import BaseModel

from memium.destination.ankiconnect.anki_model import AnkiCardID
from memium.destination.ankiconnect.ankiconnect_requester import AnkiConnectCommand, AnkiRequester


class CardDTO(BaseModel):
    deckName: str


@dataclass
class AnkiCardStore:
    anki_requester: AnkiRequester
    root_deck: str

    def get_all_ids(self) -> Sequence[AnkiCardID]:
        anki_card_ids: Sequence[int] = self.anki_requester.invoke(
            AnkiConnectCommand.FIND_CARDS, query=f'"deck:{self.root_deck}"'
        )
        return Arr(anki_card_ids).map(lambda it: AnkiCardID(it)).to_list()

    def read(self, card_id: AnkiCardID) -> CardDTO | None:
        anki_cards_info: list[dict[str, str]] = self.anki_requester.invoke(
            AnkiConnectCommand.CARD_INFO, cards=[card_id]
        )

        if len(anki_cards_info) == 0:
            return None

        return CardDTO(**anki_cards_info[0])
