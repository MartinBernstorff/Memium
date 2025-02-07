import datetime
import time
from typing import TypeGuard

from anthropic import Anthropic
from iterpy import Arr
from joblib import Memory

from memium.source.prompts.prompt import BasePrompt
from memium.source.prompts.prompt_qa import QAFromDoc, RephrasedQAFromDoc

# Set up the cache directory
# feat: make this configurable so it's stored next to the prompts
memory = Memory("/tmp/joblib_cache", verbose=0)


def get_ttl_hash(seconds: int) -> str:
    """Return the same value withing `seconds` time period"""
    value = int(time.time()) // seconds
    return str(value)


@memory.cache  # type: ignore
def rephrase_question(
    question: str,
    answer: str,
    ttl: str,  # noqa: ARG001
) -> str:
    client = Anthropic()
    prompt = f"""Given this question and its answer, rephrase the question. Make it brief, without changing the meaning.

Question: {question}
Answer: {answer}

Provide only the rephrased question with no additional text or explanation."""

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=300,
        temperature=0.7,
        messages=[{"role": "user", "content": prompt}],
    )

    return response.content[0].text.strip()  # type: ignore


class QuestionRephraser:
    def rephrase(self, question: str, answer: str, cache_seconds: int) -> str:
        return rephrase_question(question, answer, get_ttl_hash(cache_seconds))


def rephrase(prompts: Arr[BasePrompt], max_age: datetime.timedelta) -> Arr[BasePrompt]:
    def should_rephrase(prompt: BasePrompt) -> TypeGuard[QAFromDoc]:
        return (
            isinstance(prompt, QAFromDoc)
            and prompt.parent_doc.last_modified > datetime.datetime.now() - max_age
        )

    # List comp. to get TypeGuard functionality
    to_rephrase = [p for p in prompts if should_rephrase(p)]

    rephrased = Arr(to_rephrase).map(
        lambda it: RephrasedQAFromDoc(
            parent_doc=it.parent_doc,
            line_nr=it.line_nr,
            question=it.question,
            rephrased_question=rephrase_question(
                it.question, it.answer, get_ttl_hash(60 * 60 * 24 * 365)
            ),
            answer=it.answer,
        )
    )

    to_keep = prompts.filter(lambda x: not should_rephrase(x)).to_list()

    # refactor: keep these as arr and chain them together
    # requires upgrading iterpy
    return Arr(to_keep + rephrased.to_list())
