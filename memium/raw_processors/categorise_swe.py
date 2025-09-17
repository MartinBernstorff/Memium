import asyncio
import logging
import os
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

import instructor
from instructor.cache import DiskCache
from pydantic import BaseModel

from memium.source.prompt import QAWithDoc

log = logging.getLogger(__name__)


class Category(BaseModel):
    value: Literal["Software Engineering", "Other"]


api_key = os.getenv("OPENAI_API_KEY")


async def _process_prompts(
    iterated_prompt: tuple[int, QAWithDoc], version: int, client: instructor.AsyncInstructor
) -> QAWithDoc:
    # 'version' kept for future behavioural changes; underscore assignment silences unused warning
    _ = version
    idx, prompt = iterated_prompt

    response = await client.chat.completions.create(
        response_model=Category,
        messages=[
            {
                "role": "user",
                "content": (
                    f"This is a flashcard from a note called {prompt.parent_doc.title}. "
                    f"{prompt.prompt.question} | {prompt.prompt.answer}. "
                    "Is this flashcard about software engineering or not? "
                    "Answer with 'Software Engineering' or 'Other'."
                ),
            }
        ],
    )

    print(f"{idx}, categorised '{prompt.prompt.question}' as '{response.value}'")

    tags = ["anki/deck/SWE" if response.value == "Software Engineering" else "anki/deck/Other"]

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

        client = instructor.from_provider(
            "openai/gpt-4.1-nano", api_key=api_key, cache=DiskCache(str(self.cache_dir))
        )

        tasks = [_process_prompts((i, p), version=1, client=client) for i, p in enumerate(prompts)]

        # Run the async workflow in a fresh event loop.
        async def run_tasks():
            return await asyncio.gather(*tasks)

        return asyncio.run(run_tasks())
