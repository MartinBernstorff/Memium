# Anki 2.1 has mathjax built in, but ankidroid and other clients don't.
from typing import Any

# TODO: https://github.com/MartinBernstorff/personal-mnemonic-medium/issues/222 refactor: remove globals.py

ANKICONNECT_URL = (
    "http://host.docker.internal:8765"
)  # On host machine, port is 8765


VERSION = "0.1"

VERSION_LOG: dict[Any, Any] = {}
Q_TYPE_TAG = {
    "G": "med/type/1_GP",
    "A": "med/type/2_Acute_care",
    "I": "med/type/3_Internal_medicine",
    "S": "med/type/4_Specialty",
    "D": "med/type/5_Disabled",
    ".": "",
}
