DEFAULT_REGEX = "^.{1,255}$"

POSTAL_CODES_REGEX = {
    "AD": r"^AD\d{3}$",
    "AF": r"^\d{4}$",
    "AG": DEFAULT_REGEX,
    "AI": r"^(AI-2640)$",
    "AL": r"^\d{4}$",
    "AM": r"^(\d{4})|(\d{6})$",
    "AQ": r"^(7151)$",
    "AR": r"^([A-Z]\d{4}[A-Z]{3})|([A-Z]\d{4})$",
    "AS": r"^967\d{2}(-\d{4})?$",
    "AT": r"^\d{4}$",
    "AU": r"^\d{4}$",
    "AZ": r"^(AZ)(\d{4})|(AZ )(\d{4})$",
    "BA": r"^\d{5}$",
    "BB": r"^BB\d{5}$",
    "BD": r"^\d{4}$",
    "BE": r"^\d{4}$",
    "BF": r"^[1-9]\d{4}$",
    "BG": r"^\d{4}$",
    "BH": r"^\d{3}\d?$",
    "BM": r"^[A-Z]{2} \d{2}$",
    "BN": r"^[A-Z]{2}\d{4}$",
    "BR": r"^[0-9]{5}-[0-9]{3}$",
    "BT": r"^\d{5}$",
    "BY": r"^\d{6}$",
    "CA": r"^[A-Z][0-9][A-Z] [0-9][A-Z][0-9]$",
    "CC": r"^(6799)$",
    "CH": r"^[1-9]\d{3}$",
    "CL": r"^\d{7}$",
    "CN": r"^\d{6}$",
    "CO": r"^\d{6}$",
    "CR": r"^\d{5}$",
    "CU": r"^(CP)?\d{5}$",
    "CV": r"^\d{4}$",
    "CX": r"^(6798)$",
    "CY": r"^[1-9]\d{3}$",
    "CZ": r"^([1-7][0-9]{2} [0-9]{2}|[1-7][0-9]{4})$",
    "DE": r"^\d{5}$",
    "DK": r"^\d{4}$",
    "DO": r"^\d{5}$",
    "DZ": r"^\d{5}$",
    "EC": r"^\d{6}$",
    "EE": r"^\d{5}$",
    "EG": r"^\d{5}$",
    "ES": r"^\d{5}$",
    "ET": r"^\d{4}$",
    "FI": r"^\d{5}$",
    "FK": r"^(FIQQ 1ZZ)$",
    "FM": r"^9694\d{1}(-\d{4})?$",
    "FO": r"^\d{3}$",
    "FR": r"^\d{5}$",
    "GB": r"^([G][I][R] 0[A]{2})|((([A-Z][0-9]{1,2})|(([A-Z][A-HJ-Y][0-9]{1,2})|(([A-Z][0-9][A-Z])"
    r"|([A-Z][A-HJ-Y][0-9]?[A-Z])))) [0-9][A-Z]{2})$",
    "GE": r"^\d{4}$",
    "GG": r"^(GY)([0-9][0-9A-HJKPS-UW]?|[A-HK-Y][0-9][0-9ABEHMNPRV-Y]?) [0-9][ABD-HJLNP-UW-Z]{2}$",
    "GI": r"^(GX11 1AA)$",
    "GL": r"^39\d{2}$",
    "GN": r"^\d{3}$",
    "GR": r"^(\d{3}) \d{2}|\d{5}$",
    "GS": r"^(SIQQ 1ZZ)$",
    "GT": r"^\d{5}$",
    "GU": r"^((969)[1-3][0-2])(-\d{4})?$",
    "GW": r"^\d{4}$",
    "HK": r"^(999077)$",
    "HM": r"^(7151)$",
    "HN": r"^\d{5}$",
    "HR": r"^[1-5]\d{4}$",
    "HT": r"^(HT)(\d{4})|(HT) (\d{4})$",
    "HU": r"^[1-9]\d{3}$",
    "ID": r"^[1-9]\d{4}$",
    "IE": DEFAULT_REGEX,
    "IL": r"^\d{7}$",
    "IM": r"^(IM)([0-9][0-9A-HJKPS-UW]?|[A-HK-Y][0-9][0-9ABEHMNPRV-Y]?) [0-9][ABD-HJLNP-UW-Z]{2}$",
    "IN": r"^[1-9]\d{5}$",
    "IO": r"^(BB9D 1ZZ)$",
    "IQ": r"^\d{5}$",
    "IR": r"^\d{5}[\-]?\d{5}$",
    "IS": r"^[1-9]\d{2}$",
    "IT": r"^\d{5}$",
    "JE": r"^JE[0-9]{1}[\s]([\d][A-Z]{2})$",
    "JM": r"^(JM)[A-Z]{3}\d{2}$",
    "JO": r"^\d{5}$",
    "JP": r"^(\d{3}-\d{4})$",
    "KE": r"^\d{5}$",
    "KG": r"^\d{6}$",
    "KH": r"^\d{5,6}$",
    "KI": r"^KI\d{4}$",
    "KN": r"^KN\d{4}(\-\d{4})?$",
    "KR": r"^\d{5}$",
    "KW": r"^\d{5}$",
    "KY": r"^[K][Y][0-9]{1}[-]([0-9]){4}$",
    "KZ": r"^([A-Z]\d{2}[A-Z]\d[A-Z]\d)|(\d{6})$",
    "LA": r"^\d{5}$",
    "LB": r"^\d{4}( \d{4})?$",
    "LC": r"^LC\d{2} \d{3}$",
    "LI": r"^\d{4}$",
    "LK": r"^\d{5}$",
    "LR": r"^\d{4}$",
    "LS": r"^\d{3}$",
    "LT": r"^((LT)[\-])?(\d{5})$",
    "LU": r"^((L)[\-])?(\d{4})$",
    "LV": r"^((LV)[\-])?(\d{4})$",
    "LY": DEFAULT_REGEX,
    "MA": r"^[1-9]\d{4}$",
    "MD": r"^(MD[\-]?)?(\d{4})$",
    "ME": r"^\d{5}$",
    "MG": r"^\d{3}$",
    "MH": r"^((969)[6-7][0-9])(-\d{4})?$",
    "MK": r"^\d{4}$",
    "MM": r"^\d{5}$",
    "MN": r"^\d{5}$",
    "MO": DEFAULT_REGEX,
    "MP": r"^9695\d{1}(-\d{4})?$",
    "MS": r"^MSR\d{4}$",
    "MT": r"^[A-Z]{3} [0-9]{4}|[A-Z]{2}[0-9]{2}|[A-Z]{2} [0-9]{2}|[A-Z]{3}[0-9]{4}|[A-Z]{3}[0-9]{2}|[A-Z]{3} [0-9]{2}$",
    "MU": r"^([0-9A-R]\d{4})$",
    "MV": r"^\d{5}$",
    "MW": r"^\d{6}$",
    "MX": r"^\d{5}$",
    "MY": r"^\d{5}$",
    "MZ": r"^\d{4}$",
    "NA": r"^\d{5}$",
    "NC": r"^988\d{2}$",
    "NE": r"^\d{4}$",
    "NF": r"^(2899)$",
    "NG": r"^[1-9]\d{5}$",
    "NI": r"^\d{5}$",
    "NL": r"^[1-9]\d{3} [A-Z]{2}|[1-9]\d{3}[A-Z]{2}$",
    "NO": r"^\d{4}$",
    "NP": r"^\d{5}$",
    "NR": r"^(NRU68)$",
    "NU": r"^(9974)$",
    "NZ": r"^\d{4}$",
    "OM": r"^\d{3}$",
    "PA": r"^\d{4}$",
    "PE": r"^\d{5}$",
    "PF": r"^((987)\d{2})$",
    "PG": r"^\d{3}$",
    "PH": r"^\d{4}$",
    "PK": r"^[1-9]\d{4}$",
    "PL": r"^[0-9]{2}[-]([0-9]){3}$",
    "PN": r"^(PCR9 1ZZ)$",
    "PS": r"^(P[1-9]\d{6})|(\d{3}-\d{3})$",
    "PT": r"^[1-9]\d{3}((-)\d{3})$",
    "PW": r"^(96939|96940)$",
    "PY": r"^\d{4}$",
    "RO": r"^\d{6}$",
    "RS": r"^\d{5,6}$",
    "RU": r"^\d{6}$",
    "SA": r"^[1-8]\d{4}([\-]\d{4})?$",
    "SD": r"^\d{5}$",
    "SE": r"^[1-9]\d{2} \d{2}$",
    "SG": r"^\d{6}$",
    "SH": r"^(ASCN 1ZZ|TDCU 1ZZ|STHL 1ZZ)$",
    "SI": r"^[1-9]\d{3}$",
    "SK": r"^(\d{3} \d{2})|\d{5}$",
    "SM": r"^(4789\d)$",
    "SN": r"^[1-8]\d{4}$",
    "SO": DEFAULT_REGEX,
    "SS": r"^\d{5}$",
    "SV": r"^\d{4}$",
    "SZ": r"^([A-Z]\d{3})$",
    "TC": r"^(TKCA 1ZZ)$",
    "TF": DEFAULT_REGEX,
    "TH": r"^\d{5}$",
    "TJ": r"^7\d{5}$",
    "TM": r"^7\d{5}$",
    "TN": r"^\d{4}$",
    "TR": r"^\d{5}$",
    "TT": r"^\d{6}$",
    "TW": r"^(\d{3}\-\d{3})|(\d{3}[-]\d{2})|(\d{6})|(\d{3})$",
    "TZ": r"^\d{5}$",
    "UA": r"^\d{5}$",
    "US": r"^\d{5}(-\d{4})?$",
    "UY": r"^[1-9]\d{4}$",
    "UZ": r"^\d{6}$",
    "VA": r"^(00120)$",
    "VC": r"^(VC)(\d{4})$",
    "VE": r"^[1-8]\d{3}$",
    "VG": r"^(VG11)[0-6][0]$",
    "VI": r"^008\d{2}(-\d{4})?$",
    "VN": r"^\d{6}$",
    "WF": r"^(986)\d{2}$",
    "WS": r"^WS[1-2]\d{3}$",
    "ZA": r"^\d{4}$",
    "ZM": r"^\d{5}$",
    # Aland Islands (Finland system)
    "AX": r"^\d{5}$",
    # french territories
    "BL": r"^\d{5}$",
    "GF": r"^\d{5}$",
    "GP": r"^\d{5}$",
    "MC": r"^\d{5}$",
    "MF": r"^\d{5}$",
    "MQ": r"^\d{5}$",
    "PM": r"^\d{5}$",
    "RE": r"^\d{5}$",
    "YT": r"^\d{5}$",
    # end of french territories
    # Western Sahara (Morocco system)
    "EH": r"^[1-9]\d{4}$",
    # Puerto Rico (US system)
    "PR": r"^\d{5}(-\d{4})?$",
    # Svaldbard and Jan Mayen (Norway system)
    "SJ": r"^\d{4}$",
}

