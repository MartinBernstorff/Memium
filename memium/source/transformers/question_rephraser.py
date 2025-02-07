import datetime
import logging
import time
from typing import TypeGuard, cast

from anthropic import Anthropic
from iterpy import Arr
from joblib import Memory  # type: ignore

from memium.source.prompts.prompt import BasePrompt
from memium.source.prompts.prompt_qa import QAFromDoc, RephrasedQAFromDoc

# Set up the cache directory
# Note that this is modified at invocation time in the core call
memory = Memory(verbose=0)

log = logging.getLogger(__name__)


def get_ttl_hash(seconds: int) -> str:
    """Return the same value withing `seconds` time period"""
    value = int(time.time()) // seconds
    return str(value)


@memory.cache  # type: ignore
def _rephrase_question(
    question: str,
    answer: str,
    ttl: str,  # noqa: ARG001
) -> str:
    client = Anthropic()
    prompt = f"""<prompt>Rephrase the question. Make it brief, without changing the meaning. Any term surrounded by _, like _this_, must stay surrounded by _ and not be rephrased. When possible, put these terms in the start of the sentence.</prompt>
<question>{question}</question>
<answer>{answer}</answer>
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

    rephrased = Arr(to_rephrase).map(
        lambda it: RephrasedQAFromDoc(
            parent_doc=it.parent_doc,
            line_nr=it.line_nr,
            question=it.question,
            rephrased_question=_rephrase_question(
                it.question, it.answer, get_ttl_hash(60 * 60 * 24 * cache_days)
            ),
            answer=it.answer,
        )
    )

    to_keep = prompts.filter(lambda x: not should_rephrase(x)).to_list()

    return Arr(to_keep + rephrased.to_list())
