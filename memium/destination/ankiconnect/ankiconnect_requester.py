import json
import logging
import urllib.request
from dataclasses import dataclass
from enum import Enum
from time import sleep
from typing import Any

from memium.environment import in_docker

log = logging.getLogger(__name__)


class AnkiConnectCommand(Enum):
    IMPORT_PACKAGE = "importPackage"

    # Notes
    ADD_NOTE = "addNote"
    GET_NOTE_INFOS = "notesInfo"
    UPDATE_NOTE = "updateNote"
    DELETE_NOTES = "deleteNotes"

    # Cards
    CARD_INFO = "cardsInfo"
    CARDS_TO_NOTES = "cardsToNotes"
    FIND_CARDS = "findCards"
    CHANGE_DECK = "changeDeck"

    # Models
    CREATE_MODEL = "createModel"
    UPDATE_MODEL_TEMPLATES = "updateModelTemplates"
    UPDATE_MODEL_STYLING = "updateModelStyling"
    GET_MODEL_NAMES = "modelNames"


ANKICONNECT_URL = "http://host.docker.internal:8765" if in_docker() else "http://127.0.0.1:8765"


def anki_connect_is_live(ankiconnect_url: str = ANKICONNECT_URL) -> bool:
    try:
        if urllib.request.urlopen(ankiconnect_url).getcode() == 200:
            return True
        raise Exception
    except Exception as err:
        log.info(f"Attempted connection on {ankiconnect_url}")
        log.info(
            "Unable to reach anki connect. Make sure anki is running and the Anki Connect addon is installed."
        )
        log.error(f"Error was {err}")

    return False


@dataclass
class AnkiRequester:
    ankiconnect_url: str
    max_wait_seconds: int

    def __post_init__(self) -> None:
        seconds_waited = 0
        while not anki_connect_is_live(ankiconnect_url=self.ankiconnect_url):
            if seconds_waited >= self.max_wait_seconds:
                raise ConnectionError(f"Could not connect to AnkiConnect at {self.ankiconnect_url}")

            poll_seconds = 10
            log.info(f"AnkiConnect is not live, waiting {poll_seconds} seconds...")
            seconds_waited += poll_seconds
            sleep(poll_seconds)

    def _request(self, action: Any, **params: Any) -> dict[str, Any]:
        return {"action": action, "params": params, "version": 6}

    def invoke(self, action: AnkiConnectCommand, **params: Any) -> Any:
        """Helper for invoking actions with anki-connect
        Args:
            action (string): the action to invoke
        Raises:
            Exception: invalid fields provided
        Returns:
            Any: the response from anki connect
        """
        requestJson = json.dumps(self._request(action.value, **params)).encode("utf-8")
        response = json.load(
            urllib.request.urlopen(urllib.request.Request(self.ankiconnect_url, requestJson))
        )
        if len(response) != 2:
            raise Exception("response has an unexpected number of fields")
        if response["error"] is not None:
            raise Exception(response["error"])
        return response["result"]
