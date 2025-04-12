from inline_snapshot import snapshot

from memium.source.prompts.prompt_qa import obsidian_url


def test_file_title_to_uri():
    title = "Heap Properties"
    assert obsidian_url(title, 5) == snapshot(
        "obsidian://advanced-uri?filename=Heap%20Properties&line=5"
    )
