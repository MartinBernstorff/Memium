from collections.abc import Sequence
from pathlib import Path

import pytest

from personal_mnemonic_medium.data_access.document_ingesters.document import (
    Document,
)
from personal_mnemonic_medium.data_access.document_ingesters.uuid_handling import (
    extract_bear_guid,
)
from personal_mnemonic_medium.data_access.exporters.anki.card_types.cloze import (
    AnkiCloze,
)
from personal_mnemonic_medium.data_access.exporters.anki.card_types.qa import (
    AnkiQA,
)
from personal_mnemonic_medium.domain.prompt_extractors.prompt import (
    Prompt,
)
from personal_mnemonic_medium.domain.prompt_extractors.qa_extractor import (
    QAPrompt,
)


class MockPrompt(Prompt):
    def __init__(
        self,
        content: str = "Ignore",  # noqa: ARG002
        note_uuid: str = "Ignore",  # noqa: ARG002
        source_note: Document = Document(  # noqa: B008
            content="", uuid="1234", source_path=Path(__file__)
        ),
        tags: list[str] | None = None,
        line_nr: int | None = None,
    ):
        if tags is None:
            tags = ["tag1"]

        self.source_note = source_note
        self.line_nr = line_nr

    @property
    def tags(self) -> Sequence[str]:
        return self.source_note.tags

    @property
    def note_uuid(self) -> str:
        return self.source_note.uuid


def test_custom_card_to_genanki_card():
    source_note = Document(
        content="Q. What is the capital of France?\nA. Paris",
        uuid="1234",
        source_path=Path(__file__),
    )
    AnkiQA(
        fields=["Q. What is the capital of France?", "A. Paris"],
        source_prompt=QAPrompt(
            question="What is the capital of France?",
            answer="Paris",
            source_note=source_note,
        ),
    ).to_genanki_note()


def test_get_subtags():
    source_note = Document(
        content="Testing subdeck extraction, #anki/deck/Medicine, #anki/tag/med/Endocrinology",
        uuid="1234",
        source_path=Path(__file__),
    )

    card = AnkiQA(
        fields=[""],
        source_prompt=QAPrompt(
            question="What is the capital of France?",
            answer="Paris",
            source_note=source_note,
        ),
    )

    assert "Medicine" in card.subdeck


@pytest.mark.parametrize(
    ("question", "answer", "reference_guid"),
    [
        ("What is the capital of France?", "Paris", 363791134),
        (
            "What *bold* [[Value]] is this?",
            "A. [[Bold value]].",
            8054042674,
        ),
    ],
)
def test_qa_prompt_uuid(
    question: str, answer: str, reference_guid: int
):
    source_prompt = MockPrompt()
    card = AnkiQA(
        fields=[question, answer, "extra", source_prompt.note_uuid],
        source_prompt=source_prompt,
    )
    assert reference_guid == card.card_uuid


@pytest.mark.parametrize(
    ("text", "reference_guid"), [(r"Test {{cloze}}", 6023539859)]
)
def test_cloze_uuid_generation(text: str, reference_guid: int):
    source_prompt = MockPrompt()
    card = AnkiCloze(
        fields=[text, "Extra", "Tags", source_prompt.note_uuid],
        source_prompt=source_prompt,
    )
    assert reference_guid == card.card_uuid


def test_get_bear_id():
    note_str = r"Q. A card with a GUID.\nA. And here is its answer.\n\nQS. How about a card like this?\nA. Yes, an answer too.\n\nQ. How about multiline questions?\n* Like this\n* Or this?\nA. What is the hash?\n\nAnd some {cloze} deletions? For sure! Multipe {even}.\n\n<!-- {BearID:7696CDCD-803A-40BC-88D8-855DDBEC56CA-31546-000054DF17EAE2C1} -->"

    expected_id = r"<!-- {BearID:7696CDCD-803A-40BC-88D8-855DDBEC56CA-31546-000054DF17EAE2C1} -->"

    extracted_id = extract_bear_guid(note_str)

    assert extracted_id == expected_id


@pytest.mark.parametrize(
    ("example_name", "example", "replaced"),
    [
        (
            "Two links",
            "Here I am [[alias|wiki link]], and another [[alias2|wiki link2]]",
            "Here I am [[wiki link]], and another [[wiki link2]]",
        ),
        (
            "Capitalization",
            "How was ice climbing [[Franz Josef]] with [[Vibeke Christiansen|Vibeke]]?",
            "How was ice climbing [[Franz Josef]] with [[Vibeke]]?",
        ),
        (
            "Parentheses",
            "[[Isolation (database design)|Isolation]]",
            "[[Isolation]]",
        ),
        ("Dashes", "[[test-test|test-]]", "[[test-]]"),
    ],
)
def test_alias_wiki_link_substitution(
    example_name: str,  # noqa: ARG001
    example: str,
    replaced: str,
):
    assert Document.replace_alias_wiki_links(example) == replaced
