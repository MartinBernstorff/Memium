import pytest

from personal_mnemonic_medium.note_factories.note import Note
from personal_mnemonic_medium.prompt_extractors.qa_extractor import QAPromptExtractor


@pytest.fixture(scope="function")
def qa_extractor():
    return QAPromptExtractor()


def test_qa_prompt_extractor():
    note_object = Note(
        title="Test note",
        content="""Test content. 
Q. What is the first test prompt?
A. This is the prompt!
        """,
        uuid="1234",
    )

    prompts = QAPromptExtractor().extract_prompts(note_object)

    assert len(prompts) == 1
    assert prompts[0].question == "What is the first test prompt?"
    assert prompts[0].answer == "This is the prompt!"
    assert len([p for p in prompts if p.source_note is None]) == 0


def test_has_qa_matches(qa_extractor):
    example_strings = [
        "QD. Testing something something",
        "QA. Testing something else, even with QA in it!",
        "\Q. Testing newlines as well!",
    ]
    matches = [string for string in example_strings if qa_extractor.has_qa(string)]

    assert len(matches) == 3


def test_has_qa_does_not_match(qa_extractor):
    example_strings = ["\nQ.E.D.", "> A question like this, or", "::Q. A comment!::"]

    matches = 0

    for string in example_strings:
        if qa_extractor.has_qa(string):
            matches += 1

    assert matches == 0
