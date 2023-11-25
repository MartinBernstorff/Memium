from pathlib import Path

from personal_mnemonic_medium.data_access.document_ingesters.document import (
    Document,
)
from personal_mnemonic_medium.data_access.exporters.anki.card_types.qa import (
    AnkiQA,
)
from personal_mnemonic_medium.data_access.exporters.anki.sync.disk.to_apkg import (
    SkippedDeck,
    cards_to_apkg,
)
from personal_mnemonic_medium.domain.prompt_extractors.qa_extractor import (
    QAPrompt,
)


def mock_qa() -> AnkiQA:
    return AnkiQA(
        fields=[""],
        source_prompt=QAPrompt(
            question="What is the capital of France?",
            answer="Paris",
            source_note=Document(
                content="Q. What is the capital of France?\nA. Paris",
                uuid="1234",
                source_path=Path(__file__),
            ),
        ),
    )


def test_cards_to_apkg(tmpdir: Path):
    deck_path = cards_to_apkg([mock_qa()], output_dir=tmpdir)
    assert isinstance(deck_path, Path)
    assert deck_path.exists()

    deck_path = cards_to_apkg(
        [mock_qa()], output_dir=tmpdir, skip_decks=["Default"]
    )
    assert isinstance(deck_path, SkippedDeck)
