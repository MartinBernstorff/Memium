import enum
import logging
import os
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path

import instructor
from iterpy import Arr
from joblib import Memory
from pydantic import BaseModel

from memium.source.prompt import QAWithDoc

log = logging.getLogger(__name__)


class CategoryValue(enum.Enum):
    SWE = "Software"
    MEDICINE = "Medicine"
    OTHER = "Other"


class Category(BaseModel):
    value: CategoryValue


api_key = os.getenv("OPENAI_API_KEY")
client = instructor.from_provider("openai/gpt-4.1-nano", api_key=api_key)


def _process_prompts(prompt: QAWithDoc) -> QAWithDoc:
    # 'version' kept for future behavioural changes; underscore assignment silences unused warning
    response: Category = client.chat.completions.create(
        response_model=Category,
        messages=[
            {
                "role": "user",
                "content": (
                    f"This is a flashcard from a note called {prompt.parent_doc.title}. "
                    f"{prompt.prompt.question} | {prompt.prompt.answer}. "
                    f"What is this flashcard about? Choose one of the following categories (måske på dansk): "
                ),
            }
        ],
    )  # type: ignore

    tags = ["anki/deck/" + response.value.value]
    msg = f"Categorised '{prompt.prompt.question}' as {response.value}"
    log.info(msg)
    print(msg)

    return QAWithDoc(
        prompt=prompt.prompt,
        parent_doc=prompt.parent_doc.with_tags(tags),
        line_nr=prompt.line_nr,
        render_parent_doc=prompt.render_parent_doc,
    )


@dataclass(frozen=True)
class Categoriser:
    cache_dir: Path  # kept for interface compatibility, unused in async version

    def __call__(self, prompts: Sequence[QAWithDoc]) -> Sequence[QAWithDoc]:
        """Synchronously categorise prompts.

        Internally spins up an asyncio event loop to run the original
        concurrent categorisation logic while exposing a blocking API
        to callers.
        """
        if not prompts:
            return []

        self.cache_dir.mkdir(parents=True, exist_ok=True)
        print(f"Using cache dir: {self.cache_dir}")

        mem = Memory(str(self.cache_dir), verbose=0)
        cached_func = mem.cache(_process_prompts)

        return Arr(prompts).pmap(cached_func).to_list()
