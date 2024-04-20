import pytest

from ...source.prompts.prompt import BasePrompt, DestinationPrompt
from ...source.prompts.prompt_cloze import ClozePrompt, ClozeWithoutDoc
from ...source.prompts.prompt_qa import QAPrompt, QAWithoutDoc
from .anki_cloze import AnkiCloze
from .anki_gateway import NoteInfo
from .anki_prompt import AnkiPrompt
from .anki_qa import AnkiQA, FakeAnkiCloze, FakeAnkiQA


@pytest.mark.parametrize(
    ("input_prompt", "expected_card"),
    [
        (
            QAWithoutDoc(question="FakeQuestion", answer="FakeAnswer", add_tags=["FakeTag"]),
            FakeAnkiQA(
                uuid=4875918425
            ),  # Ensure that UUID generation remains stable to retain idempotency over time
        ),
        (
            ClozeWithoutDoc(text="FakeText", add_tags=["FakeTag"]),
            FakeAnkiCloze(
                uuid=1873301177
            ),  # Ensure that UUID generation remains stable to retain idempotency over time
        ),
    ],
)
def should_convert_to_cards(input_prompt: BasePrompt, expected_card: AnkiPrompt):
    """Tests the AnkiPromptConverter class"""
    generated_card = AnkiPromptConverter(
        base_deck="FakeBaseDeck", card_css="FakeCSS"
    ).prompt_to_card(input_prompt)

    assert generated_card.uuid == expected_card.uuid


class AnkiPromptConverter:
    def __init__(self, base_deck: str, card_css: str, deck_prefix: str = "#anki_deck") -> None:
        self.base_deck = base_deck
        self.deck_prefix = deck_prefix
        self.card_css = card_css

    def prompt_to_card(self, prompt: BasePrompt) -> AnkiPrompt:
        deck_in_tags = [tag for tag in prompt.tags if tag.startswith(self.deck_prefix)]
        deck = deck_in_tags[0] if deck_in_tags else self.base_deck

        match prompt:
            case QAPrompt():
                return AnkiQA(
                    question=prompt.question,
                    answer=prompt.answer,
                    base_deck=deck,
                    tags=prompt.tags,
                    css=self.card_css,
                    uuid=prompt.scheduling_uid,
                )
            case ClozePrompt():
                return AnkiCloze(
                    text=prompt.text,
                    base_deck=deck,
                    tags=prompt.tags,
                    css=self.card_css,
                    uuid=prompt.scheduling_uid,
                )
            case BasePrompt():
                raise ValueError("BasePrompt is the base class for all prompts, use a subclass")

    def note_info_to_prompt(self, note_info: NoteInfo) -> DestinationPrompt:
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
                ClozeWithoutDoc(text=note_info.fields["Text"].value, add_tags=note_info.tags),
                destination_id=str(note_info.noteId),
            )

        raise ValueError(f"NoteInfo {note_info} has neither Question nor Text field")
