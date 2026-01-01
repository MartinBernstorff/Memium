import pytest
from inline_snapshot import snapshot

from memium.source.prompt import QAPrompt, obsidian_url


def test_file_title_to_uri():
    title = "Heap Properties"
    assert obsidian_url(title, 5) == snapshot(
        "obsidian://advanced-uri?filename=Heap%20Properties&line=5"
    )


def test_should_error_on_styling():
    with pytest.raises(ValueError) as excinfo:  # noqa: PT011
        QAPrompt(question="Testing <p style='opacity: 1'>", answer="")

    assert str(excinfo.value) == snapshot("""\
1 validation error for QAPrompt
  Value error, 'style=' found in question [type=value_error, input_value={'question': "Testing <p ...ity: 1'>", 'answer': ''}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/value_error\
""")
