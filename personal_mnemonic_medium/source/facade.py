from collections.abc import Sequence
from typing import Protocol

from .document import Document
from .document_ingester import BaseDocumentIngester
from .extractors.extractor import BasePromptExtractor
from .prompts.prompt import BasePrompt


class BasePromptSource(Protocol):
    def get_prompts(self) -> Sequence[BasePrompt]:
        ...


class DocumentPromptSource(BasePromptSource):
    def __init__(
        self,
        document_ingester: BaseDocumentIngester,
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

    def get_prompts(self) -> Sequence[BasePrompt]:
        documents = self._document_ingester.get_documents()

        prompts = [self._get_prompts_from_document(doc) for doc in documents]

        return [item for sublist in prompts for item in sublist]
