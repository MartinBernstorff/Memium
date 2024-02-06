from pathlib import Path

from .document_source import MarkdownDocumentSource
from .extractors.extractor_qa import QAPromptExtractor
from .prompt_source import DocumentPromptSource


class TestPromptSource:
    def test_should_deduplicate_prompts(self, tmp_path: Path):
        with (tmp_path / "test.md").open("w") as f:
            f.write(
                """Q. Question
A. Answer

Q. Question
A. Answer"""
            )
        prompts = DocumentPromptSource(
            document_ingester=MarkdownDocumentSource(directory=tmp_path),
            prompt_extractors=[QAPromptExtractor(question_prefix="Q.", answer_prefix="A.")],
        ).get_prompts()
        assert len(prompts) == 1
