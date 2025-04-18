from memium.destination.ankiconnect.anki_model import AnkiQAModel, Markdown

from ...source.prompts.prompt import BasePrompt, DestinationPrompt
from ...source.prompts.prompt_qa import QAFromDoc, QAPromptImpl, QAWithoutDoc
from .ankiconnect_gateway import NoteInfo


def _edit_button(url: str) -> str:
    return f"""<a href="{url}" style="background-color: #5f0069;
        border: none;
        color: white;
        padding: 0.8em;
        text-align: center;
        text-decoration: none;
        font-size: 0.8em;
        font-family: 'Inter', sans-serif;
        border-radius: 8px;
        opacity: 0.8;
">Obsidian</a>"""


def extra_field_content(
    source_title: str | None, edit_url: str | None, render_parent_doc: bool
) -> Markdown:
    note_title = (
        f"<span style='opacity: 0.5; font-size: 0.7em; line-height: 0%;'>{source_title}</span>"
        if source_title and render_parent_doc
        else ""
    )
    edit_button_html = _edit_button(edit_url) if edit_url else ""
    return Markdown(
        f"<div class='edit_button' style='text-align: center;'>{edit_button_html}</div>{note_title}"
    )


class AnkiPromptConverter:
    def __init__(self, root_deck: str, deck_prefix: str = "#anki_deck") -> None:
        self.root_deck = root_deck
        self.deck_prefix = deck_prefix

    @staticmethod
    def dummy() -> "AnkiPromptConverter":
        return AnkiPromptConverter(root_deck="FakeBaseDeck")

    def to_destination(self, prompt: BasePrompt) -> AnkiQAModel:
        deck_in_tags = [tag for tag in prompt.tags if tag.startswith(self.deck_prefix)]
        deck = deck_in_tags[0] if deck_in_tags else self.root_deck
        match prompt:
            case QAFromDoc():
                return AnkiQAModel(
                    Question=Markdown(prompt.prompt.question),
                    Answer=Markdown(prompt.prompt.answer),
                    Extra=extra_field_content(
                        source_title=prompt.parent_doc.title,
                        edit_url=prompt.edit_url,
                        render_parent_doc=prompt.render_parent_doc,
                    ),
                    UUID=Markdown(str(prompt.prompt.scheduling_uid)),
                    tags=prompt.tags,
                    raw_prompt=prompt.prompt,
                    root_deck=deck,
                )
            case QAWithoutDoc():
                return AnkiQAModel(
                    Question=Markdown(prompt.prompt.question),
                    Answer=Markdown(prompt.prompt.answer),
                    Extra=extra_field_content(
                        source_title=None, edit_url=prompt.edit_url, render_parent_doc=False
                    ),
                    UUID=Markdown(str(prompt.prompt.scheduling_uid)),
                    tags=prompt.tags,
                    raw_prompt=prompt.prompt,
                    root_deck=deck,
                )
            case BasePrompt():
                raise ValueError("BasePrompt is the base class for all prompts, use a subclass")

    def from_destination(self, note_info: NoteInfo) -> DestinationPrompt:
        if "Question" in note_info.fields and "Answer" in note_info.fields:
            return DestinationPrompt(
                QAWithoutDoc(
                    QAPromptImpl(
                        question=note_info.fields["raw_question"].value,
                        answer=note_info.fields["raw_answer"].value,
                    ),
                    add_tags=note_info.tags,
                ),
                destination_id=str(note_info.noteId),
            )

        raise ValueError(f"No Question field in note info: {note_info}")
