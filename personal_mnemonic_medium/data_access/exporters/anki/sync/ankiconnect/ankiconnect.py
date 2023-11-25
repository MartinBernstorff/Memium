# helper for creating anki connect requests
import json
import urllib.request
from typing import Any

from personal_mnemonic_medium.data_access.exporters.anki.globals import (
    ANKICONNECT_URL,
)
from personal_mnemonic_medium.data_access.exporters.anki.sync.anki_sync import (
    msg,
)


def request(action: Any, **params: Any) -> dict[str, Any]:
    return {"action": action, "params": params, "version": 6}


# helper for invoking actions with anki-connect
def invoke(action: Any, **params: Any) -> Any:
    """Helper for invoking actions with anki-connect
    Args:
        action (string): the action to invoke
    Raises:
        Exception: invalid fields provided
    Returns:
        Any: the response from anki connect
    """
    requestJson = json.dumps(request(action, **params)).encode(
        "utf-8"
    )
    response = json.load(
        urllib.request.urlopen(
            urllib.request.Request(ANKICONNECT_URL, requestJson)
        )
    )
    if len(response) != 2:
        raise Exception("response has an unexpected number of fields")
    if "error" not in response:
        raise Exception("response is missing required error field")
    if "result" not in response:
        raise Exception("response is missing required result field")
    if response["error"] is not None:
        raise Exception(response["error"])
    return response["result"]


def anki_connect_is_live() -> bool:
    try:
        if urllib.request.urlopen(ANKICONNECT_URL).getcode() == 200:
            return True
        raise Exception
    except Exception as err:
        msg.info(f"Attempted connection on {ANKICONNECT_URL}")
        msg.info(
            "Unable to reach anki connect. Make sure anki is running and the Anki Connect addon is installed."
        )
        msg.fail(f"Error was {err}")

    return False
