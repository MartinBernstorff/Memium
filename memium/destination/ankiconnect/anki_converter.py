from iterpy import Arr

from memium.destination.ankiconnect.anki_model import AnkiQAModel, Markdown

from ...source.prompt import QAWithDoc


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


def _extra_field_content(
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
    def __init__(self, root_deck: str, deck_prefix: str = "anki/deck") -> None:
        self.root_deck = root_deck
        self.deck_prefix = deck_prefix

    @staticmethod
    def dummy() -> "AnkiPromptConverter":
        return AnkiPromptConverter(root_deck="FakeBaseDeck")

    def to_destination(self, prompt: QAWithDoc) -> AnkiQAModel:
        return AnkiQAModel(
            Question=Markdown(prompt.prompt.question),
            Answer=Markdown(prompt.prompt.answer),
            Extra=_extra_field_content(
                source_title=prompt.parent_doc.title,
                edit_url=prompt.edit_url,
                render_parent_doc=prompt.render_parent_doc,
            ),
            tags=Arr(prompt.tags).unique().to_list(),
            raw_prompt=prompt.prompt,
            root_deck=self.root_deck,
            destination_id=None,
            card_ids=[],
        )
