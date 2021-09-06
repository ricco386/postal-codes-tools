from postal_codes_tools.postal_codes import verify_postal_code_format


def test_verify_postal_code_formats():
    # Samples from European Central Bank spreadsheet
    assert verify_postal_code_format(postal_code='123', postal_code_country='DE') is True
