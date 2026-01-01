import enum
import logging
import os
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import cast

import instructor
from iterpy import Arr
from pydantic import BaseModel

from memium.source.prompt import QAWithDoc
from memium.utils.disk_cache import DiskCache

log = logging.getLogger(__name__)


class CategoryValue(enum.Enum):
    FHIR = "FHIR"
    JAVA = "Java"
    PYTHON = "Python"
    SPRING_BOOT = "SpringBoot"
    ML = "MachineLearning"
    SWE = "SoftwareEngineering"
    TRIFORK = "TRIFORK"
    OTHER = "Other"


class Category(BaseModel):
    value: CategoryValue


api_key = os.getenv("OPENAI_API_KEY")
client = instructor.from_provider("openai/gpt-5-nano", api_key=api_key)


def _process_prompts(prompt: QAWithDoc) -> QAWithDoc:
    # 'version' kept for future behavioural changes; underscore assignment silences unused warning
    response: Category = client.chat.completions.create(
        response_model=Category,
        messages=[
            {
                "role": "user",
                "content": (
                    f"This is a flashcard from a note called {prompt.parent_doc.title}. "
                    f"Q. {prompt.prompt.question} A. {prompt.prompt.answer}. "
                    f"What is this flashcard about? Choose one of the following categories."
                ),
            }
        ],
    )  # type: ignore

    tags = ["anki/deck/" + response.value.value]
    prompt_repr = f"{prompt.parent_doc.title}: Q. {prompt.prompt.question}"
    msg = f"Categorised '{prompt_repr}' as {response.value.value}"
    log.info(msg)
    print(msg)

    return QAWithDoc(
        prompt=prompt.prompt,
        parent_doc=prompt.parent_doc.with_tags(tags),
        line_nr=prompt.line_nr,
        render_parent_doc=prompt.render_parent_doc,
    )


def _get_cache_key(prompt: QAWithDoc) -> str:
    return prompt.prompt.scheduling_uid_str


@dataclass(frozen=True)
class Categoriser:
    cache_dir: Path

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

        cached = DiskCache[
            QAWithDoc, QAWithDoc
        ](
            cache_file=str(self.cache_dir / "categoriser_cache.sqlite"),
            compute_fn=_process_prompts,
            cache_key_fn=_get_cache_key,  # Do not use a lambda here; needs to be picklable for multiprocessing in pmap
            result_type=QAWithDoc,
        )

        result = cast(Sequence[QAWithDoc], Arr(prompts).map(cached).to_list())
        return result
