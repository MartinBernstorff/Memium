import asyncio
import enum
import functools
import logging
import os
import re
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

import anyio
import instructor
from anyio import Semaphore
from pydantic import BaseModel, model_validator

from memium.source.prompt import QAWithDoc
from memium.utils.disk_cache import DiskCache

log = logging.getLogger(__name__)

DECK_TAG_PREFIX = "anki/deck/"


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


class CachedCategory(BaseModel):
    value: CategoryValue

    @model_validator(mode="before")
    @classmethod
    def _read_entry_holding_a_whole_prompt(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        entry = cast("dict[str, Any]", data)
        parent_doc = cast("dict[str, Any]", entry.get("parent_doc", {}))
        deck_tags = re.findall(rf"#{DECK_TAG_PREFIX}([\w/]+)", str(parent_doc.get("content", "")))

        if not deck_tags:
            return entry

        return {"value": CategoryValue(deck_tags[-1])}


@functools.cache
def _client() -> instructor.AsyncInstructor:
    return instructor.from_provider(
        "openai/gpt-5-nano", api_key=os.getenv("OPENAI_API_KEY"), async_client=True
    )


async def _categorise(prompt: QAWithDoc) -> CachedCategory:
    response: Category = await _client().chat.completions.create(
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

    prompt_repr = f"{prompt.parent_doc.title}: Q. {prompt.prompt.question}"
    msg = f"Categorised '{prompt_repr}' as {response.value.value}"
    log.info(msg)
    print(msg)

    return CachedCategory(value=response.value)


def _with_category(prompt: QAWithDoc, category: CachedCategory) -> QAWithDoc:
    return QAWithDoc(
        prompt=prompt.prompt,
        parent_doc=prompt.parent_doc.with_tags([DECK_TAG_PREFIX + category.value.value]),
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
        cached = DiskCache[QAWithDoc, CachedCategory](
            cache_file=str(self.cache_dir / "categoriser_cache.sqlite"),
            compute_fn=_categorise,
            cache_key_fn=_categoriser_cache_key,
            result_type=CachedCategory,
        )

        semaphore = Semaphore(self.max_concurrency)
        results: list[QAWithDoc | None] = [None] * len(prompts)

        async def process_with_semaphore(index: int, prompt: QAWithDoc) -> None:
            async with semaphore:
                results[index] = _with_category(prompt, await cached(prompt))
                if len(prompts) % 10 == 0:
                    log.info(f"Categorised {index + 1}/{len(prompts)}")

        async with anyio.create_task_group() as tg:
            for i, prompt in enumerate(prompts):
                tg.start_soon(process_with_semaphore, i, prompt)

        return [r for r in results if r is not None]
