from pathlib import Path

import pytest
from inline_snapshot import snapshot

from memium.source.document import Document
from memium.source.prompt import QAPrompt, QAWithDoc, obsidian_url


def test_file_title_to_uri():
    assert obsidian_url("Heap Properties", 5, "My Vault") == snapshot(
        "obsidian://advanced-uri?vault=My%20Vault&filename=Heap%20Properties&line=5"
    )


def test_uri_targets_the_documents_vault():
    prompt = QAWithDoc.dummy(
        parent_doc=Document.dummy(source_path=Path("Note.md"), vault_name="My Vault"), line_nr=3
    )

    assert prompt.edit_url == snapshot(
        "obsidian://advanced-uri?vault=My%20Vault&filename=Note&line=3"
    )


def test_uri_without_vault_lets_obsidian_pick():
    prompt = QAWithDoc.dummy(
        parent_doc=Document.dummy(source_path=Path("Note.md"), vault_name=None), line_nr=3
    )

    assert prompt.edit_url == snapshot("obsidian://advanced-uri?filename=Note&line=3")


def test_prompts_cached_before_vaults_were_modelled_still_load():
    cached = '{"prompt":{"question":"Q","answer":"A"},"parent_doc":{"content":"c","source_path":"Note.md"},"line_nr":1,"render_parent_doc":true}'

    assert QAWithDoc.model_validate_json(cached).parent_doc.vault_name is None


def test_should_error_on_styling():
    with pytest.raises(ValueError) as excinfo:  # noqa: PT011
        QAPrompt(question="Testing <p style='opacity: 1'>", answer="")

    assert str(excinfo.value) == snapshot("""\
1 validation error for QAPrompt
  Value error, 'style=' found in question [type=value_error, input_value={'question': "Testing <p ...ity: 1'>", 'answer': ''}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/value_error\
""")
