import hashlib


def clean_str(input_str: str) -> str:
    """Clean string before hashing, so changes to spacing, punctuation, newlines etc. do not affect the hash."""
    lowered = input_str.lower()

    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`|~"""
    cleaned = lowered.translate(str.maketrans("", "", punctuation)).replace(
        " ", ""
    )

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


def hash_cleaned_str(input_str: str) -> int:
    """Hash a string after cleaning it."""
    cleaned = clean_str(input_str)
    hashed = int_hash_str(cleaned)
    return hashed
