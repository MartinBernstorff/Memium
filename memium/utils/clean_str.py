import re

import pytest
import unidecode
from bs4 import BeautifulSoup

from memium.str_utils.hasher import hash_str_to_int


def _hash_cleaned_str(input_str: str) -> int:
    return hash_str_to_int(clean_str(input_str))


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("Is <2, but >4", "is_2_but_4"),
        ("Q. ![](src). Question?", "q_src_question"),
        ("pre <img src='testsrc' /> post", "pre_testsrc_post"),
        ("\t", ""),
        ("\n", ""),
        ("""1. One\n\t2. Two""", "one_two"),
        ("""* One\n\t* Two""", "one_two"),
        ("""- One\n\t- Two""", "one_two"),
        ("[link1](blah) and [link2](blah)", "link1_and_link2"),
    ],
)
def should_clean_strings(input_str: str, expected: str):
    assert clean_str(input_str) == expected


@pytest.mark.parametrize(("input_str", "hash_identical_str"), [("<p>Test</p>", "Test"), ("å", "å")])
def should_remove_html_tags(input_str: str, hash_identical_str: str):
    assert _hash_cleaned_str(input_str) == _hash_cleaned_str(hash_identical_str)


def should_ignore_punctuation():
    strings_should_hash_to_identical = ["this", "This"]

    punctuation = r"!().,:;/"
    strings_should_hash_to_identical += [
        f"{s}{punctuation}" for s in strings_should_hash_to_identical
    ]

    assert len({hash_str_to_int(clean_str(s)) for s in strings_should_hash_to_identical}) == 1


def _replace_whitespace(text: str) -> str:
    return "_".join(text.split())


def _remove_non_content_html_tags(text: str) -> str:
    """Remove non-content html tags from a string."""
    soup = BeautifulSoup(text, "html.parser")

    for img in soup.find_all("img"):
        if img.get("src"):
            img.replace_with(img["src"])
        else:
            img.delete()

    return soup.text


def _remove_punctuation(text: str) -> str:
    """Clean string before hashing, so changes to spacing, punctuation, newlines etc. do not affect the hash."""
    lowered = text.lower()

    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`|~"""
    cleaned = lowered.translate(str.maketrans("", "", punctuation))

    return cleaned


def _remove_markdown_links(text: str) -> str:
    """Get the text from markdown links, e.g. '[link text](link url)' -> 'link text'"""
    return re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)


def _decode_unicode(text: str) -> str:
    """Standardise accents in a string."""
    return unidecode.unidecode(text)


def _remove_list_markup(text: str) -> str:
    """Remove markdown list markup, including '1. Item', '*' and '-'."""
    without_list_numbers = re.sub(r"^\s*\d+\. ", "", text, flags=re.MULTILINE)
    without_bullets = re.sub(r"^\s\* ", "", without_list_numbers, flags=re.MULTILINE)
    without_dashes = re.sub(r"^\s- ", "", without_bullets, flags=re.MULTILINE)
    return without_dashes


def clean_str(input_str: str) -> str:
    """Clean string before hashing, so changes to spacing, punctuation, newlines etc. do not affect the hash."""
    cleaned = input_str

    for cleaner in [
        _remove_non_content_html_tags,
        _remove_markdown_links,
        _remove_list_markup,
        _remove_punctuation,
        _decode_unicode,
        _replace_whitespace,
    ]:
        cleaned = cleaner(cleaned)

    return cleaned
