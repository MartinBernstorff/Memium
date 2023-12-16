from personal_mnemonic_medium.domain.utils.clean_str import clean_str
from personal_mnemonic_medium.domain.utils.int_hash_str import (
    int_hash_str,
)


def hash_cleaned_str(input_str: str) -> int:
    """Hash a string after cleaning it."""
    cleaned = clean_str(input_str)
    hashed = int_hash_str(cleaned)
    return hashed
