from ...source.prompts.prompt import BasePrompt, DestinationPrompt
from ...source.prompts.prompt_qa import QAFromDoc, QAPromptImpl, QAWithoutDoc
from .anki_prompt import AnkiPrompt
from .anki_prompt_qa import AnkiQA
from .ankiconnect_gateway import NoteInfo


class AnkiPromptConverter:
    def __init__(self, base_deck: str, card_css: str, deck_prefix: str = "#anki_deck") -> None:
        self.base_deck = base_deck
        self.deck_prefix = deck_prefix
        self.card_css = card_css

    def prompt_to_card(self, prompt: BasePrompt) -> AnkiPrompt:
        deck_in_tags = [tag for tag in prompt.tags if tag.startswith(self.deck_prefix)]
        deck = deck_in_tags[0] if deck_in_tags else self.base_deck

        match prompt:
            case QAFromDoc():
                return AnkiQA(
                    prompt=prompt.prompt,
                    base_deck=deck,
                    tags=prompt.tags,
                    css=self.card_css,
                    uuid=prompt.scheduling_uid,
                    edit_url=prompt.edit_url,
                    source_title=prompt.parent_doc.title,
                    render_parent_doc=prompt.render_parent_doc,
                )
            case QAWithoutDoc():
                return AnkiQA(
                    prompt=prompt.prompt,
                    base_deck=deck,
                    tags=prompt.tags,
                    css=self.card_css,
                    uuid=prompt.scheduling_uid,
                    edit_url=prompt.edit_url,
                    source_title=None,
                    render_parent_doc=False,
                )
            case BasePrompt():
                raise ValueError("BasePrompt is the base class for all prompts, use a subclass")

    def note_info_to_prompt(self, note_info: NoteInfo) -> DestinationPrompt:
        if "Question" in note_info.fields and "Answer" in note_info.fields:
            return DestinationPrompt(
                QAWithoutDoc(
                    QAPromptImpl(
                        question=note_info.fields["Question"].value,
                        answer=note_info.fields["Answer"].value,
                    ),
                    add_tags=note_info.tags,
                ),
                destination_id=str(note_info.noteId),
            )

        raise ValueError(f"No Question field in note info: {note_info}")
