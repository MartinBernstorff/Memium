from dataclasses import dataclass

from memium.source.prompts.prompt_qa import QAPrompt


@dataclass(frozen=True)
class FakeQAPrompt(QAPrompt):
    @property
    def edit_url(self) -> str:
        return ""
