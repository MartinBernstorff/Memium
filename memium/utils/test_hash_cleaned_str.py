from .hash_cleaned_str import hash_cleaned_str


def test_hash_cleaned_str():
    strings_should_hash_to_identical = ["this", "This"]

    punctuation = r"!().,:;/"
    strings_should_hash_to_identical += [
        f"{s}{punctuation}" for s in strings_should_hash_to_identical
    ]

    assert (
        len({hash_cleaned_str(s) for s in strings_should_hash_to_identical})
        == 1
    )
