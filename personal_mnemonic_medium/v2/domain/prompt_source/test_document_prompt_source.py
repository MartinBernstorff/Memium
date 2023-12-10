from pathlib import Path

from .document_ingesters.document import Document
from .document_ingesters.fake_document_ingester import (
    FakeDocumentIngester,
)
from .document_prompt_source import DocumentPromptSource
from .prompt_extractors.qa_prompt_extractor import QAPromptExtractor


def test_document_prompt_source():
    source = DocumentPromptSource(
        document_ingester=FakeDocumentIngester(
            [
                Document(
                    """Q. What is a test even?
A. Nothing""",
                    Path("test.md"),
                )
            ]
        ),
        prompt_extractors=[
            QAPromptExtractor(
                question_prefix="Q.", answer_prefix="A."
            )
        ],
    )
    prompts = source.get_prompts()
    assert len(prompts) == 1
