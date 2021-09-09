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

    assert verify_postal_code_format(postal_code=None, country_iso_code="TC") is False

    assert country_without_postal_code("TC") is False
    assert has_postal_code("TC") is True


def test_verify_postal_code_for_countries_without_postal_code():
    assert country_without_postal_code("AO") is True
    assert country_without_postal_code("DE") is False

    assert has_postal_code("AO") is False

    with pytest.raises(KeyError):
        verify_postal_code_format(postal_code="", country_iso_code="AO")
    with pytest.raises(KeyError):
        assert verify_postal_code_format(postal_code="ASFAFS", country_iso_code="AO")


def test_verify_postal_code_for_unknown_countries():
    with pytest.raises(KeyError):
        assert verify_postal_code_format(postal_code="12345", country_iso_code="KK")
    with pytest.raises(KeyError):
        assert verify_postal_code_format(postal_code="", country_iso_code="KK")

    assert country_without_postal_code("KK") is False
    assert has_postal_code("KK") is False


def test_countries_with_postal_code():
    assert verify_postal_code_format(postal_code="AD123", country_iso_code="AD") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="AF") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="AG") is True
    assert verify_postal_code_format(postal_code="AI-2640", country_iso_code="AI") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="AL") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="AM") is True
    assert verify_postal_code_format(postal_code="123456", country_iso_code="AM") is True
    assert verify_postal_code_format(postal_code="7151", country_iso_code="AQ") is True
    assert verify_postal_code_format(postal_code="U5601", country_iso_code="AR") is True
    assert verify_postal_code_format(postal_code="G5861URB", country_iso_code="AR") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="AS") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="AT") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="AU") is True
    assert verify_postal_code_format(postal_code="AZ 1234", country_iso_code="AZ") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="BA") is True
    assert verify_postal_code_format(postal_code="BB12345", country_iso_code="BB") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="BD") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="BE") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="BG") is True
    assert verify_postal_code_format(postal_code="123", country_iso_code="BH") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="BH") is True
    assert verify_postal_code_format(postal_code="AB 12", country_iso_code="BM") is True
    assert verify_postal_code_format(postal_code="AB1234", country_iso_code="BN") is True
    assert verify_postal_code_format(postal_code="12345-123", country_iso_code="BR") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="BT") is True
    assert verify_postal_code_format(postal_code="123456", country_iso_code="BY") is True
    assert verify_postal_code_format(postal_code="C7R4R4", country_iso_code="CA") is True
    assert verify_postal_code_format(postal_code="Y8H 9K2", country_iso_code="CA") is True
    assert verify_postal_code_format(postal_code="Y6W-2N7", country_iso_code="CA") is True
    assert verify_postal_code_format(postal_code="6799", country_iso_code="CC") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="CH") is True
    assert verify_postal_code_format(postal_code="1234567", country_iso_code="CL") is True
    assert verify_postal_code_format(postal_code="123456", country_iso_code="CN") is True
    assert verify_postal_code_format(postal_code="123456", country_iso_code="CO") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="CR") is True
    assert verify_postal_code_format(postal_code="CP12345", country_iso_code="CU") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="CV") is True
    assert verify_postal_code_format(postal_code="6798", country_iso_code="CX") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="CY") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="CZ") is True
    assert verify_postal_code_format(postal_code="123 45", country_iso_code="CZ") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="DE") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="DK") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="DO") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="DZ") is True
    assert verify_postal_code_format(postal_code="123456", country_iso_code="EC") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="EE") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="EG") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="ES") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="ET") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="FI") is True
    assert verify_postal_code_format(postal_code="FIQQ 1ZZ", country_iso_code="FK") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="FM") is True
    assert verify_postal_code_format(postal_code="123", country_iso_code="FO") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="FR") is True
    assert verify_postal_code_format(postal_code="I48 0Fh", country_iso_code="GB") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="GE") is True
    assert verify_postal_code_format(postal_code="GY1 2AX", country_iso_code="GG") is True
    assert verify_postal_code_format(postal_code="GYD3 4FY", country_iso_code="GG") is True
    assert verify_postal_code_format(postal_code="GYK60 2FE", country_iso_code="GG") is True
    assert verify_postal_code_format(postal_code="GX11 1AA", country_iso_code="GI") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="GL") is True
    assert verify_postal_code_format(postal_code="123", country_iso_code="GN") is True
    assert verify_postal_code_format(postal_code="123 45", country_iso_code="GR") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="GR") is True
    assert verify_postal_code_format(postal_code="SIQQ 1ZZ", country_iso_code="GS") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="GT") is True
    assert verify_postal_code_format(postal_code="96912", country_iso_code="GU") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="GW") is True
    assert verify_postal_code_format(postal_code="999077", country_iso_code="HK") is True
    assert verify_postal_code_format(postal_code="7151", country_iso_code="HM") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="HN") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="HR") is True
    assert verify_postal_code_format(postal_code="HT9440", country_iso_code="HT") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="HU") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="ID") is True
    assert verify_postal_code_format(postal_code="D6W-5R40", country_iso_code="IE") is True
    assert verify_postal_code_format(postal_code="P35A0DY", country_iso_code="IE") is True
    assert verify_postal_code_format(postal_code="N52 7CHX", country_iso_code="IE") is True
    assert verify_postal_code_format(postal_code="1234567", country_iso_code="IL") is True
    assert verify_postal_code_format(postal_code="Y7W 7PF", country_iso_code="IM") is True
    assert verify_postal_code_format(postal_code="IM0", country_iso_code="IM") is True
    assert verify_postal_code_format(postal_code="IM56", country_iso_code="IM") is True
    assert verify_postal_code_format(postal_code="123456", country_iso_code="IN") is True
    assert verify_postal_code_format(postal_code="BB9D 1ZZ", country_iso_code="IO") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="IQ") is True
    assert verify_postal_code_format(postal_code="1234512345", country_iso_code="IR") is True
    assert verify_postal_code_format(postal_code="12345-12345", country_iso_code="IR") is True
    assert verify_postal_code_format(postal_code="123", country_iso_code="IS") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="IT") is True
    assert verify_postal_code_format(postal_code="JE0 0NX", country_iso_code="JE") is True
    assert verify_postal_code_format(postal_code="JMDQV43", country_iso_code="JM") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="JO") is True
    assert verify_postal_code_format(postal_code="123-1234", country_iso_code="JP") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="KE") is True
    assert verify_postal_code_format(postal_code="123456", country_iso_code="KG") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="KH") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="KR") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="KW") is True
    assert verify_postal_code_format(postal_code="KY6-2299", country_iso_code="KY") is True
    assert verify_postal_code_format(postal_code="123456", country_iso_code="KZ") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="LA") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="LB") is True
    assert verify_postal_code_format(postal_code="1234 1234", country_iso_code="LB") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="LI") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="LK") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="LR") is True
    assert verify_postal_code_format(postal_code="123", country_iso_code="LS") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="LT") is True
    assert verify_postal_code_format(postal_code="LT-12345", country_iso_code="LT") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="LU") is True
    assert verify_postal_code_format(postal_code="L-1234", country_iso_code="LU") is True
    assert verify_postal_code_format(postal_code="LV-1234", country_iso_code="LV") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="MA") is True
    assert verify_postal_code_format(postal_code="MD-1234", country_iso_code="MD") is True
    assert verify_postal_code_format(postal_code="MD1234", country_iso_code="MD") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="ME") is True
    assert verify_postal_code_format(postal_code="123", country_iso_code="MG") is True
    assert verify_postal_code_format(postal_code="96969", country_iso_code="MH") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="MK") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="MM") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="MN") is True
    assert verify_postal_code_format(postal_code="999078", country_iso_code="MO") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="MP") is True
    assert verify_postal_code_format(postal_code="MSR 1234", country_iso_code="MS") is True
    assert verify_postal_code_format(postal_code="BOR 9267", country_iso_code="MT") is True
    assert verify_postal_code_format(postal_code="WE 39", country_iso_code="MT") is True
    assert verify_postal_code_format(postal_code="NJ23", country_iso_code="MT") is True
    assert verify_postal_code_format(postal_code="XXQ01", country_iso_code="MT") is True
    assert verify_postal_code_format(postal_code="V8959", country_iso_code="MU") is True
    assert verify_postal_code_format(postal_code="79621", country_iso_code="MU") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="MV") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="MX") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="MY") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="MZ") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="NC") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="NE") is True
    assert verify_postal_code_format(postal_code="2899", country_iso_code="NF") is True
    assert verify_postal_code_format(postal_code="123456", country_iso_code="NG") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="NI") is True
    assert verify_postal_code_format(postal_code="1234AB", country_iso_code="NL") is True
    assert verify_postal_code_format(postal_code="1234 AB", country_iso_code="NL") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="NO") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="NP") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="NZ") is True
    assert verify_postal_code_format(postal_code="123", country_iso_code="OM") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="PE") is True
    assert verify_postal_code_format(postal_code="98712", country_iso_code="PF") is True
    assert verify_postal_code_format(postal_code="123", country_iso_code="PG") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="PH") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="PK") is True
    assert verify_postal_code_format(postal_code="12-123", country_iso_code="PL") is True
    assert verify_postal_code_format(postal_code="PCR9 1ZZ", country_iso_code="PN") is True
    assert verify_postal_code_format(postal_code="123-123", country_iso_code="PS") is True
    assert verify_postal_code_format(postal_code="1234-123", country_iso_code="PT") is True
    assert verify_postal_code_format(postal_code="96939", country_iso_code="PW") is True
    assert verify_postal_code_format(postal_code="96940", country_iso_code="PW") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="PY") is True
    assert verify_postal_code_format(postal_code="123456", country_iso_code="RO") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="RS") is True
    assert verify_postal_code_format(postal_code="123456", country_iso_code="RU") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="SA") is True
    assert verify_postal_code_format(postal_code="12345-1234", country_iso_code="SA") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="SD") is True
    assert verify_postal_code_format(postal_code="123 45", country_iso_code="SE") is True
    assert verify_postal_code_format(postal_code="123456", country_iso_code="SG") is True
    assert verify_postal_code_format(postal_code="ASCN 1ZZ", country_iso_code="SH") is True
    assert verify_postal_code_format(postal_code="TDCU 1ZZ", country_iso_code="SH") is True
    assert verify_postal_code_format(postal_code="STHL 1ZZ", country_iso_code="SH") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="SI") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="SK") is True
    assert verify_postal_code_format(postal_code="123 45", country_iso_code="SK") is True
    assert verify_postal_code_format(postal_code="47892", country_iso_code="SM") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="SN") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="SS") is True
    assert verify_postal_code_format(postal_code="CP 1234", country_iso_code="SV") is True
    assert verify_postal_code_format(postal_code="A123", country_iso_code="SZ") is True
    assert verify_postal_code_format(postal_code="TKCA 1ZZ", country_iso_code="TC") is True
    assert verify_postal_code_format(postal_code="98412", country_iso_code="TF") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="TH") is True
    assert verify_postal_code_format(postal_code="123", country_iso_code="TJ") is True
    assert verify_postal_code_format(postal_code="123456", country_iso_code="TM") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="TN") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="TR") is True
    assert verify_postal_code_format(postal_code="123", country_iso_code="TW") is True
    assert verify_postal_code_format(postal_code="123-45", country_iso_code="TW") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="TZ") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="UA") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="US") is True
    assert verify_postal_code_format(postal_code="12345-1234", country_iso_code="US") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="UY") is True
    assert verify_postal_code_format(postal_code="123456", country_iso_code="UZ") is True
    assert verify_postal_code_format(postal_code="00120", country_iso_code="VA") is True
    assert verify_postal_code_format(postal_code="VC1234", country_iso_code="VC") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="VE") is True
    assert verify_postal_code_format(postal_code="VG1110", country_iso_code="VG") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="VI") is True
    assert verify_postal_code_format(postal_code="123456", country_iso_code="VN") is True
    assert verify_postal_code_format(postal_code="98612", country_iso_code="WF") is True
    assert verify_postal_code_format(postal_code="96799", country_iso_code="WS") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="ZA") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="ZM") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="GF") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="GP") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="MQ") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="YT") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="RE") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="BL") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="MF") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="PM") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="MC") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="PR") is True
    assert verify_postal_code_format(postal_code="12345-1234", country_iso_code="PR") is True
    assert verify_postal_code_format(postal_code="1234", country_iso_code="SJ") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="EH") is True
    assert verify_postal_code_format(postal_code="12345", country_iso_code="AX") is True


