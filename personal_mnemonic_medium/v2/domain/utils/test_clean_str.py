from .clean_str import clean_str


def test_clean_str():
    input_str = "This is  a test string!"
    assert clean_str(input_str) == "this_is_a_test_string".replace(
        "_", ""
    )
