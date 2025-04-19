from inline_snapshot import snapshot

from memium.raw_processors.title_as_answer import TitleAsAnswerProcessor
from memium.source.prompt import QAWithDoc


def test_extract_reversed_definition():
    doc = QAWithDoc.dummy(question="Definition?", answer="A location used for testing.")
    result = TitleAsAnswerProcessor(
        question_matcher="Definition?", reversed_question="Term for '%s'?"
    ).__call__([doc])

    assert len(result) == 2
    assert result[1].prompt.question == snapshot("Term for 'A location used for testing'?")
    assert result[1].prompt.answer == snapshot("DummyPath")


def test_empty_definition_extractor():
    doc = QAWithDoc.dummy(question="No def?", answer="Blah")
    result = TitleAsAnswerProcessor(
        question_matcher="Definition?", reversed_question="Term for '%s'?"
    ).__call__([doc])
    assert len(result) == 1


def test_application_extractor():
    doc = QAWithDoc.dummy(question="Use when?", answer="Preventing coagulation.")
    result = TitleAsAnswerProcessor(
        question_matcher="Use when?", reversed_question="What should we use for '%s'?"
    ).__call__([doc])

    assert len(result) == 2
    assert result[1].prompt.question == snapshot("What should we use for 'Preventing coagulation'?")
    assert result[1].prompt.answer == snapshot("DummyPath")
