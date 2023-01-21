from personal_mnemonic_medium.note_factories.note import Note
from personal_mnemonic_medium.prompt_extractors.qa_prompt_extractor import (
    QAPromptExtractor,
)


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
