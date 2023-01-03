import re

from .formats_constants import COUNTRIES_WITHOUT_POSTAL_CODE_SYSTEM, POSTAL_CODES_REGEX, STRICT_TERRITORY_POSTAL_CODES_REGEX


def country_without_postal_code(country_iso2: str) -> bool:
    """
    Verify that country that does not have (use) postal codes.

    :param country_iso2: String with ISO 3166-1 alpha-2 code which is two letter country code (e.g. US, DE, SK)
    :type country_iso2: str
    :return: function returns True/False depending if country does not use postal codes.
    :rtype: bool
    """
    if country_iso2 in COUNTRIES_WITHOUT_POSTAL_CODE_SYSTEM:
        return True

    return False


def get_countries_without_postal_code() -> tuple:
    """
    Get tuple of countries that does not have (use) postal codes.

    :return: function returns list (Python tuple) of countries that does not have (use) postal codes.
    :rtype: tuple
    """
    return tuple(COUNTRIES_WITHOUT_POSTAL_CODE_SYSTEM)


def has_postal_code(country_iso2: str) -> bool:
    """
    Verify that country that does have (use) postal codes.

    :param country_iso2: String with ISO 3166-1 alpha-2 code which is two letter country code (e.g. US, DE, SK)
    :type country_iso2: str
    :return: function returns True/False depending if country does use postal codes and have REGEX defined.
    :rtype: bool
    """
    if country_iso2 in POSTAL_CODES_REGEX:
        return True

    return False


def verify_postal_code_format(postal_code: str, country_iso2: str, strict=False) -> bool:
    """
    Validate postal_code, based on its country.

    :param postal_code: String containing given postal code
    :type postal_code: str
    :param country_iso2: String with ISO 3166-1 alpha-2 code which is two letter country code (e.g. US, DE, SK)
    :type country_iso2: str
    :param strict: Territories can be tested with more strict REGEX (default: False)
    :type strict: bool
    :return:
        function returns True/False according to presence of given combination of postal code and country
        within POSTAL_CODES_REGEX dictionary
    :rtype: bool
    """
    # if postal code of country which should have postal code has None value,
    # which would mess up re.match 'coz it's neither string nor byte
    if postal_code is None:
        return False

    if strict:
        merged_postal_code_regex = {**POSTAL_CODES_REGEX, **STRICT_TERRITORY_POSTAL_CODES_REGEX}
        return bool(re.match(merged_postal_code_regex[country_iso2], postal_code))

    return bool(re.match(POSTAL_CODES_REGEX[country_iso2], postal_code))


def get_postal_code_regex(country_iso2: str, strict=False) -> str:
    """
    Helper function to return REGEX that is used to verify the postal code.

    :param country_iso2: String with ISO 3166-1 alpha-2 code which is two letter country code (e.g. US, DE, SK)
    :type country_iso2: str
    :param strict: Territories can be tested with more strict REGEX (default: False)
    :type strict: bool
    :return: function returns REGEX that is used to verify the postal code string.
    :rtype: string
    """
    postal_code_regex = None

    if country_iso2 in POSTAL_CODES_REGEX:
        if strict:
            merged_postal_code_regex = {**POSTAL_CODES_REGEX, **STRICT_TERRITORY_POSTAL_CODES_REGEX}
            postal_code_regex = merged_postal_code_regex[country_iso2]
        else:
            postal_code_regex = POSTAL_CODES_REGEX[country_iso2]

    return postal_code_regex
