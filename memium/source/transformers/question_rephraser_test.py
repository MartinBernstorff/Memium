import os
from unittest.mock import patch

import pytest

from .question_rephraser import _rephrase_question, get_ttl_hash  # type: ignore


@pytest.mark.skipif(
    not os.getenv("ANTHROPIC_API_KEY"), reason="ANTHROPIC_API_KEY environment variable is not set"
)
@pytest.mark.parametrize(
    ("question", "answer", "expected_contains"),
    [
        ("what's the city that's the capital in _France_?", "Paris", ["France", "capital"]),
        (
            "what programming language is _Python_?",
            "Python is a high-level programming language",
            ["_Python_"],
        ),
        (
            "If _Kubernetes_ fails to spin up a pod for a job, what can you find in _K9s_?",
            "The job resource exists as a failure, the pod does not.",
            ["_Kubernetes_", "_K9s"],
        ),
    ],
)
def test_rephrase_question(question: str, answer: str, expected_contains: str):
    result = _rephrase_question(question, answer, "", "1")

    assert len(result) > 0
    for expected in expected_contains:
        assert expected.lower() in result.lower()
    assert result.endswith("?")
    assert result != question


def test_get_ttl_hash():
    with patch("time.time") as mock_time:
        # Test same hash within time window
        mock_time.return_value = 0
        hash1 = get_ttl_hash(60)

        mock_time.return_value = 59
        hash2 = get_ttl_hash(60)
        assert hash1 == hash2  # Should return same hash within 60 seconds

        # Test different hash across time window
        mock_time.return_value = 60
        hash3 = get_ttl_hash(60)
        assert hash1 != hash3  # Should return different hash after 60 seconds
