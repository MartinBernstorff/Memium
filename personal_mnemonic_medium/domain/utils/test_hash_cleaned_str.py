from personal_mnemonic_medium.domain.utils.hash_cleaned_str import (
    hash_cleaned_str,
)


def test_hash_cleaned_str():
    identical_strings = [
        "This!",
        "This ",
        "this",
        "this(",
        "this.",
        "this,",
        "this:",
        "this;",
    ]

    assert len({hash_cleaned_str(s) for s in identical_strings}) == 1
