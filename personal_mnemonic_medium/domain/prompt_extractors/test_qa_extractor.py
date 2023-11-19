from pathlib import Path

import pytest

from personal_mnemonic_medium.data_access.document_ingesters.document import (
    Document,
)
from personal_mnemonic_medium.domain.prompt_extractors.qa_extractor import (
    QAPromptExtractor,
)


@pytest.fixture()
def qa_extractor() -> QAPromptExtractor:
    return QAPromptExtractor(question_prefix="Q.", answer_prefix="A.")


def test_qa_prompt_extractor():
    note_object = Document(
        content="""Test content.
Q. What is the first test prompt?
A. This is the prompt!
        """,
        uuid="1234",
        source_path=Path(__file__),
    )

    prompts = QAPromptExtractor(
        question_prefix="Q.", answer_prefix="A."
    ).extract_prompts(note_object)

    assert len(prompts) == 1
    prompt = prompts[0]
    assert prompt.question == "What is the first test prompt?"
    assert prompt.answer == "This is the prompt!"
    assert isinstance(prompt.source_note, Document)


def test_has_qa_matches(qa_extractor: QAPromptExtractor):
    example_strings = [
        "QD. Testing something something",
        "QA. Testing something else, even with QA in it!",
        "\\Q. Testing newlines as well!",
    ]
    matches = [
        string
        for string in example_strings
        if qa_extractor._has_qa(string)  # type: ignore
    ]

    assert len(matches) == 3


def test_has_qa_does_not_match(qa_extractor: QAPromptExtractor):
    example_strings = [
        "\nQ.E.D.",
        "> A question like this, or",
        "::Q. A comment!::",
    ]

    matches = 0

    for string in example_strings:
        if qa_extractor._has_qa(string):  # type: ignore
            matches += 1

    assert matches == 0


def test_line_indexing(qa_extractor: QAPromptExtractor):
    note_object = Document(
        uuid="1234",
        source_path=Path(__file__),
        content="""Test content.

Q. What is the first test prompt?
A. This is the prompt!

Block line 1

Q. What is the second test prompt?
A. This is the second prompt!
""",
    )

    prompts = qa_extractor.extract_prompts(note_object)

    assert prompts[0].line_nr == 3
    assert prompts[1].line_nr == 8
