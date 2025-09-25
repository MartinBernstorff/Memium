import logging
from collections.abc import Sequence
from dataclasses import dataclass

from iterpy import Arr
from pydantic import BaseModel

from memium.destination.ankiconnect import card_store
from memium.destination.ankiconnect.anki_model import AnkiCardID, AnkiNoteID, AnkiQAModel
from memium.destination.ankiconnect.ankiconnect_requester import AnkiConnectCommand, AnkiRequester
from memium.utils.markdown import md_to_html

log = logging.getLogger(__name__)


class AnkiFieldDTO(BaseModel):
    value: str


class AnkiNoteInfoDTO(BaseModel):
    noteId: int
    fields: dict[str, AnkiFieldDTO]
    tags: Sequence[str]
    cards: Sequence[int]


class AnkiRawFieldsDTO(BaseModel):
    Question: str  # p2: Make it clear that these are HTML?
    Answer: str
    Extra: str
    raw_question: str
    raw_answer: str


class AnkiNoteOptionsDTO(BaseModel):
    allowDuplicate: bool


class AnkiRawDTO(BaseModel):
    deckName: str  # p2: NewType
    modelName: str
    fields: AnkiRawFieldsDTO
    tags: Sequence[str]
    options: AnkiNoteOptionsDTO | None


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

    def get_all_ids(self) -> Sequence[AnkiNoteID]:
        anki_card_ids = self.card_store.get_all_ids()

        # get a list of anki notes in the deck
        anki_note_ids: list[int] = self.anki_requester.invoke(
            AnkiConnectCommand.CARDS_TO_NOTES, cards=Arr(anki_card_ids).map(int).to_list()
        )

        return [AnkiNoteID(it) for it in anki_note_ids]

    def get_all_sans_decks(self) -> Sequence[AnkiQAModel]:
        note_ids = self.get_all_ids()
        return self.read(note_ids)

    def clear(self) -> None:
        note_ids = self.get_all_ids()
        self.delete(note_ids)

    def create(self, note: Sequence[AnkiQAModel]) -> Sequence[AnkiNoteID]:
        # p2: Ensure note model exists
        # p2: Ensure deck exists
        # p3: include css (where?)
        # Create the note

        # bug: we used to use just self.root_deck here, ignoring the deck from the AnkiQAModel
        # Not sure how to avoid bugs in these mapping situations, other than:
        # * Making the mapping a separate function, so there is no available context that you shouldn't use
        # * Writing tests
        # * Would NewTypes have helped here?

        # bug: seems to detect duplicates for the "reversed" definition prompts. Not sure why.
        dtos = Arr(note).map(
            lambda it: AnkiRawDTO(
                deckName=it.deck,
                modelName="Ankdown QA with raw text",
                fields=AnkiRawFieldsDTO(
                    Question=md_to_html(it.Question),
                    Answer=md_to_html(it.Answer),
                    Extra=md_to_html(it.Extra),
                    raw_question=it.raw_prompt.question,
                    raw_answer=it.raw_prompt.answer,
                ),
                options=AnkiNoteOptionsDTO(allowDuplicate=True),
                # Anki's duplicate checking is over-eager, ignoring e.g. the "extra" field.
                # Since it contains the note title in my modelling, a duplicate on the question field may, in fact,
                # contain enough context in the Extra field to not be a true duplicate.
                # Perhaps this indicates that the note title should be in the question field, but that would trigger _a lot_ of rescheduling for me.
                tags=it.tags,
            )
        )

        ids = dtos.map(
            lambda it: self.anki_requester.invoke(
                action=AnkiConnectCommand.ADD_NOTE, note=it.model_dump()
            )
        ).map(lambda it: AnkiNoteID(it))

        return ids.to_list()

    def read(self, note_ids: Sequence[AnkiNoteID]) -> Sequence[AnkiQAModel]:
        response = self.anki_requester.invoke(AnkiConnectCommand.GET_NOTE_INFOS, notes=note_ids)

        if len(response) == 0 or response == [{}]:
            return []

        anki_notes_info: Sequence[AnkiNoteInfoDTO] = [AnkiNoteInfoDTO(**it) for it in response]

        return Arr(anki_notes_info).map(self._prepare_note_from_info).to_list()

    def _prepare_note_from_info(
        self, note_info: AnkiNoteInfoDTO, get_deck: bool = False
    ) -> AnkiQAModel:
        # Allows skipping deck fetch for batch operations
        if get_deck:
            card = self.card_store.read(AnkiCardID(note_info.cards[0]))
            gotten_deck = None if card is None else card.deckName
            deck = self.root_deck if gotten_deck is None else gotten_deck
        else:
            deck = self.root_deck

        return AnkiQAModel.from_primitives(
            question=note_info.fields["Question"].value,
            answer=note_info.fields["Answer"].value,
            extra=note_info.fields["Extra"].value,
            raw_question=note_info.fields["raw_question"].value,
            raw_answer=note_info.fields["raw_answer"].value,
            tags=note_info.tags,
            root_deck=deck,
            destination_id=AnkiNoteID(note_info.noteId),
            card_ids=[AnkiCardID(it) for it in note_info.cards],
        )

    def update(self, note: AnkiQAModel) -> None:
        # Update deck, https://git.sr.ht/~foosoft/anki-connect#codechangedeckcode
        # "params": {  # noqa: ERA001
        #     "cards": [1502098034045, 1502098034048, 1502298033753],  # noqa: ERA001
        #     "deck": "Japanese::JLPT N3"
        # }
        if note.destination_id is None:
            raise ValueError("Note must have a destination_id to be updated")

        destination_note = self.read([note.destination_id])[0]
        if not destination_note.card_ids:
            raise ValueError(f"Note {note.destination_id} has no associated cards")

        log.info(f"Updating note with Question: {note.Question}")

        self.anki_requester.invoke(
            action=AnkiConnectCommand.CHANGE_DECK, cards=destination_note.card_ids, deck=note.deck
        )

        # Update fields and tags
        dto = AnkiUpdateDTO(
            id=note.destination_id,
            fields=AnkiRawFieldsDTO(
                Question=md_to_html(note.Question),
                Answer=md_to_html(note.Answer),
                Extra=md_to_html(note.Extra),
                raw_question=note.raw_prompt.question,
                raw_answer=note.raw_prompt.answer,
            ),
            tags=note.tags,
        )

        self.anki_requester.invoke(action=AnkiConnectCommand.UPDATE_NOTE, note=dto.model_dump())

        # Have to update tags separately, because if a tag list is empty, it is _not_ removed when calling UPDATE_NOTE
        self.anki_requester.invoke(
            action=AnkiConnectCommand.UPDATE_NOTE_TAGS, note=dto.id, tags=dto.tags
        )

    def delete(self, note_ids: Sequence[AnkiNoteID]) -> None:
        if len(note_ids) == 0:
            return

        self.anki_requester.invoke(AnkiConnectCommand.DELETE_NOTES, notes=note_ids)
