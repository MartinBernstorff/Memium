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
        QAPrompt("Testing <p style='opacity: 1'>", "")

    assert str(excinfo.value) == snapshot("'style=' found in question")
