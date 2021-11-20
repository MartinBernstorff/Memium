import json
import typing as t
import urllib.request
from pathlib import Path

from genanki import Model

anki_connect_url = "http://localhost:8765"


# helper for creating anki connect requests
def request(action, **params):
    return {"action": action, "params": params, "version": 6}


# helper for invoking actions with anki-connect
def invoke(action, **params):
    """Helper for invoking actions with anki-connect
    Args:
        action (string): the action to invoke
    Raises:
        Exception: invalid fields provided
    Returns:
        Any: the response from anki connect
    """
    global anki_connect_url
    requestJson = json.dumps(request(action, **params)).encode("utf-8")
    response = json.load(
        urllib.request.urlopen(urllib.request.Request(anki_connect_url, requestJson))
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


def anki_connect_is_live():
    global anki_connect_url
    try:
        if urllib.request.urlopen(anki_connect_url).getcode() == 200:
            return True
        else:
            raise Exception()
    except Exception:
        print_error(
            "Unable to reach anki connect. Make sure anki is running and the Anki Connect addon is installed.",
        )

    return False


# synchronize the deck with markdown
# Borrowed from https://github.com/lukesmurray/markdown-anki-decks/blob/de6556d7ecd2d39335607c05171f8a9c39c8f422/markdown_anki_decks/sync.py#L64
def sync_package(pathToDeckPackage: Path):
    if anki_connect_is_live():
        pathToDeckPackage = pathToDeckPackage.resolve()
        try:
            invoke("importPackage", path=str(pathToDeckPackage))
            print(f"Imported {pathToDeckPackage}!")
        except Exception as e:
            print(f"Unable to import {pathToDeckPackage} to anki")
            print(f"\t{e}")


# synchronize the model and styling in the deck
def sync_model(model: Model):
    model_names_to_ids = dict()
    try:
        model_names_to_ids = invoke("modelNamesAndIds")
        if model.name not in model_names_to_ids:
            return
    except Exception as e:
        print_error("\tUnable to fetch existing model names and ids from anki")
        print_error(f"\t\t{e}")

    if anki_connect_is_live():
        try:
            invoke(
                "updateModelTemplates",
                model={
                    "name": model.name,
                    "templates": {
                        t["name"]: {
                            "qfmt": t["qfmt"],
                            "afmt": t["afmt"],
                        }
                        for t in model.templates
                    },
                },
            )
            print_success(f"\tUpdated model {model.name} template")
        except Exception as e:
            print_error(f"\tUnable to update model {model.name} template")
            print_error(f"\t\t{e}")

        try:
            invoke(
                "updateModelStyling",
                model={
                    "name": model.name,
                    "css": model.css,
                },
            )
            print_success(f"\tUpdated model {model.name} css")
        except Exception as e:
            print_error(f"\tUnable to update model {model.name} css")
            print_error(f"\t\t{e}")
