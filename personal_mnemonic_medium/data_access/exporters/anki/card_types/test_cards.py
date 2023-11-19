from collections.abc import Sequence
from pathlib import Path

import pytest

from personal_mnemonic_medium.data_access.document_ingesters.document import (
    Document,
)
from personal_mnemonic_medium.data_access.document_ingesters.markdown_ingester import (
    MarkdownIngester,
)
from personal_mnemonic_medium.data_access.document_ingesters.uuid_handling import (
    extract_bear_guid,
)
from personal_mnemonic_medium.data_access.exporters.anki.card_types.qa import (
    AnkiQA,
)
from personal_mnemonic_medium.data_access.exporters.anki.package_generator import (
    AnkiPackageGenerator,
)
from personal_mnemonic_medium.domain.card_pipeline import CardPipeline
from personal_mnemonic_medium.domain.prompt_extractors.base import (
    PromptExtractor,
)
from personal_mnemonic_medium.domain.prompt_extractors.cloze_extractor import (
    ClozePromptExtractor,
)
from personal_mnemonic_medium.domain.prompt_extractors.qa_extractor import (
    QAPrompt,
    QAPromptExtractor,
)


class MockCardPipeline(CardPipeline):
    def __init__(
        self,
        prompt_extractors: Sequence[PromptExtractor] | None = None,
    ) -> None:
        prompt_extractors = (
            prompt_extractors
            if prompt_extractors is not None
            else [
                QAPromptExtractor(
                    question_prefix="Q.", answer_prefix="A."
                ),
                ClozePromptExtractor(),
            ]
        )

        super().__init__(
            document_factory=MarkdownIngester(
                cut_note_after="# Backlinks",
                uuid_extractor=extract_bear_guid,
                uuid_generator=None,
            ),
            prompt_extractors=prompt_extractors,
            card_exporter=AnkiPackageGenerator(),
        )


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


def test_qa_uuid_generation():
    # TODO: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues/204 Remove dependency on test_md_files
    file_path = Path(__file__).parent / "test_cards.md"
    cards = MockCardPipeline(
        prompt_extractors=[
            QAPromptExtractor(
                question_prefix="Q.", answer_prefix="A."
            )
        ]
    ).run(input_path=file_path)
    notes = [c.to_genanki_note() for c in cards]

    field_guids: set[str] = {note.guid for note in notes}  # type: ignore
    reference_guids = {9315717920, 3912828915, 6300568814}
    generated_guids = {card.card_uuid for card in cards}

    assert reference_guids == generated_guids == field_guids


def test_cloze_uuid_generation():
    file_path = Path(__file__).parent / "test_cards.md"
    cloze_cards = MockCardPipeline(
        prompt_extractors=[ClozePromptExtractor()]
    ).run(input_path=file_path)

    cloze_generated_guids = {card.card_uuid for card in cloze_cards}
    cloze_reference_guids = {3001245253, 952903559}
    assert cloze_reference_guids == cloze_generated_guids


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
