from dataclasses import dataclass

from memium.source.prompts.prompt_qa import QAPromptImpl


@dataclass(frozen=True)
class AnkiPrompt:
    prompt: QAPromptImpl

    source_title: str | None
    edit_url: str | None

    render_parent_doc: bool

    @property
    def uuid(self) -> int:
        return self.prompt.scheduling_uid
