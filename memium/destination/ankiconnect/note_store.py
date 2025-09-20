import logging
from collections.abc import Sequence
from dataclasses import dataclass

from iterpy import Arr
from pydantic import BaseModel

from memium.destination.ankiconnect import card_store
from memium.destination.ankiconnect.anki_model import AnkiCardID, AnkiNoteID, AnkiQAModel
from memium.destination.ankiconnect.ankiconnect_requester import AnkiConnectCommand, AnkiRequester

log = logging.getLogger(__name__)


class AnkiRawFieldsDTO(BaseModel):
    Question: str
    Answer: str
    Extra: str
    raw_question: str
    raw_answer: str


class AnkiRawDTO(BaseModel):
    noteId: int | None = None
    deckName: str
    modelName: str
    fields: AnkiRawFieldsDTO
    tags: Sequence[str]


class AnkiUpdateDTO(BaseModel):
    id: AnkiNoteID
    fields: AnkiRawFieldsDTO
    tags: Sequence[str]


@dataclass
class AnkiNoteStore:
    anki_requester: AnkiRequester
    root_deck: str

    def __post_init__(self) -> None:
        self.card_store = card_store.AnkiCardStore(
            anki_requester=self.anki_requester, root_deck=self.root_deck
        )

    def get_all(self) -> Sequence[AnkiNoteID]:
        anki_card_ids = self.card_store.get_all_ids()

        # get a list of anki notes in the deck
        anki_note_ids: list[int] = self.anki_requester.invoke(
            AnkiConnectCommand.CARDS_TO_NOTES, cards=Arr(anki_card_ids).map(int).to_list()
        )

        return [AnkiNoteID(it) for it in anki_note_ids]

    def clear(self) -> None:
        note_ids = self.get_all()
        self.delete(note_ids)

    def create(self, note: Sequence[AnkiQAModel]) -> Sequence[AnkiNoteID]:
        # p2: Ensure note model exists
        # p2: Ensure deck exists
        # Create the note

        dtos = (
            Arr(note)
            .map(
                lambda it: AnkiRawDTO(
                    deckName=self.root_deck,
                    modelName="Ankdown QA with raw text",
                    fields=AnkiRawFieldsDTO(
                        Question=it.Question,
                        Answer=it.Answer,
                        Extra=it.Extra,
                        raw_question=it.raw_prompt.question,
                        raw_answer=it.raw_prompt.answer,
                    ),
                    tags=it.tags,
                )
            )
            .map(
                lambda it: self.anki_requester.invoke(
                    action=AnkiConnectCommand.ADD_NOTE, note=it.model_dump()
                )
            )
            .map(lambda it: AnkiNoteID(it))
            .to_list()
        )

        return dtos

    def read(self, note_id: AnkiNoteID) -> AnkiQAModel | None:
        anki_notes_info: list[dict[str, Any]] = self.anki_requester.invoke(
            AnkiConnectCommand.GET_NOTE_INFOS, notes=[note_id]
        )

        if len(anki_notes_info) == 0:
            return None

        fields = anki_notes_info[0]["fields"] if len(anki_notes_info) > 0 else None
        card_ids = anki_notes_info[0].get("cards", None) if len(anki_notes_info) > 0 else None
        cards = self.card_store.read(AnkiCardID(card_ids[0]))

        return AnkiQAModel.from_primitives(
            question=fields["Question"]["value"],
            answer=fields["Answer"]["value"],
            extra=fields["Extra"]["value"],
            raw_question=fields["raw_question"]["value"],
            raw_answer=fields["raw_answer"]["value"],
            tags=anki_notes_info[0]["tags"],
            root_deck=cards.deck_name,
            destination_id=AnkiNoteID(anki_notes_info[0]["noteId"]),
            card_ids=[AnkiCardID(it) for it in card_ids] if card_ids is not None else None,
        )

    def update(self, note: AnkiQAModel) -> None:
        # Update deck, https://git.sr.ht/~foosoft/anki-connect#codechangedeckcode
        # "params": {  # noqa: ERA001
        #     "cards": [1502098034045, 1502098034048, 1502298033753],  # noqa: ERA001
        #     "deck": "Japanese::JLPT N3"
        # }
        if note.destination_id is None:
            raise ValueError("Note must have a destination_id to be updated")

        destination_note = self.read(note.destination_id)
        if destination_note is None:
            raise ValueError(f"Note with id {note.destination_id} does not exist in Anki")
        if destination_note.card_ids is None:
            raise ValueError(f"Note {note.destination_id} has no associated cards")

        self.anki_requester.invoke(
            action=AnkiConnectCommand.CHANGE_DECK, cards=destination_note.card_ids, deck=note.deck
        )

        # Update fields and tags
        dto = AnkiUpdateDTO(
            id=note.destination_id,
            fields=AnkiRawFieldsDTO(
                Question=note.Question,
                Answer=note.Answer,
                Extra=note.Extra,
                raw_question=note.raw_prompt.question,
                raw_answer=note.raw_prompt.answer,
            ),
            tags=note.tags,
        )

        self.anki_requester.invoke(action=AnkiConnectCommand.UPDATE_NOTE, note=dto.model_dump())

    def delete(self, note_ids: Sequence[AnkiNoteID]) -> None:
        if len(note_ids) == 0:
            return

        self.anki_requester.invoke(AnkiConnectCommand.DELETE_NOTES, notes=note_ids)
