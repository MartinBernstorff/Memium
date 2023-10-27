import hashlib


def simple_hash(text: str) -> int:
    """MD5 of text, mod 2^63. Probably not a great hash function."""
    comp_hash = (
        int(hashlib.sha256(text.encode("utf-8")).hexdigest(), 16)
        % 10**10
    )

    return comp_hash
