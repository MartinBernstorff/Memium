from collections.abc import Sequence

from memium.destination.ankiconnect.ankiconnect_requester import AnkiConnectCommand, AnkiRequester


class AmbiguousDeckNameError(Exception):
    pass


def resolve_deck_path(deck_name: str, existing_decks: Sequence[str]) -> str:
    """Find the full path of the deck whose path ends with deck_name, e.g. 'Memium' -> 'Parent::Memium'.

    Allows the user to move the deck within Anki without updating the configuration.
    If no deck matches, deck_name is returned as-is, and the deck is created on the first sync."""
    name_segments = deck_name.split("::")
    matches = [
        deck for deck in existing_decks if deck.split("::")[-len(name_segments) :] == name_segments
    ]

    if len(matches) > 1:
        raise AmbiguousDeckNameError(
            f"Deck name '{deck_name}' matches multiple decks: {sorted(matches)}. Specify more of the path, e.g. '{sorted(matches)[0]}'."
        )

    return matches[0] if matches else deck_name


def resolve_deck_path_in_anki(deck_name: str, anki_requester: AnkiRequester) -> str:
    existing_decks: Sequence[str] = anki_requester.invoke(AnkiConnectCommand.DECK_NAMES)
    return resolve_deck_path(deck_name, existing_decks)
