from pathlib import Path

from ...promptsource.document import Document
from ...promptsource.ingester_fake import FakeDocumentIngester
from ...promptsource.prompt_source_document import (
    DocumentPromptSource,
)
from ...promptsource.prompt_extractor_qa import QAPromptExtractor


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
