from memium.source.prompts.prompt_from_doc import obsidian_url


def test_file_title_to_uri(snapshot: str):
    title = "Heap Properties"
    assert snapshot == obsidian_url(title, 5)
