from ...source.prompts.prompt import BasePrompt, DestinationPrompt
from ...source.prompts.prompt_cloze import ClozePrompt, ClozeWithoutDoc
from ...source.prompts.prompt_qa import QAPrompt, QAWithoutDoc, RephrasedQAFromDoc
from .anki_prompt import AnkiPrompt
from .anki_prompt_cloze import AnkiCloze
from .anki_prompt_qa import AnkiQA
from .ankiconnect_gateway import NoteInfo


def front_from_rephrased(prompt: RephrasedQAFromDoc) -> str:
    return f"""{prompt.rephrased_question} <span style="opacity: 0.1">(LLM-rephrased)</span>"""


def back_from_rephrased(prompt: RephrasedQAFromDoc) -> str:
    return f"""{prompt.answer} <span style="opacity: 0.1">(LLM-rephrased)</span>
<p style="opacity: 0.1;">Rephrased from: {prompt.question}</p>
"""


class AnkiPromptConverter:
    def __init__(self, base_deck: str, card_css: str, deck_prefix: str = "#anki_deck") -> None:
        self.base_deck = base_deck
        self.deck_prefix = deck_prefix
        self.card_css = card_css

    def prompt_to_card(self, prompt: BasePrompt) -> AnkiPrompt:
        deck_in_tags = [tag for tag in prompt.tags if tag.startswith(self.deck_prefix)]
        deck = deck_in_tags[0] if deck_in_tags else self.base_deck

        match prompt:
            case RephrasedQAFromDoc():
                return AnkiQA(
                    question=front_from_rephrased(prompt),
                    answer=back_from_rephrased(prompt.answer),
                    base_deck=deck,
                    tags=prompt.tags,
                    css=self.card_css,
                    uuid=prompt.scheduling_uid,
                    edit_url=prompt.edit_url,
                )
            case QAPrompt():
                return AnkiQA(
                    question=prompt.question,
                    answer=prompt.answer,
                    base_deck=deck,
                    tags=prompt.tags,
                    css=self.card_css,
                    uuid=prompt.scheduling_uid,
                    edit_url=prompt.edit_url,
                )
            case ClozePrompt():
                return AnkiCloze(
                    text=prompt.text,
                    base_deck=deck,
                    tags=prompt.tags,
                    css=self.card_css,
                    uuid=prompt.scheduling_uid,
                    edit_url=prompt.edit_url,
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
