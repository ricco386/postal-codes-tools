import re

from postal_codes_tools.formats_constants import COUNTRIES_WITHOUT_POSTAL_CODE_SYSTEM
from postal_codes_tools.formats_constants import POSTAL_CODES_REGEX


def country_without_postal_code(country_iso_code) -> bool:
    if country_iso_code in COUNTRIES_WITHOUT_POSTAL_CODE_SYSTEM:
        return True
    return False


def has_postal_code(country_iso_code) -> bool:
    if country_iso_code in POSTAL_CODES_REGEX:
        return True
    return False


def verify_postal_code_format(postal_code: str, country_iso_code: str) -> bool:
    """
    Validate postal_code, based on its country

    :param postal_code: String containing given postal code
    :param country_iso_code: String with ISO 3166-1 alpha-2 code which is two letter country code (e.g. US, DE, SK)

    :return:
        function returns True/False according to presence of given combination of postal code and country
        within POSTAL_CODES_REGEX dictionary
    """

    return bool(re.match(POSTAL_CODES_REGEX[country_iso_code], postal_code))
