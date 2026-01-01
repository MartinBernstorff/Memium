import logging
from collections.abc import Awaitable, Callable
from dataclasses import dataclass

from pydantic import BaseModel
from sqlalchemy import String, Text, select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

log = logging.getLogger(__name__)


class Base(DeclarativeBase):
    pass


class CacheEntry(Base):
    __tablename__ = "cache"

    key: Mapped[str] = mapped_column(String, primary_key=True)
    value: Mapped[str] = mapped_column(Text, nullable=False)


@dataclass
class DiskCache[T: BaseModel, S: BaseModel]:
    """
    An async disk-based cache using SQLAlchemy/SQLite for Pydantic models.

    Args:
        cache_file: Path to the SQLite database file
        compute_fn: Async function to compute the result from input
        cache_key_fn: Function to generate a cache key from input
        result_type: The Pydantic model class for the result (needed for deserialization)
    """

    cache_file: str
    compute_fn: Callable[[T], Awaitable[S]]
    cache_key_fn: Callable[[T], str]
    result_type: type[S]

    def __post_init__(self) -> None:
        # Use aiosqlite driver for async SQLite support
        self.engine = create_async_engine(f"sqlite+aiosqlite:///{self.cache_file}")
        self._initialized = False

    async def _ensure_tables(self) -> None:
        """Create tables if they don't exist (lazy initialization)."""
        if not self._initialized:
            async with self.engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            self._initialized = True

    async def _get_cached(self, key: str) -> S | None:
        """Retrieve a value from the cache."""
        await self._ensure_tables()

        async with AsyncSession(self.engine) as session:
            stmt = select(CacheEntry).where(CacheEntry.key == key)
            entry = await session.scalar(stmt)

            if entry is not None:
                return self.result_type.model_validate_json(entry.value)
            return None

    async def _set_cached(self, key: str, value: S) -> None:
        """Store a value in the cache."""
        await self._ensure_tables()

        async with AsyncSession(self.engine) as session:
            entry = await session.get(CacheEntry, key)

            if entry is not None:
                entry.value = value.model_dump_json()
            else:
                entry = CacheEntry(key=key, value=value.model_dump_json())
                session.add(entry)

            await session.commit()

    async def __call__(self, input_value: T) -> S:
        """
        Get the result for the input, using cache if available.

        Args:
            input_value: The input Pydantic model

        Returns:
            The computed or cached result
        """
        key = self.cache_key_fn(input_value)

        # Check for cache hit
        cached_result = await self._get_cached(key)
        if cached_result is not None:
            log.info(f"Cache hit for key: {key}")
            return cached_result

        # Cache miss: compute, store, and return
        result = await self.compute_fn(input_value)
        await self._set_cached(key, result)
        return result

    async def close(self) -> None:
        """Close the database engine and release resources."""
        await self.engine.dispose()
