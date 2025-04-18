import logging
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Protocol

from iterpy import Iter

from memium.source.prompt import QAWithDoc

from .document import Document
from .document_source import BaseDocumentSource
from .extractors.extractor import BasePromptExtractor

log = logging.getLogger(__name__)


class BasePromptSource(Protocol):
    def get_prompts(self) -> Sequence[QAWithDoc]: ...


@dataclass(frozen=True)
class DocumentPromptSource(BasePromptSource):
    document_ingester: BaseDocumentSource
    prompt_extractors: Sequence[BasePromptExtractor]

    def _get_prompts_from_document(self, document: Document) -> Sequence[QAWithDoc]:
        prompts: list[QAWithDoc] = []

        for extractor in self.prompt_extractors:
            try:
                extractor_prompts = list(extractor.extract_prompts(document))
                prompts += extractor_prompts
            except Exception as e:
                log.error(
                    f"Failed to extract prompts with {extractor} from {document.source_path.name} using {extractor}. Reason: {e}"
                )

        return prompts

    def _deduplicate_group(self, group: tuple[str, Sequence[QAWithDoc]]) -> QAWithDoc:
        prompts_in_group = group[1]

        if len(prompts_in_group) != 1:
            identifiers = [p.edit_url if p.edit_url else p for p in prompts_in_group]
            log.warning(f"""Duplicate prompts: {identifiers}""")

        return prompts_in_group[0]

    def _deduplicate_prompts(self, prompts: Sequence[QAWithDoc]) -> Sequence[QAWithDoc]:
        """Deduplicate prompts based on scheduling id. If the scheduling id is the same, the prompt is considered a duplicate."""
        scheduling_id_groups = Iter(prompts).groupby(lambda prompt: str(prompt.scheduling_id))

        unique_prompts = scheduling_id_groups.map(self._deduplicate_group).to_list()

        n_duplicates = len(prompts) - len(unique_prompts)
        if n_duplicates != 0:
            log.warning(f"Found a total of {n_duplicates} duplicate prompts")

        return unique_prompts

    def get_prompts(self) -> Sequence[QAWithDoc]:
        prompts = (
            Iter(self.document_ingester.get_documents())
            .map(self._get_prompts_from_document)
            .flatten()
            .to_list()
        )

        return self._deduplicate_prompts(prompts)
