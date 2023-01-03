# List of territory to parent country mappings
TERRITORY_COUNTRY_MAP = {
    "AX": "FI",
    "BL": "FR",
    "GF": "FR",
    "GP": "FR",
    "MC": "FR",
    "MF": "FR",
    "MQ": "FR",
    "PM": "FR",
    "RE": "FR",
    "YT": "FR",
    "EH": "MA",
    "SJ": "NO",
    "PR": "US",
}


def territory_to_parent_mapper(country_iso2: str) -> str:
    """
    Maps territories to countries if the mapping exists.

    :param country_iso2: String containing ISO2 code.
    :return: If country exists in TERRITORY_COUNTRY_MAP, return the mapped country,
             Else return input country_iso2.
    """
    return TERRITORY_COUNTRY_MAP.get(country_iso2, country_iso2)