def test_countries_without_postal_code():
    assert country_without_postal_code("ML") is True
    assert country_without_postal_code("GH") is True
    assert country_without_postal_code("TL") is True
    assert country_without_postal_code("BS") is True
    assert country_without_postal_code("LY") is True
    assert country_without_postal_code("YE") is True
    assert country_without_postal_code("BF") is True
    assert country_without_postal_code("TT") is True
    assert country_without_postal_code("TV") is True
    assert country_without_postal_code("MW") is True
    assert country_without_postal_code("GD") is True
    assert country_without_postal_code("UM") is True
    assert country_without_postal_code("KM") is True
    assert country_without_postal_code("TG") is True
    assert country_without_postal_code("LC") is True
    assert country_without_postal_code("BJ") is True
    assert country_without_postal_code("DM") is True
    assert country_without_postal_code("RW") is True
    assert country_without_postal_code("MR") is True
    assert country_without_postal_code("QA") is True
    assert country_without_postal_code("BW") is True
    assert country_without_postal_code("ER") is True
    assert country_without_postal_code("ST") is True
    assert country_without_postal_code("KP") is True
    assert country_without_postal_code("NA") is True
    assert country_without_postal_code("BV") is True
    assert country_without_postal_code("SR") is True
    assert country_without_postal_code("KN") is True
    assert country_without_postal_code("VU") is True
    assert country_without_postal_code("BZ") is True
    assert country_without_postal_code("DJ") is True
    assert country_without_postal_code("CK") is True
    assert country_without_postal_code("BQ") is True
    assert country_without_postal_code("BI") is True
    assert country_without_postal_code("AE") is True
    assert country_without_postal_code("SL") is True
    assert country_without_postal_code("SO") is True
    assert country_without_postal_code("CD") is True
    assert country_without_postal_code("SY") is True
    assert country_without_postal_code("PA") is True
    assert country_without_postal_code("XX") is True
    assert country_without_postal_code("AW") is True
    assert country_without_postal_code("CI") is True
    assert country_without_postal_code("CF") is True
    assert country_without_postal_code("GA") is True
    assert country_without_postal_code("GY") is True
    assert country_without_postal_code("SC") is True
    assert country_without_postal_code("AO") is True
    assert country_without_postal_code("BO") is True
    assert country_without_postal_code("TO") is True
    assert country_without_postal_code("CM") is True
    assert country_without_postal_code("KI") is True
    assert country_without_postal_code("CG") is True
    assert country_without_postal_code("SX") is True
    assert country_without_postal_code("TD") is True
    assert country_without_postal_code("FJ") is True
    assert country_without_postal_code("GM") is True
    assert country_without_postal_code("UG") is True
    assert country_without_postal_code("NU") is True
    assert country_without_postal_code("SB") is True
    assert country_without_postal_code("TK") is True
    assert country_without_postal_code("NR") is True
    assert country_without_postal_code("GQ") is True
    assert country_without_postal_code("CW") is True
    assert country_without_postal_code("ZW") is True
