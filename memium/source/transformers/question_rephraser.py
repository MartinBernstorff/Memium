import datetime
import logging
import time
from collections.abc import Callable
from typing import TypeGuard, cast

from anthropic import Anthropic
from iterpy import Arr
from joblib import Memory  # type: ignore

from memium.source.prompts.prompt import BasePrompt
from memium.source.prompts.prompt_qa import QAFromDoc, RephrasedQAFromDoc

# Set up the cache directory
# Note that this is modified at invocation time in the core call
memory = Memory(verbose=1)

log = logging.getLogger(__name__)


def get_ttl_hash(seconds: int) -> str:
    """Return the same value withing `seconds` time period"""
    value = int(time.time()) // seconds
    return str(value)


@memory.cache  # type: ignore
def _rephrase_question(
    question: str,
    answer: str,  # noqa: ARG001
    note_title: str,
    ttl: str,  # noqa: ARG001
    version: str = "3",  # Note, changing this default value will invalidate all caches. Beware! # noqa: ARG001
) -> str:
    client = Anthropic()
    prompt = f"""<prompt>This is a question from a note. Rephrase the question for learning, keeping it brief, while retaining the meaning. Any term surrounded by _, like _this_, must remain surrounded by _ and not be rephrased. If the note title appears in the question, you can remove it.</prompt>
<note_title>{note_title}</note_title>
<question>{question}</question>
<prompt>Provide only the rephrased question with no additional text or explanation.</prompt>"""

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=300,
        temperature=0.7,
        messages=[{"role": "user", "content": prompt}],
    )

    rephrasing: str = cast(str, response.content[0].text.strip())  # type: ignore
    log.info({"event": "rephrased_question", "question": question, "rephrasing": rephrasing})
    return rephrasing


def rephrase(
    prompts: Arr[BasePrompt], max_age: datetime.timedelta, cache_days: int
) -> Arr[BasePrompt]:
    def should_rephrase(prompt: BasePrompt) -> TypeGuard[QAFromDoc]:
        return (
            isinstance(prompt, QAFromDoc)
            and prompt.parent_doc.last_modified > datetime.datetime.now() - max_age
        )

    # List comp. to get TypeGuard functionality
    to_rephrase = [p for p in prompts if should_rephrase(p)]

    log.info(f"Found {len(to_rephrase)} prompts to rephrase")

    # Need this to be an inner function so we can swap out the memory path before
    # this function is defined.
    # Joblib is terribly typed, so just have to trust me here.
    def _cached_rephraser(x: QAFromDoc) -> str:
        location = cast(str, memory.location)  # type: ignore
        log.info(f"Looking into cache at {location}")

        cached_func: Callable[[str, str, str], str] = memory.cache(  # type: ignore
            lambda q, a, n: _rephrase_question(  # type: ignore
                q,  # type: ignore
                a,  # type: ignore
                n,  # type: ignore
                get_ttl_hash(60 * 60 * 24 * cache_days),  # type: ignore
                version="3",  # type: ignore
            )
        )
        return cached_func(x.question, x.answer, x.parent_doc.source_path.stem)

    rephrased: list[RephrasedQAFromDoc] = []
    total_to_rephrase = len(to_rephrase)
    for i, it in enumerate(to_rephrase):
        rephrased.append(
            RephrasedQAFromDoc(
                parent_doc=it.parent_doc,
                line_nr=it.line_nr,
                question=it.question,
                rephrased_question=_cached_rephraser(it),
                answer=it.answer,
            )
        )
        log.info(
            {
                "event": "rephraseProgress",
                "n_done": i + 1,
                "total": total_to_rephrase,
                "progress": round((i + 1) / total_to_rephrase, 2),
            }
        )

    to_keep = prompts.filter(lambda x: not should_rephrase(x)).to_list()

    return Arr(to_keep + rephrased)
