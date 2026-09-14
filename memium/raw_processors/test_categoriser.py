import asyncio
from pathlib import Path

from pydantic import BaseModel

from memium.raw_processors.categoriser import (
    CachedCategory,
    Categoriser,
    CategoryValue,
    _categoriser_cache_key,  # type: ignore[PrivateUsage]
)
from memium.source.document import Document
from memium.source.prompt import QAWithDoc
from memium.utils.disk_cache import DiskCache


def _prompt(source_path: Path) -> QAWithDoc:
    return QAWithDoc(
        prompt=QAWithDoc.dummy().prompt,
        parent_doc=Document(content="Some content", source_path=source_path, vault_name="Vault"),
        line_nr=4,
    )


def _seed(
    cache_dir: Path, result_type: type[BaseModel], prompt: QAWithDoc, value: BaseModel
) -> None:
    async def explode(prompt: QAWithDoc) -> BaseModel:
        raise AssertionError(f"Should have been a cache hit: {prompt}")

    async def write() -> None:
        cache = DiskCache[QAWithDoc, BaseModel](
            cache_file=str(cache_dir / "categoriser_cache.sqlite"),
            compute_fn=explode,
            cache_key_fn=_categoriser_cache_key,
            result_type=result_type,
        )
        await cache._set_cached(_categoriser_cache_key(prompt), value)  # type: ignore[PrivateUsage]
        await cache.close()

    asyncio.run(write())


def test_moved_prompt_gets_new_destination(tmp_path: Path):
    _seed(
        tmp_path,
        CachedCategory,
        _prompt(Path("original.md")),
        CachedCategory(value=CategoryValue.PYTHON),
    )

    categorised = Categoriser(cache_dir=tmp_path)([_prompt(Path("moved.md"))])

    assert categorised[0].parent_doc.source_path == Path("moved.md")
    assert categorised[0].parent_doc.tags == ["anki/deck/Python"]


def test_entries_from_before_only_the_category_was_cached_are_still_read(tmp_path: Path):
    original = _prompt(Path("original.md"))
    _seed(
        tmp_path,
        QAWithDoc,
        original,
        QAWithDoc(
            prompt=original.prompt,
            parent_doc=original.parent_doc.with_tags(["anki/deck/Python"]),
            line_nr=original.line_nr,
        ),
    )

    categorised = Categoriser(cache_dir=tmp_path)([_prompt(Path("moved.md"))])

    assert categorised[0].parent_doc.source_path == Path("moved.md")
    assert categorised[0].parent_doc.tags == ["anki/deck/Python"]
