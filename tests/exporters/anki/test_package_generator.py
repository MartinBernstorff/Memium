from personal_mnemonic_medium.exporters.anki.anki_card import AnkiCard
from personal_mnemonic_medium.exporters.anki.package_generator import PackageGenerator


def test_package_generators():
    genanki_notes = [
        AnkiCard(
            fields=["Q. What is the capital of France?", "A. Paris"],
            source_markdown="Q. What is the capital of France?\nA. Paris",
            tags=["test"],
            model_type="QA",
            uuid="1234",
        )
        for _ in range(4)
    ]

    PackageGenerator().cards_to_package(cards=genanki_notes, output_path="test_package")