STRICT_TERRITORY_POSTAL_CODES_REGEX = {
    # Aland Islands (Finland system)
    "AX": r"^22\d{3}$",
    # french territories
    "BL": r"^(9709\d{1})|97133$",
    "GF": r"^973\d{2}$",
    "GP": r"^97[0-1]\d{2}$",
    "MC": r"^980\d{2}$",
    "MF": r"^97[0-1]\d{2}$",
    "MQ": r"^972\d{2}$",
    "PM": r"^975\d{2}$",
    "RE": r"^(974|977|978)\d{2}$",
    "YT": r"^(976|985)\d{2}$",
    # end of french territories
    # Western Sahara (Morocco system)
    "EH": r"^7\d{4}$",
    # Puerto Rico (US system)
    "PR": r"^00\d{3}(-\d{4})?$",
    # Svaldbard and Jan Mayen (Norway system)
    "SJ": r"^8099|(917[0-1])$",
}

# Countries without postal code system
# In ECB spreadsheet default REGEX was added and no example (same behaviour)
# Countries that have example, will match default REGEX
COUNTRIES_WITHOUT_POSTAL_CODE_SYSTEM = {
    "AE",
    "AO",
    "AW",
    "BI",
    "BJ",
    "BO",
    "BQ",
    "BS",
    "BV",
    "BW",
    "BZ",
    "CD",
    "CF",
    "CG",
    "CI",
    "CK",
    "CM",
    "CW",
    "DJ",
    "DM",
    "ER",
    "FJ",
    "GA",
    "GD",
    "GH",
    "GM",
    "GQ",
    "GY",
    "KM",
    "KP",
    "ML",
    "MR",
    "QA",
    "RW",
    "SB",
    "SC",
    "SL",
    "SR",
    "ST",
    "SX",
    "SY",
    "TD",
    "TG",
    "TK",
    "TL",
    "TO",
    "TV",
    "UG",
    "UM",
    "VU",
    "XX",
    "YE",
    "ZW",
}
