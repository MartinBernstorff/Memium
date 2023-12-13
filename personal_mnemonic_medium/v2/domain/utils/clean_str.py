from .int_hash_str import int_hash_str


def hash_cleaned_str(input_str: str) -> int:
    """Hash a string after cleaning it."""
    cleaned = clean_str(input_str)
    return int_hash_str(cleaned)


def clean_str(input_str: str) -> str:
    """Clean string before hashing, so changes to spacing, punctuation, newlines etc. do not affect the hash."""
    lowered = input_str.lower()

    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`|~"""
    cleaned = lowered.translate(
        str.maketrans("", "", punctuation)
    ).replace(" ", "")

    return cleaned
