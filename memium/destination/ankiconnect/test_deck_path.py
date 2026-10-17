import pytest

from memium.destination.ankiconnect.deck_path import AmbiguousDeckNameError, resolve_deck_path


@pytest.mark.parametrize(
    ("deck_name", "existing_decks", "expected"),
    [
        ("Memium", ["Default", "Parent::Memium", "Parent::Memium::Python"], "Parent::Memium"),
        ("Memium", ["Memium", "Memium::Python"], "Memium"),
        ("Parent::Memium", ["Parent::Memium"], "Parent::Memium"),
        ("Memium", ["Default", "NotMemium"], "Memium"),
    ],
)
def test_resolve_deck_path(deck_name: str, existing_decks: list[str], expected: str):
    assert resolve_deck_path(deck_name, existing_decks) == expected


def test_resolve_deck_path_raises_on_ambiguous_name():
    with pytest.raises(AmbiguousDeckNameError):
        resolve_deck_path("Memium", ["A::Memium", "B::Memium"])


def test_resolve_deck_path_disambiguates_with_longer_suffix():
    assert resolve_deck_path("B::Memium", ["A::Memium", "B::Memium"]) == "B::Memium"
