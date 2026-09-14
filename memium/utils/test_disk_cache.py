import asyncio
from pathlib import Path

import pydantic
from sqlalchemy import text

from memium.utils.disk_cache import DiskCache


class Input(pydantic.BaseModel):
    key: str


class Result(pydantic.BaseModel):
    value: int


def test_unreadable_entry_is_a_miss(tmp_path: Path):
    """An entry written by an older version of the cached function should be recomputed,
    rather than failing the run."""
    computations = 0

    async def compute(input_value: Input) -> Result:
        nonlocal computations
        computations += 1
        return Result(value=len(input_value.key))

    async def run() -> list[Result]:
        cache = DiskCache[Input, Result](
            cache_file=str(tmp_path / "cache.sqlite"),
            compute_fn=compute,
            cache_key_fn=lambda it: it.key,
            result_type=Result,
        )

        # An entry the result type cannot read
        await cache._set_cached("ab", Result(value=0))  # type: ignore[PrivateUsage]
        async with cache.engine.begin() as conn:
            await conn.execute(text("UPDATE cache SET value = '{\"old_shape\": true}'"))

        results = [await cache(Input(key="ab")), await cache(Input(key="ab"))]
        await cache.close()
        return results

    results = asyncio.run(run())

    assert results == [Result(value=2), Result(value=2)]
    # Recomputed once, then read back from the cache it replaced
    assert computations == 1
