from pathlib import Path

from inline_snapshot import snapshot

from memium.source.document import DummyDocument
from memium.source.extractors.extractor_qa import QAPromptExtractor
from memium.source.extractors.extractor_title_as_answer import TitleAsAnswerExtractor


def test_extract_reversed_definition():
    doc = DummyDocument(
        content="""
Q. Definition?
A. A large African cat with a mane.""",
        source_path=Path("Lion.md"),
    )
    result = TitleAsAnswerExtractor(
        QAPromptExtractor("Q.", "A."), matcher="Definition?", reversed_question="Term for '%s'?"
    ).extract_prompts(doc)

    assert len(result) == 1
    assert result[0].prompt.question == snapshot("Term for 'A large African cat with a mane'?")
    assert result[0].prompt.answer == snapshot("Lion")


def test_empty_definition_extractor():
    doc = DummyDocument(
        content="""
Q. No def?
A. Blah"""
    )
    result = TitleAsAnswerExtractor(
        QAPromptExtractor("Q.", "A."), matcher="Definition?", reversed_question="Term for '%s'?"
    ).extract_prompts(doc)
    assert len(result) == 0


def test_application_extractor():
    doc = DummyDocument(
        content="""Q. Use when?
A. Preventing coagulation.""",
        source_path=Path("Heparin.md"),
    )
    result = TitleAsAnswerExtractor(
        QAPromptExtractor("Q.", "A."),
        matcher="Use when?",
        reversed_question="What should we use for '%s'?",
    ).extract_prompts(doc)

    assert len(result) == 1
    assert result[0].prompt.question == snapshot("What should we use for 'Preventing coagulation'?")
    assert result[0].prompt.answer == snapshot("Heparin")


def test_avoid_extractor():
    doc = DummyDocument(
        content="""Q. Avoid when?
A. High risk of venous bleeding, e.g. intestinal.""",
        source_path=Path("Heparin.md"),
    )
    result = TitleAsAnswerExtractor(
        QAPromptExtractor("Q.", "A."),
        matcher="Avoid when?",
        reversed_question="What should we avoid when '%s'?",
    ).extract_prompts(doc)

    assert len(result) == 1
    assert result[0].prompt.question == snapshot(
        "What should we avoid when 'High risk of venous bleeding, e.g. intestinal'?"
    )
    assert result[0].prompt.answer == snapshot("Heparin")
