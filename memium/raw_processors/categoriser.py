import asyncio
import enum
import logging
import os
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path

import anyio
import instructor
from anyio import Semaphore
from pydantic import BaseModel

from memium.source.prompt import QAWithDoc
from memium.utils.disk_cache import DiskCache

log = logging.getLogger(__name__)


class CategoryValue(enum.Enum):
    FHIR = "FHIR"
    JAVA = "Java"
    PYTHON = "Python"
    DJANGO = "Django"
    MEDICINE = "Medicine"
    SPRING_BOOT = "SpringBoot"
    ML = "MachineLearning"
    SWE = "SoftwareEngineering"
    TRIFORK = "TRIFORK"
    OTHER = "Other"


class Category(BaseModel):
    value: CategoryValue


api_key = os.getenv("OPENAI_API_KEY")
client = instructor.from_provider("openai/gpt-5-nano", api_key=api_key, async_client=True)


async def _process_prompts(prompt: QAWithDoc) -> QAWithDoc:
    response: Category = await client.chat.completions.create(
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


def _categoriser_cache_key(prompt: QAWithDoc) -> str:
    return f"{prompt.prompt.scheduling_uid_str}_v2"


@dataclass(frozen=True)
class Categoriser:
    cache_dir: Path
    max_concurrency: int = 10

    def __call__(self, prompts: Sequence[QAWithDoc]) -> Sequence[QAWithDoc]:
        """Synchronously categorise prompts.

        Internally spins up an asyncio event loop to run the concurrent
        categorisation logic while exposing a blocking API to callers.
        """
        if not prompts:
            return []

        self.cache_dir.mkdir(parents=True, exist_ok=True)
        print(f"Using cache dir: {self.cache_dir}")

        return asyncio.run(self._categorise_async(prompts))

    async def _categorise_async(self, prompts: Sequence[QAWithDoc]) -> list[QAWithDoc]:
        """Asynchronously categorise all prompts with controlled concurrency."""
        cached = DiskCache[QAWithDoc, QAWithDoc](
            cache_file=str(self.cache_dir / "categoriser_cache.sqlite"),
            compute_fn=_process_prompts,
            cache_key_fn=_categoriser_cache_key,
            result_type=QAWithDoc,
        )

        semaphore = Semaphore(self.max_concurrency)
        results: list[QAWithDoc | None] = [None] * len(prompts)

        async def process_with_semaphore(index: int, prompt: QAWithDoc) -> None:
            async with semaphore:
                results[index] = await cached(prompt)
                if len(prompts) % 10 == 0:
                    log.info(f"Categorised {index + 1}/{len(prompts)}")

        async with anyio.create_task_group() as tg:
            for i, prompt in enumerate(prompts):
                tg.start_soon(process_with_semaphore, i, prompt)

        return [r for r in results if r is not None]
