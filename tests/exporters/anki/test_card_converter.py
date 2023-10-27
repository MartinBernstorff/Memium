from collections.abc import Sequence
from pathlib import Path

from personal_mnemonic_medium.card_pipeline import CardPipeline
from personal_mnemonic_medium.exporters.anki.card_types.base import (
    AnkiCard,
)
from personal_mnemonic_medium.exporters.anki.card_types.qa import (
    AnkiQA,
)
from personal_mnemonic_medium.exporters.anki.package_generator import (
    AnkiPackageGenerator,
)
from personal_mnemonic_medium.exporters.base import CardExporter
from personal_mnemonic_medium.note_factories.base import (
    DocumentFactory,
)
from personal_mnemonic_medium.note_factories.markdown import (
    MarkdownNoteFactory,
)
from personal_mnemonic_medium.note_factories.note import Document
from personal_mnemonic_medium.prompt_extractors.base import (
    PromptExtractor,
)
from personal_mnemonic_medium.prompt_extractors.cloze_extractor import (
    ClozePromptExtractor,
)
from personal_mnemonic_medium.prompt_extractors.qa_extractor import (
    QAPrompt,
    QAPromptExtractor,
)


class TestCardPipeline(CardPipeline):
    def __init__(
        self,
        document_factory: DocumentFactory = MarkdownNoteFactory(),  # noqa: B008
        prompt_extractors: Sequence[PromptExtractor] = [
            QAPromptExtractor(),
            ClozePromptExtractor(),
        ],
        card_exporter: CardExporter = AnkiPackageGenerator(),  # noqa: B008
    ) -> None:
        super().__init__(
            document_factory=document_factory,
            prompt_extractors=prompt_extractors,
            card_exporter=card_exporter,
        )

    def test_card_pipeline(self, input_path: Path) -> list[AnkiCard]:
        return self.run(input_path=input_path)


def test_custom_card_to_genanki_card():
    source_note = Document(
        title="Test",
        content="Q. What is the capital of France?\nA. Paris",
        uuid="1234",
        source_path=Path(__file__),
    )
    AnkiQA(
        fields=["Q. What is the capital of France?", "A. Paris"],
        source_prompt=QAPrompt(
            question="What is the capital of France?",
            answer="Paris",
            note_uuid="1234",
            source_note=source_note,
        ),
    ).to_genanki_note()


def test_get_subtags():
    source_note = Document(
        title="Test",
        content="Testing subdeck extraction, #anki/deck/Medicine, #anki/tag/med/Endocrinology",
        uuid="1234",
        source_path=Path(__file__),
    )

    card = AnkiQA(
        fields=[""],
        source_prompt=QAPrompt(
            question="What is the capital of France?",
            answer="Paris",
            note_uuid="1234",
            source_note=source_note,
        ),
    )

    assert "Medicine" in card.subdeck


def test_qa_uuid_generation():
    file_path = (
        Path(__file__).parent.parent.parent
        / "test_md_files"
        / "test_card_guid.md"
    )
    cards = TestCardPipeline(
        prompt_extractors=[QAPromptExtractor()]
    ).run(input_path=file_path)
    notes = [c.to_genanki_note() for c in cards]

    field_guids = {note.guid for note in notes}
    reference_guids = {9315717920, 3912828915, 6300568814}
    generated_guids = {card.card_uuid for card in cards}

    assert reference_guids == generated_guids == field_guids


def test_cloze_uuid_generation():
    file_path = (
        Path(__file__).parent.parent.parent
        / "test_md_files"
        / "test_card_guid.md"
    )
    cloze_cards = TestCardPipeline(
        prompt_extractors=[ClozePromptExtractor()]
    ).run(input_path=file_path)

    cloze_generated_guids = {card.card_uuid for card in cloze_cards}
    cloze_reference_guids = {3001245253, 952903559}
    assert cloze_reference_guids == cloze_generated_guids


def test_get_bear_id():
    factory = MarkdownNoteFactory()
    note_str = r"Q. A card with a GUID.\nA. And here is its answer.\n\nQS. How about a card like this?\nA. Yes, an answer too.\n\nQ. How about multiline questions?\n* Like this\n* Or this?\nA. What is the hash?\n\nAnd some {cloze} deletions? For sure! Multipe {even}.\n\n<!-- {BearID:7696CDCD-803A-40BC-88D8-855DDBEC56CA-31546-000054DF17EAE2C1} -->"

    expected_id = r"<!-- {BearID:7696CDCD-803A-40BC-88D8-855DDBEC56CA-31546-000054DF17EAE2C1} -->"

    extracted_id = factory.get_note_id(note_str)

    assert extracted_id == expected_id


def test_alias_wiki_link_substitution():
    alias = "Here I am [[alias|wiki link]], and another [[alias2|wiki link2]]"
    output = Document.replace_alias_wiki_links(alias)
    assert (
        output
        == "Here I am [[wiki link]], and another [[wiki link2]]"
    )

    no_alias = "Here I am [[wiki link]] and another [[wiki link2]]"
    output = Document.replace_alias_wiki_links(no_alias)
    assert (
        output == "Here I am [[wiki link]] and another [[wiki link2]]"
    )

    test_3 = "How was ice climbing [[Franz Josef]] with [[Vibeke Christiansen|Vibeke]]?"
    output = Document.replace_alias_wiki_links(test_3)
    assert (
        output
        == "How was ice climbing [[Franz Josef]] with [[Vibeke]]?"
    )

    alias = "[[Isolation (database design)|Isolation]]"
    output = Document.replace_alias_wiki_links(alias)
    assert output == "[[Isolation]]"

    alias = "[[test-test|test-]]"
    output = Document.replace_alias_wiki_links(alias)
    assert output == "[[test-]]"
