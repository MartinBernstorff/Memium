import logging
from collections.abc import Sequence
from typing import Protocol

from iter import Iter

from .document import Document
from .document_source import BaseDocumentSource
from .extractors.extractor import BasePromptExtractor
from .prompts.prompt import BasePrompt

log = logging.getLogger(__name__)


class BasePromptSource(Protocol):
    def get_prompts(self) -> Sequence[BasePrompt]:
        ...


class DocumentPromptSource(BasePromptSource):
    def __init__(
        self,
        document_ingester: BaseDocumentSource,
        prompt_extractors: Sequence[BasePromptExtractor],
    ):
        self._document_ingester = document_ingester
        self._prompt_extractors = prompt_extractors

    def _get_prompts_from_document(
        self, document: Document
    ) -> Sequence[BasePrompt]:
        prompts: list[BasePrompt] = []
        for extractor in self._prompt_extractors:
            extractor_prompts = list(extractor.extract_prompts(document))
            prompts += extractor_prompts

        return prompts

    def _deduplicate_group(
        self, group: tuple[str, Sequence[BasePrompt]]
    ) -> BasePrompt:
        prompts = group[1]

        if len(prompts) != 1:
            log.warn(f"Found duplicate prompts: {prompts}")

        return prompts[0]

    def _deduplicate_prompts(
        self, prompts: Sequence[BasePrompt]
    ) -> Sequence[BasePrompt]:
        """Deduplicate prompts based on scheduling UID. If the scheduling UID is the same, the prompt is considered a duplicate."""
        scheduling_uuid_groups = Iter(prompts).groupby(
            lambda prompt: str(prompt.scheduling_uid)
        )

        unique_prompts = scheduling_uuid_groups.map(
            self._deduplicate_group
        ).to_list()

        return unique_prompts

    def get_prompts(self) -> Sequence[BasePrompt]:
        prompts = (
            Iter(self._document_ingester.get_documents())
            .map(self._get_prompts_from_document)
            .flatten()
            .to_list()
        )

        return self._deduplicate_prompts(prompts)
