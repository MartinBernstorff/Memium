from dataclasses import dataclass

from memium.source.prompt import QAPrompt


@dataclass(frozen=True)
class AnkiPrompt:
    prompt: QAPrompt

    source_title: str | None
    edit_url: str | None

    render_parent_doc: bool
