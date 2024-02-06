import logging
from collections.abc import Sequence
from typing import Protocol

from iterpy import Iter

from .document import Document
from .document_source import BaseDocumentSource
from .extractors.extractor import BasePromptExtractor
from .prompts.prompt import BasePrompt
from .prompts.prompt_from_doc import PromptFromDocMixin

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
    ) -> Sequence[PromptFromDocMixin]:
        prompts: list[PromptFromDocMixin] = []

        for extractor in self._prompt_extractors:
            try:
                extractor_prompts = list(extractor.extract_prompts(document))
                prompts += extractor_prompts  # type: ignore
            except Exception as e:
                log.error(
                    f"Failed to extract prompts with {extractor} from {document.source_path.name} using {extractor}. Reason: {e}"
                )

        return prompts

    def _deduplicate_group(
        self, group: tuple[str, Sequence[PromptFromDocMixin]]
    ) -> BasePrompt:
        prompts_in_group = group[1]

        if len(prompts_in_group) != 1:
            duplicate_prompt_locations = (
                Iter(prompts_in_group)
                .map(
                    lambda prompt: f"{prompt.parent_doc.source_path.name}:{prompt.line_nr}"
                )
                .to_list()
            )
            log.warn(f"Found duplicate prompts in {duplicate_prompt_locations}")

        return prompts_in_group[0]

    def _deduplicate_prompts(
        self, prompts: Sequence[PromptFromDocMixin]
    ) -> Sequence[BasePrompt]:
        """Deduplicate prompts based on scheduling UID. If the scheduling UID is the same, the prompt is considered a duplicate."""
        scheduling_uuid_groups = Iter(prompts).groupby(
            lambda prompt: str(prompt.scheduling_uid)
        )

        unique_prompts = scheduling_uuid_groups.map(
            self._deduplicate_group
        ).to_list()

        n_duplicates = len(prompts) - len(unique_prompts)
        if n_duplicates != 0:
            log.warn(f"Found a total of {n_duplicates} duplicate prompts")

        return unique_prompts

    def get_prompts(self) -> Sequence[BasePrompt]:
        prompts = (
            Iter(self._document_ingester.get_documents())
            .map(self._get_prompts_from_document)
            .flatten()
            .to_list()
        )

        return self._deduplicate_prompts(prompts)
