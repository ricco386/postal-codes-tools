POSTAL_CODES_REGEX = {
    "AD": r"(?:AD)(\d{3})",
    "AF": r"^\d{4}$",
    "AG": r"^\d{5}$",
    "AI": r"^(AI-2640)$",
    "AL": r"^\d{4}$",
    "AM": r"(^\d{4}$)|(^\d{6}$)",
    "AQ": r"(7151)",
    "AR": r"(^[A-Z]\d{4}[A-Z]{3}$)|(^[A-Z]\d{4}$)",
    "AS": r"^\d{5}$",
    "AT": r"^\d{4}$",
    "AU": r"^\d{4}$",
    "AZ": r"^(AZ) (\d{4})$",
    "BA": r"^\d{5}$",
    "BB": r"^(?:BB)(\d{5})$",
    "BD": r"^\d{4}$",
    "BE": r"^\d{4}$",
    "BG": r"^\d{4}$",
    "BH": r"^\d{3}\d?$",
    "BM": r"^[A-Z]{2} \d{2}$",
    "BN": r"^[A-Z]{2}\d{4}$",
    "BR": r"^[0-9]{5}-[0-9]{3}$",
    "BT": r"^\d{5}$",
    "BY": r"^\d{6}$",
    "CA": r"^(?!.*[DFIOQU])[A-VXY][0-9][A-Z] +?[0-9][A-Z][0-9]$",
    "CC": r"^(6799)$",
    "CH": r"^\d{4}$",
    "CL": r"^\d{7}$",
    "CN": r"^\d{6}$",
    "CO": r"^\d{6}$",
    "CR": r"^\d{5}$",
    "CU": r"^(?:CP)(\d{5})$",
    "CV": r"^\d{4}$",
    "CX": r"^(6798)$",
    "CY": r"^\d{4}$",
    "CZ": r"(^[0-9]{3} [0-9]{2}$)|(^[0-9]{5}$)",
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
    "FM": r"^\d{5}$",
    "FO": r"^\d{3}$",
    "FR": r"^\d{5}$",
    "GB": r"(^[Gg][Ii][Rr] 0[Aa]{2}$)|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})"
    "|(([A-Za-z][0-9][A-Za-z])|"
    "([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) [0-9][A-Za-z]{2})",
    "GE": r"^\d{4}$",
    "GG": r"^(GY)([0-9][0-9A-HJKPS-UW]?|[A-HK-Y][0-9][0-9ABEHMNPRV-Y]?) [0-9][ABD-HJLNP-UW-Z]{2}$",
    "GI": r"^(GX11 1AA)$",
    "GL": r"^\d{4}$",
    "GN": r"^\d{3}$",
    "GR": r"^(\d{3}) \d{2}|\d{5}$",
    "GS": r"^(SIQQ 1ZZ)$",
    "GT": r"^\d{5}$",
    "GU": r"^((969)[1-3][0-2])$",
    "GW": r"^\d{4}$",
    "HK": r"^(999077)$",
    "HM": r"^(7151)$",
    "HN": r"^\d{5}$",
    "HR": r"^\d{5}$",
    "HT": r"^(?:HT)(\d{4})$",
    "HU": r"^\d{4}$",
    "ID": r"^\d{5}$",
    "IE": r"^STRNG_LTN_EXT_255$",
    "IL": r"^\d{7}$",
    "IM": r"(^(IM)([0-9][0-9A-HJKPS-UW]?$)|(^[A-HK-Y][0-9][0-9ABEHMNPRV-Y]?) [0-9][ABD-HJLNP-UW-Z]{2}$)",
    "IN": r"^\d{6}$",
    "IO": r"^(BB9D 1ZZ)$",
    "IQ": r"^\d{5}$",
    "IR": r"^\d{5}[\-]?\d{5}$",
    "IS": r"^\d{3}$",
    "IT": r"^\d{5}$",
    "JE": r"^JE[0-9]{1}[\s]([\d][A-Z]{2})$",
    "JM": r"^(JM)[A-Z]{3}\d{2}$",
    "JO": r"^\d{5}$",
    "JP": r"^(\d{3}-\d{4})$",
    "KE": r"^\d{5}$",
    "KG": r"^\d{6}$",
    "KH": r"^\d{5}$",
    "KR": r"^\d{5}$",
    "KW": r"^\d{5}$",
    "KY": r"^[K][Y][0-9]{1}[-]([0-9]){4}$",
    "KZ": r"^\d{6}$",
    "LA": r"^\d{5}$",
    "LB": r"^\d{4}( \d{4})?$",
    "LI": r"^\d{4}$",
    "LK": r"^\d{5}$",
    "LR": r"^\d{4}$",
    "LS": r"^\d{3}$",
    "LT": r"^((?:LT)[\-])?(\d{5})$",
    "LU": r"^((?:L)[\-])?(\d{4})$",
    "LV": r"^[L]{1}[V]{1}[-]([0-9]){4}$",
    "MA": r"^\d{5}$",
    "MD": r"^(?:MD)[\-]?(\d{4})$",
    "ME": r"^\d{5}$",
    "MG": r"^\d{3}$",
    "MH": r"^((969)[6-7][0-9])$",
    "MK": r"^\d{4}$",
    "MM": r"^\d{5}$",
    "MN": r"^\d{5}$",
    "MO": r"^(999078)$",
    "MP": r"^\d{5}$",
    "MS": r"^(?:MSR )(\d{4})$",
    "MT": r"[A-Z]{3} [0-9]{4}|[A-Z]{2}[0-9]{2}|[A-Z]{2} [0-9]{2}|[A-Z]{3}[0-9]{4}|[A-Z]{3}[0-9]{2}|[A-Z]{3} [0-9]{2}",
    "MU": r"^([0-9A-Z]\d{4})$",
    "MV": r"^\d{5}$",
    "MX": r"^\d{5}$",
    "MY": r"^\d{5}$",
    "MZ": r"^\d{4}$",
    "NC": r"^\d{5}$",
    "NE": r"^\d{4}$",
    "NF": r"^(2899)$",
    "NG": r"^\d{6}$",
    "NI": r"^\d{5}$",
    "NL": r"^[0-9]{4} [A-Z]{2}|[0-9]{4}[A-Z]{2}$",
    "NO": r"^\d{4}$",
    "NP": r"^\d{5}$",
    "NZ": r"^\d{4}$",
    "OM": r"^\d{3}$",
    "PE": r"^\d{5}$",
    "PF": r"^((987)\d{2})$",
    "PG": r"^\d{3}$",
    "PH": r"^\d{4}$",
    "PK": r"^\d{5}$",
    "PL": r"^[0-9]{2}[-]([0-9]){3}$",
    "PN": r"^(PCR9 1ZZ)$",
    "PS": r"^(\d{3}-\d{3})$",
    "PT": r"^\d{4}((-)\d{3})$",
    "PW": r"^(96939|96940)$",
    "PY": r"^\d{4}$",
    "RO": r"^\d{6}$",
    "RS": r"^\d{5}$",
    "RU": r"^\d{6}$",
    "SA": r"^\d{5}([\-]\d{4})?$",
    "SD": r"^\d{5}$",
    "SE": r"^(\d{3} \d{2})$",
    "SG": r"^\d{6}$",
    "SH": r"^(ASCN 1ZZ|TDCU 1ZZ|STHL 1ZZ)$",
    "SI": r"^\d{4}$",
    "SK": r"^(\d{3} \d{2})|\d{5}$",
    "SM": r"^(4789\d)$",
    "SN": r"^\d{5}$",
    "SS": r"^\d{5}$",
    "SV": r"^((CP) \d{4})$",
    "SZ": r"^([A-Z]\d{3})$",
    "TC": r"^(TKCA 1ZZ)$",
    "TF": r"^((984)\d{2})$",
    "TH": r"^\d{5}$",
    "TJ": r"^\d{3}$",
    "TM": r"^\d{6}$",
    "TN": r"^\d{4}$",
    "TR": r"^\d{5}$",
    "TW": r"^(\d{3}[-]\d{2})|(\d{3})$",
    "TZ": r"^\d{5}$",
    "UA": r"^\d{5}$",
    "US": r"^[0-9]{5}(?:-[0-9]{4})?$",
    "UY": r"^\d{5}$",
    "UZ": r"^\d{6}$",
    "VA": r"^(00120)$",
    "VC": r"^(VC)(\d{4})$",
    "VE": r"^\d{4}$",
    "VG": r"^(VG11)[0-6][0]$",
    "VI": r"^\d{5}$",
    "VN": r"^\d{6}$",
    "WF": r"^((986)\d{2})$",
    "WS": r"^(96799)$",
    "ZA": r"^\d{4}$",
    "ZM": r"^\d{5}$",
}
