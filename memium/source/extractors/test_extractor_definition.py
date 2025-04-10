from pathlib import Path

from inline_snapshot import snapshot

from memium.source.document import DummyDocument
from memium.source.extractors.extractor_definition import ReversedDefinitionExtractor
from memium.source.extractors.extractor_qa import QAPromptExtractor


def test_extract_reversed_definition():
    doc = DummyDocument(
        content="""
Q. Definition?
A. A large African cat with a mane.""",
        source_path=Path("Lion.md"),
    )
    result = ReversedDefinitionExtractor(QAPromptExtractor("Q.", "A.")).extract_prompts(doc)

    assert len(result) == 1
    assert result[0].question == snapshot("Term for 'A large African cat with a mane'?")
    assert result[0].answer == snapshot("Lion")


def test_empty_definition_extractor():
    doc = DummyDocument(
        content="""
Q. No def?
A. Blah"""
    )
    result = ReversedDefinitionExtractor(QAPromptExtractor("Q.", "A.")).extract_prompts(doc)
    assert len(result) == 0
