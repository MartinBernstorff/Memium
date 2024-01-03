import hashlib
from collections.abc import Callable

from bs4 import BeautifulSoup


def remove_spaces(text: str) -> str:
    """Remove spaces from a string."""
    return text.replace(" ", "")


def remove_html_tags(text: str) -> str:
    clean_text = BeautifulSoup(text, "html.parser").text
    return clean_text


def remove_punctuation(text: str) -> str:
    """Clean string before hashing, so changes to spacing, punctuation, newlines etc. do not affect the hash."""
    lowered = text.lower()

    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`|~"""
    cleaned = lowered.translate(str.maketrans("", "", punctuation))

    return cleaned


def clean_str(input_str: str) -> str:
    """Clean string before hashing, so changes to spacing, punctuation, newlines etc. do not affect the hash."""
    cleaned = input_str

    for cleaner in [remove_html_tags, remove_punctuation, remove_spaces]:
        cleaned = cleaner(cleaned)

    return cleaned


def int_hash_str(input_string: str, max_length: int = 10) -> int:
    # Convert the string to bytes
    bytes_string = input_string.encode()

    # Create a SHA256 hash object
    hash_object = hashlib.sha256(bytes_string)

    # Hex digest the hash and convert it to an integer
    unique_int = int(hash_object.hexdigest(), 16)
    shortened = unique_int % 10**max_length

    return shortened


def hash_cleaned_str(
    input_str: str, cleaner: Callable[[str], str] = clean_str
) -> int:
    """Hash a string after cleaning it."""
    hashed = int_hash_str(cleaner(input_str))
    return hashed
