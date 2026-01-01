from collections.abc import Callable
from dataclasses import dataclass

from pydantic import BaseModel
from sqlalchemy import String, Text, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class CacheEntry(Base):
    __tablename__ = "cache"

    key: Mapped[str] = mapped_column(String, primary_key=True)
    value: Mapped[str] = mapped_column(Text, nullable=False)


@dataclass
class DiskCache[T: BaseModel, S: BaseModel]:
    """
    A disk-based cache using SQLAlchemy/SQLite for Pydantic models.

    Args:
        cache_file: Path to the SQLite database file
        compute_fn: Function to compute the result from input
        cache_key_fn: Function to generate a cache key from input
        result_type: The Pydantic model class for the result (needed for deserialization)
    """

    cache_file: str
    compute_fn: Callable[[T], S]
    cache_key_fn: Callable[[T], str]
    result_type: type[S]

    def __post_init__(self) -> None:
        self.engine = create_engine(f"sqlite:///{self.cache_file}")
        Base.metadata.create_all(self.engine)

    def _get_cached(self, key: str) -> S | None:
        with Session(self.engine) as session:
            stmt = select(CacheEntry).where(CacheEntry.key == key)
            entry = session.scalar(stmt)

            if entry is not None:
                return self.result_type.model_validate_json(entry.value)
            return None

    def _set_cached(self, key: str, value: S) -> None:
        """Store a value in the cache."""
        with Session(self.engine) as session:
            entry = session.get(CacheEntry, key)

            if entry is not None:
                entry.value = value.model_dump_json()
            else:
                entry = CacheEntry(key=key, value=value.model_dump_json())
                session.add(entry)

            session.commit()

    def __call__(self, input_value: T) -> S:
        """
        Get the result for the input, using cache if available.

        Args:
            input_value: The input Pydantic model

        Returns:
            The computed or cached result
        """
        key = self.cache_key_fn(input_value)

        # Check for cache hit
        cached_result = self._get_cached(key)
        if cached_result is not None:
            return cached_result

        # Cache miss: compute, store, and return
        result = self.compute_fn(input_value)
        self._set_cached(key, result)
        return result
