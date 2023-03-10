import os
from datetime import datetime

from application.main import *

IMPORT_TIME = "{}".format(datetime.now().strftime("%Y.%m/%d_%H:%M"))


def test_has_qa_matches():
    example_strings = [
        "QD. Testing something something",
        "QA. Testing something else, even with QA in it!",
        "\Q. Testing newlines as well!",
    ]

    matches = [string for string in example_strings if has_qa(string)]

    assert len(matches) == 3


def test_has_qa_does_not_match():
    example_strings = ["\nQ.E.D.", "> A question like this, or", "::Q. A comment!::"]

    matches = 0

    for string in example_strings:
        if has_qa(string):
            matches += 1

    assert matches == 0


def simple_has_answer_tests():
    list = [
        "QG. Hvilke overordnede kategorier [[Bensår]] findes?\n1) Venøse, 2) Arterielle, 3) Immunologisk"
    ]

    matches = [string for string in list if has_qa(string)]

    assert len(matches) == 1


def test_has_answer():
    example_1 = """
    Q. How do you write a classical, 3-part for loop in Javascript? 
A.
``` js
for (let i = 0; i < 4; i += 1) {
	console.log(i);
};
```


    """

    assert len(get_first_answer(example_1)) > 0

    example_2 = """
'QG. Hvor sidder et [[Angiopatisk diabetisk fodsår]] typisk?
A. Tæer eller fodryg.
![](BearImages/571434A5-E8B0-4F67-9269-1D0E968E7B24-62499-00007B8AE41283A1/23B8BF26-1E95-4DCD-AEBC-34722EB6CB27.png)
    """

    assert len(get_first_answer(example_2)) > 0


def test_block_breakage():
    with open("tests/test.md", "r", encoding="utf-8") as f:
        example_string = f.read()

        blocks = break_string_by_two_or_more_newlines(example_string)

        assert len(blocks) == 19


def test_q_production_from_file():
    card_generator = produce_cards_from_file("tests/test.md", import_time=IMPORT_TIME)

    file_blocks = []

    for item in card_generator:
        file_blocks.append({item.fields[0]: item.fields[1]})

    reference_blocks = [
        {
            "<p>Hvilke biokemiske faktorer <strong>leder til</strong> sekretion af <u>FSH</u>?   </p>\n": "<p><u>GnRH</u>  </p>\n"
        },
        {
            "<p>Hvilke biokemiske faktorer <strong>hæmmer</strong> sekretion af <u>FSH</u>?   </p>\n": "<p><u>Testosteron</u>/<u>Østrogen</u> og <u>Inhibin</u>  </p>\n"
        },
        {
            "<p>Hvilke(t) organ(er) påvirkes af <u>FSH</u>?   </p>\n": "<p>Ovarier/tests  </p>\n"
        },
        {
            "<p>{{c490::And now}} for some testing of cloze deletions –\xa0how much does this matter? More than me just accepting that it&#39;s missing deletions.</p>\n": '<h4 class="right"><a href="bear://x-callback-url/open-note?title=test&show_window=yes&new_window=yes&edit=yes">Bear</a></h4>'
        },
        {
            "<p>And now for some testing of cloze deletions –\xa0how much does this {{c236::matter}}? More than me just accepting that it&#39;s missing deletions.</p>\n": '<h4 class="right"><a href="bear://x-callback-url/open-note?title=test&show_window=yes&new_window=yes&edit=yes">Bear</a></h4>'
        },
        {
            "<p>And now for some testing of cloze deletions –\xa0how much does this matter? More than me just accepting that it&#39;s {{c892::missing}} deletions.</p>\n": '<h4 class="right"><a href="bear://x-callback-url/open-note?title=test&show_window=yes&new_window=yes&edit=yes">Bear</a></h4>'
        },
        {
            "<p>And now for some testing of cloze deletions –\xa0how much does this matter? More than me just accepting that it&#39;s missing {{c313::deletions}}.</p>\n": '<h4 class="right"><a href="bear://x-callback-url/open-note?title=test&show_window=yes&new_window=yes&edit=yes">Bear</a></h4>'
        },
    ]

    for i, reference in enumerate(reference_blocks):
        file_block = file_blocks[i]

        assert file_block == reference


def test_getting_content_only():
    test_string = """# Bensår
![](BearImages/C1C47096-5A13-4BC6-BDC6-CC0F126EA691-62499-00007BA30DD2A745/23B8BF26-1E95-4DCD-AEBC-34722EB6CB27.png)

## Backlinks
* [[Bensår]]
	* QG. Hvilke overordnede kategorier [[Bensår]] findes?
	* QG. Hvad er de hyppigste årsager til [[Bensår]]?
	* QG. Hvilke faktorer skal der spørges til specifikt for [[Bensår]]?
	* QG. Hvilke dele i den objektive us. er specifikt for [[Bensår]]?
* [[Pyoderma gangraenosum]]
	* [[Bensår]]

<!-- #anki/tag/med/Derma #anki/deck/Medicine #anki/tag/med/Endocrinology -->

<!-- {BearID:1062B55E-8F85-44C8-9271-FFC193FE1E6C-36407-0000013F9B8F0C61} -->
    """

    reference_string = "![](BearImages/C1C47096-5A13-4BC6-BDC6-CC0F126EA691-62499-00007BA30DD2A745/23B8BF26-1E95-4DCD-AEBC-34722EB6CB27.png)\n\n"

    content_only = get_content_only(test_string)

    assert content_only == reference_string


def test_card_guid():
    working_directory = os.getcwd()

    file_path = os.path.join(
        working_directory + "/tests/test_md_files/test_card_guid.md"
    )

    example_cards = produce_cards_from_file(file_path, import_time=IMPORT_TIME)

    reference_guids = [9315717920, 3912828915, 6300568814, 3001245253, 952903559]
    generated_guids = []

    for example_card in example_cards:
        generated_guids.append(example_card.guid())

    for i, ref_guid in enumerate(reference_guids):
        assert ref_guid == generated_guids[i]


def test_header_removal():
    working_directory = os.getcwd()

    file_path = os.path.join(
        working_directory + "/tests/test_md_files/test_header_removal.md"
    )

    example_cards = produce_cards_from_file(file_path, import_time=IMPORT_TIME)

    reference_guids = [9360765022, 1138085893]
    generated_guids = []

    for example_card in example_cards:
        generated_guids.append(example_card.guid())

    for i, ref_guid in enumerate(reference_guids):
        assert ref_guid == generated_guids[i]
