import pytest

from personal_mnemonic_medium.data_access.document_ingesters.uuid_handling import (
    extract_bear_guid,
    generate_bear_guid,
)


def test_extract_bear_guid():
    test_double_guid = f"{generate_bear_guid()}{generate_bear_guid()}"

    with pytest.raises(IndexError):
        extract_bear_guid(test_double_guid)

    extract_bear_guid(generate_bear_guid())
