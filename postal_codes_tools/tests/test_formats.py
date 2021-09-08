import pytest

from postal_codes_tools.postal_codes import verify_postal_code_format
from postal_codes_tools.postal_codes import country_without_postal_code
from postal_codes_tools.postal_codes import has_postal_code


def test_verify_postal_code_formats():
    # Samples from European Central Bank spreadsheet
    assert verify_postal_code_format(postal_code="12345", country_iso_code="DE") is True
    assert verify_postal_code_format(postal_code="123", country_iso_code="DE") is False
    assert verify_postal_code_format(postal_code="AD123", country_iso_code="AD") is True
    assert verify_postal_code_format(postal_code="AD1234", country_iso_code="AD") is False
    assert verify_postal_code_format(postal_code="AD12", country_iso_code="AD") is False
    assert verify_postal_code_format(postal_code="12345", country_iso_code="AD") is False


def test_check_country_which_has_postal_code():
    assert verify_postal_code_format(postal_code="TKCA 1ZZ", country_iso_code="TC") is True
    assert verify_postal_code_format(postal_code="TKCA1ZZ", country_iso_code="TC") is False
    assert verify_postal_code_format(postal_code="1234", country_iso_code="TC") is False
    assert verify_postal_code_format(postal_code="", country_iso_code="TC") is False

    assert country_without_postal_code("TC") is False
    assert has_postal_code("TC") is True


def test_verify_postal_code_for_countries_without_postal_code():
    with pytest.raises(KeyError):
        verify_postal_code_format(postal_code="", country_iso_code="AO")
    with pytest.raises(KeyError):
        assert verify_postal_code_format(postal_code="ASFAFS", country_iso_code="AO")

    assert country_without_postal_code("AO") is True
    assert country_without_postal_code("DE") is False

    assert has_postal_code("AO") is False


def test_verify_postal_code_for_unknown_countries():
    with pytest.raises(KeyError):
        assert verify_postal_code_format(postal_code="12345", country_iso_code="KK")
    with pytest.raises(KeyError):
        assert verify_postal_code_format(postal_code="", country_iso_code="KK")

    assert country_without_postal_code("KK") is False
    assert has_postal_code("KK") is False
