import logging
from collections.abc import Sequence
from dataclasses import dataclass

from iterpy import Arr

from memium.destination.ankiconnect.anki_converter import AnkiPromptConverter
from memium.destination.ankiconnect.anki_model import AnkiNoteID, AnkiQAModel
from memium.destination.ankiconnect.note_store import AnkiNoteStore
from memium.source.prompt import QAWithDoc, SchedulingUID

log = logging.getLogger(__name__)


@dataclass
class Syncer:
    source_prompts: Sequence[QAWithDoc]
    destination_prompts: Sequence[AnkiQAModel]
    converter: AnkiPromptConverter
    note_store: AnkiNoteStore

    def __post_init__(self) -> None:
        self.source_sched_id2source_prompt = {p.scheduling_id: p for p in self.source_prompts}
        self.destination_id2source_prompt = {
            p.raw_prompt.scheduling_uid: p for p in self.destination_prompts
        }

    def sync(self) -> None:
        self._handle_only_in_source()
        self._handle_only_in_destination()
        self._handle_on_both()

    def _update(self, scheduling_id: SchedulingUID):
        source = self.source_sched_id2source_prompt[scheduling_id]
        destination = self.destination_id2source_prompt[scheduling_id]
        converted_source = self.converter.to_destination(source)

        candidate_update = AnkiQAModel(
            Question=converted_source.Question,
            Answer=converted_source.Answer,
            Extra=converted_source.Extra,
            raw_prompt=converted_source.raw_prompt,
            tags=converted_source.tags,
            root_deck=converted_source.root_deck,
            destination_id=destination.destination_id,
            card_ids=destination.card_ids,
        )

        candidate_identity = candidate_update.sync_identity()
        destination_identity = destination.sync_identity()
        needs_update = candidate_identity != destination_identity

        if needs_update:
            self.note_store.update(candidate_update)

    def _handle_on_both(self) -> set[SchedulingUID]:
        common_ids = (
            self.source_sched_id2source_prompt.keys() & self.destination_id2source_prompt.keys()
        )

        Arr(common_ids).map(lambda id_: self._update(id_))

        return common_ids

    def _handle_only_in_source(self) -> Sequence[AnkiNoteID]:
        only_in_source_ids = (
            self.source_sched_id2source_prompt.keys() - self.destination_id2source_prompt.keys()
        )
        notes = Arr(only_in_source_ids).map(
            lambda id_: self.converter.to_destination(self.source_sched_id2source_prompt[id_])
        )

        log.info(f"Creating {len(notes)} new notes in Anki")
        return self.note_store.create(notes.to_list())

    def _handle_only_in_destination(self) -> set[SchedulingUID]:
        only_in_destination_ids = (
            self.destination_id2source_prompt.keys() - self.source_sched_id2source_prompt.keys()
        )
        notes = (
            Arr(only_in_destination_ids)
            .map(lambda id_: self.destination_id2source_prompt[id_])
            .map(lambda it: it.destination_id)
            .to_list()
        )

        note_ids = [it for it in notes if it is not None]

        log.info(f"Deleting {len(note_ids)} notes from Anki")
        self.note_store.delete(note_ids)

        return only_in_destination_ids
