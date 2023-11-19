# Anki 2.1 has mathjax built in, but ankidroid and other clients don't.
import textwrap
from typing import Any

from personal_mnemonic_medium.data_access.exporters.anki.anki_css import (
    CARD_MODEL_CSS,
)

# TODO: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues/222 refactor: remove globals.py

ANKICONNECT_URL = (
    "http://host.docker.internal:8765"
)  # On host machine, port is 8765

CARD_MATHJAX_CONTENT = textwrap.dedent(
    """\

"""
)

VERSION = "0.1"

CLOZE_MODEL_TEMPLATE = [
    {
        "name": "Ankdown Cloze Card with UUID",
        "qfmt": r"{{{{cloze:Text}}}}\n<div class='extra'>{{{{Extra}}}}</div>\n{}".format(
            CARD_MATHJAX_CONTENT
        ),
        "afmt": r"{{{{cloze:Text}}}}\n<div class='extra'>{{{{Extra}}}}</div>\n{}".format(
            CARD_MATHJAX_CONTENT
        ),
    }
]

CONFIG = {
    "pkg_arg": "AnkdownPkg.apkg",
    "recur_dir": ".",
    "dollar": False,
    "updated_only": False,
    "version_log": ".mdvlog",
    "card_model_name_cloze": "Ankdown Cloze with UUID",
    "card_model_name_qa": "Ankdown QA with UUID",
    "card_model_css": CARD_MODEL_CSS,
    "card_model_fields_cloze": [
        {"name": "Text"},
        {"name": "Extra"},
        {"name": "Tags"},
        {"name": "UUID"},
    ],
    "card_model_fields_qa": [
        {"name": "Question"},
        {"name": "Answer"},
        {"name": "Extra"},
        {"name": "UUID"},
    ],
    "card_model_template_qa": QA_MODEL_TEMPLATE,
    "card_model_template_cloze": CLOZE_MODEL_TEMPLATE,
}

VERSION_LOG: dict[Any, Any] = {}
Q_TYPE_TAG = {
    "G": "med/type/1_GP",
    "A": "med/type/2_Acute_care",
    "I": "med/type/3_Internal_medicine",
    "S": "med/type/4_Specialty",
    "D": "med/type/5_Disabled",
    ".": "",
}
