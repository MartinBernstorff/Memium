from .base_diff_determiner import GeneralSyncer


def test_diff_determiner():
    syncer = GeneralSyncer(
        source={"a": 1, "b": 2}, destination={"b": "2", "c": "3"}
    )

    assert syncer.only_in_source() == [1]
    assert syncer.only_in_destination() == ["3"]
