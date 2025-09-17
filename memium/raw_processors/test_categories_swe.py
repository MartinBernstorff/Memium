from memium.raw_processors.categorise_swe import Categoriser
from memium.source.prompt import QAWithDoc


def test_extract_reversed_definition():
    doc = QAWithDoc.dummy(question="Definition?", answer="A location used for testing.")
    result = Categoriser(
        question_matcher="Definition?", reversed_question="Term for '%s'?"
    ).__call__([doc])

    assert len(result) == 1
    assert result[0].parent_doc.tags == ["anki/deck/Other"]
