from pathlib import Path

from memium.raw_processors.categoriser import Categoriser
from memium.source.prompt import QAWithDoc


def test_swe():
    doc = QAWithDoc.dummy(question="Definition?", answer="A location used for testing.")
    result = Categoriser(
        question_matcher="Definition?", reversed_question="Term for '%s'?"
    ).__call__([doc])

    assert len(result) == 1
    assert result[0].parent_doc.tags == ["anki/deck/Other"]


def test_medicine():
    doc = QAWithDoc.dummy(question="Hvad er symptomerne på migræne?", answer="Hovedpine")
    result = Categoriser(cache_dir=Path("/tmp")).__call__([doc])

    assert len(result) == 1
    assert result[0].parent_doc.tags == ["anki/deck/Medicine"]
