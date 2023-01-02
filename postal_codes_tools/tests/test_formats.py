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
    assert verify_postal_code_format(country_iso_code="AD", postal_code="AD100") is True
    assert verify_postal_code_format(country_iso_code="AD", postal_code="AD123") is True
    assert verify_postal_code_format(country_iso_code="AF", postal_code="1057") is True
    assert verify_postal_code_format(country_iso_code="AG", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="AI", postal_code="AI-2640") is True
    assert verify_postal_code_format(country_iso_code="AL", postal_code="5300") is True
    assert verify_postal_code_format(country_iso_code="AM", postal_code="1234") is True
    assert verify_postal_code_format(country_iso_code="AM", postal_code="123456") is True
    assert verify_postal_code_format(country_iso_code="AQ", postal_code="7151") is True
    assert verify_postal_code_format(country_iso_code="AR", postal_code="G5861URB") is True
    assert verify_postal_code_format(country_iso_code="AR", postal_code="U5601") is True
    assert verify_postal_code_format(country_iso_code="AS", postal_code="96799") is True
    assert verify_postal_code_format(country_iso_code="AS", postal_code="96799-9999") is True
    assert verify_postal_code_format(country_iso_code="AT", postal_code="1010") is True
    assert verify_postal_code_format(country_iso_code="AU", postal_code="2599") is True
    assert verify_postal_code_format(country_iso_code="AZ", postal_code="AZ 1234") is True
    assert verify_postal_code_format(country_iso_code="AZ", postal_code="AZ1000") is True
    assert verify_postal_code_format(country_iso_code="BA", postal_code="71000") is True
    assert verify_postal_code_format(country_iso_code="BB", postal_code="BB12345") is True
    assert verify_postal_code_format(country_iso_code="BB", postal_code="BB15094") is True
    assert verify_postal_code_format(country_iso_code="BD", postal_code="1219") is True
    assert verify_postal_code_format(country_iso_code="BE", postal_code="1049") is True
    assert verify_postal_code_format(country_iso_code="BF", postal_code="99999") is True
    assert verify_postal_code_format(country_iso_code="BG", postal_code="1000") is True
    assert verify_postal_code_format(country_iso_code="BH", postal_code="123") is True
    assert verify_postal_code_format(country_iso_code="BH", postal_code="1234") is True
    assert verify_postal_code_format(country_iso_code="BM", postal_code="AB 12") is True
    assert verify_postal_code_format(country_iso_code="BN", postal_code="AB1234") is True
    assert verify_postal_code_format(country_iso_code="BR", postal_code="12345-123") is True
    assert verify_postal_code_format(country_iso_code="BT", postal_code="31002") is True
    assert verify_postal_code_format(country_iso_code="BY", postal_code="231300") is True
    assert verify_postal_code_format(country_iso_code="CA", postal_code="K1A 0T6") is True
    assert verify_postal_code_format(country_iso_code="CC", postal_code="6799") is True
    assert verify_postal_code_format(country_iso_code="CH", postal_code="8050") is True
    assert verify_postal_code_format(country_iso_code="CL", postal_code="1234567") is True
    assert verify_postal_code_format(country_iso_code="CN", postal_code="123456") is True
    assert verify_postal_code_format(country_iso_code="CO", postal_code="123456") is True
    assert verify_postal_code_format(country_iso_code="CR", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="CU", postal_code="CP10400") is True
    assert verify_postal_code_format(country_iso_code="CV", postal_code="1234") is True
    assert verify_postal_code_format(country_iso_code="CX", postal_code="6798") is True
    assert verify_postal_code_format(country_iso_code="CY", postal_code="4999") is True
    assert verify_postal_code_format(country_iso_code="CZ", postal_code="160 00") is True
    assert verify_postal_code_format(country_iso_code="CZ", postal_code="16000") is True
    assert verify_postal_code_format(country_iso_code="DE", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="DK", postal_code="1234") is True
    assert verify_postal_code_format(country_iso_code="DO", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="DZ", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="EC", postal_code="123456") is True
    assert verify_postal_code_format(country_iso_code="EE", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="EG", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="ES", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="ET", postal_code="1234") is True
    assert verify_postal_code_format(country_iso_code="FI", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="FK", postal_code="FIQQ 1ZZ") is True
    assert verify_postal_code_format(country_iso_code="FM", postal_code="96942") is True
    assert verify_postal_code_format(country_iso_code="FM", postal_code="96942-9999") is True
    assert verify_postal_code_format(country_iso_code="FO", postal_code="123") is True
    assert verify_postal_code_format(country_iso_code="FR", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="GB", postal_code="DT3 6GB") is True
    assert verify_postal_code_format(country_iso_code="GB", postal_code="L2 2DP") is True
    assert verify_postal_code_format(country_iso_code="GE", postal_code="1234") is True
    assert verify_postal_code_format(country_iso_code="GG", postal_code="GY1 2AX") is True
    assert verify_postal_code_format(country_iso_code="GG", postal_code="GYD3 4FY") is True
    assert verify_postal_code_format(country_iso_code="GG", postal_code="GYK60 2FE") is True
    assert verify_postal_code_format(country_iso_code="GI", postal_code="GX11 1AA") is True
    assert verify_postal_code_format(country_iso_code="GL", postal_code="3905") is True
    assert verify_postal_code_format(country_iso_code="GN", postal_code="123") is True
    assert verify_postal_code_format(country_iso_code="GR", postal_code="123 45") is True
    assert verify_postal_code_format(country_iso_code="GR", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="GS", postal_code="SIQQ 1ZZ") is True
    assert verify_postal_code_format(country_iso_code="GT", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="GU", postal_code="96911") is True
    assert verify_postal_code_format(country_iso_code="GU", postal_code="96911-9999") is True
    assert verify_postal_code_format(country_iso_code="GW", postal_code="1234") is True
    assert verify_postal_code_format(country_iso_code="HK", postal_code="999077") is True
    assert verify_postal_code_format(country_iso_code="HM", postal_code="7151") is True
    assert verify_postal_code_format(country_iso_code="HN", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="HR", postal_code="21000") is True
    assert verify_postal_code_format(country_iso_code="HT", postal_code="HT 1440") is True
    assert verify_postal_code_format(country_iso_code="HT", postal_code="HT1440") is True
    assert verify_postal_code_format(country_iso_code="HU", postal_code="2310") is True
    assert verify_postal_code_format(country_iso_code="ID", postal_code="15360") is True
    assert verify_postal_code_format(country_iso_code="IE", postal_code="D6W-5R40") is True
    assert verify_postal_code_format(country_iso_code="IE", postal_code="N52 7CHX") is True
    assert verify_postal_code_format(country_iso_code="IE", postal_code="P35A0DY") is True
    assert verify_postal_code_format(country_iso_code="IL", postal_code="1234567") is True
    assert verify_postal_code_format(country_iso_code="IM", postal_code="IM0") is True
    assert verify_postal_code_format(country_iso_code="IM", postal_code="IM56") is True
    assert verify_postal_code_format(country_iso_code="IM", postal_code="Y7W 7PF") is True
    assert verify_postal_code_format(country_iso_code="IN", postal_code="500012") is True
    assert verify_postal_code_format(country_iso_code="IO", postal_code="BB9D 1ZZ") is True
    assert verify_postal_code_format(country_iso_code="IQ", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="IR", postal_code="12345-12345") is True
    assert verify_postal_code_format(country_iso_code="IR", postal_code="1234512345") is True
    assert verify_postal_code_format(country_iso_code="IS", postal_code="101") is True
    assert verify_postal_code_format(country_iso_code="IT", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="JE", postal_code="JE0 0NX") is True
    assert verify_postal_code_format(country_iso_code="JM", postal_code="JMDQV43") is True
    assert verify_postal_code_format(country_iso_code="JO", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="JP", postal_code="123-1234") is True
    assert verify_postal_code_format(country_iso_code="KE", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="KG", postal_code="123456") is True
    assert verify_postal_code_format(country_iso_code="KH", postal_code="010102") is True
    assert verify_postal_code_format(country_iso_code="KH", postal_code="01501") is True
    assert verify_postal_code_format(country_iso_code="KH", postal_code="120209") is True
    assert verify_postal_code_format(country_iso_code="KI", postal_code="KI0107") is True
    assert verify_postal_code_format(country_iso_code="KN", postal_code="KN0101") is True
    assert verify_postal_code_format(country_iso_code="KN", postal_code="KN0801-0802") is True
    assert verify_postal_code_format(country_iso_code="KN", postal_code="KN0802") is True
    assert verify_postal_code_format(country_iso_code="KN", postal_code="KN0901-0902") is True
    assert verify_postal_code_format(country_iso_code="KR", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="KW", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="KY", postal_code="KY6-2299") is True
    assert verify_postal_code_format(country_iso_code="KZ", postal_code="010010") is True
    assert verify_postal_code_format(country_iso_code="KZ", postal_code="A10A5T4") is True
    assert verify_postal_code_format(country_iso_code="LA", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="LB", postal_code="1234 1234") is True
    assert verify_postal_code_format(country_iso_code="LB", postal_code="1234") is True
    assert verify_postal_code_format(country_iso_code="LC", postal_code="LC05 201") is True
    assert verify_postal_code_format(country_iso_code="LI", postal_code="1234") is True
    assert verify_postal_code_format(country_iso_code="LK", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="LR", postal_code="1234") is True
    assert verify_postal_code_format(country_iso_code="LS", postal_code="123") is True
    assert verify_postal_code_format(country_iso_code="LT", postal_code="01100") is True
    assert verify_postal_code_format(country_iso_code="LT", postal_code="LT-01100") is True
    assert verify_postal_code_format(country_iso_code="LU", postal_code="1019") is True
    assert verify_postal_code_format(country_iso_code="LU", postal_code="L-2530") is True
    assert verify_postal_code_format(country_iso_code="LV", postal_code="1010") is True
    assert verify_postal_code_format(country_iso_code="LV", postal_code="LV-1010") is True
    assert verify_postal_code_format(country_iso_code="MA", postal_code="20192") is True
    assert verify_postal_code_format(country_iso_code="MD", postal_code="2001") is True
    assert verify_postal_code_format(country_iso_code="MD", postal_code="MD-2001") is True
    assert verify_postal_code_format(country_iso_code="MD", postal_code="MD2001") is True
    assert verify_postal_code_format(country_iso_code="ME", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="MG", postal_code="123") is True
    assert verify_postal_code_format(country_iso_code="MH", postal_code="96960") is True
    assert verify_postal_code_format(country_iso_code="MH", postal_code="96960-9999") is True
    assert verify_postal_code_format(country_iso_code="MK", postal_code="1234") is True
    assert verify_postal_code_format(country_iso_code="MM", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="MN", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="MO", postal_code="999078") is True
    assert verify_postal_code_format(country_iso_code="MP", postal_code="96950") is True
    assert verify_postal_code_format(country_iso_code="MP", postal_code="96950-9999") is True
    assert verify_postal_code_format(country_iso_code="MS", postal_code="MSR1120") is True
    assert verify_postal_code_format(country_iso_code="MT", postal_code="BOR 9267") is True
    assert verify_postal_code_format(country_iso_code="MT", postal_code="NJ23") is True
    assert verify_postal_code_format(country_iso_code="MT", postal_code="WE 39") is True
    assert verify_postal_code_format(country_iso_code="MT", postal_code="XXQ01") is True
    assert verify_postal_code_format(country_iso_code="MU", postal_code="20101") is True
    assert verify_postal_code_format(country_iso_code="MU", postal_code="A0000") is True
    assert verify_postal_code_format(country_iso_code="MV", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="MW", postal_code="101100") is True
    assert verify_postal_code_format(country_iso_code="MW", postal_code="307100") is True
    assert verify_postal_code_format(country_iso_code="MX", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="MY", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="MZ", postal_code="1234") is True
    assert verify_postal_code_format(country_iso_code="NA", postal_code="10003") is True
    assert verify_postal_code_format(country_iso_code="NC", postal_code="98814") is True
    assert verify_postal_code_format(country_iso_code="NE", postal_code="1234") is True
    assert verify_postal_code_format(country_iso_code="NF", postal_code="2899") is True
    assert verify_postal_code_format(country_iso_code="NG", postal_code="100001") is True
    assert verify_postal_code_format(country_iso_code="NI", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="NL", postal_code="1011 AC") is True
    assert verify_postal_code_format(country_iso_code="NL", postal_code="1011AC") is True
    assert verify_postal_code_format(country_iso_code="NO", postal_code="1234") is True
    assert verify_postal_code_format(country_iso_code="NP", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="NR", postal_code="NRU68") is True
    assert verify_postal_code_format(country_iso_code="NU", postal_code="9974") is True
    assert verify_postal_code_format(country_iso_code="NZ", postal_code="1234") is True
    assert verify_postal_code_format(country_iso_code="OM", postal_code="123") is True
    assert verify_postal_code_format(country_iso_code="PA", postal_code="0601") is True
    assert verify_postal_code_format(country_iso_code="PA", postal_code="1001") is True
    assert verify_postal_code_format(country_iso_code="PE", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="PF", postal_code="98712") is True
    assert verify_postal_code_format(country_iso_code="PG", postal_code="123") is True
    assert verify_postal_code_format(country_iso_code="PH", postal_code="1234") is True
    assert verify_postal_code_format(country_iso_code="PK", postal_code="75600") is True
    assert verify_postal_code_format(country_iso_code="PL", postal_code="12-123") is True
    assert verify_postal_code_format(country_iso_code="PN", postal_code="PCR9 1ZZ") is True
    assert verify_postal_code_format(country_iso_code="PS", postal_code="600-699") is True
    assert verify_postal_code_format(country_iso_code="PS", postal_code="P3600700") is True
    assert verify_postal_code_format(country_iso_code="PT", postal_code="1000-260") is True
    assert verify_postal_code_format(country_iso_code="PW", postal_code="96939") is True
    assert verify_postal_code_format(country_iso_code="PW", postal_code="96940") is True
    assert verify_postal_code_format(country_iso_code="PY", postal_code="1234") is True
    assert verify_postal_code_format(country_iso_code="RO", postal_code="123456") is True
    assert verify_postal_code_format(country_iso_code="RS", postal_code="24430") is True
    assert verify_postal_code_format(country_iso_code="RS", postal_code="456769") is True
    assert verify_postal_code_format(country_iso_code="RU", postal_code="123456") is True
    assert verify_postal_code_format(country_iso_code="SA", postal_code="11564") is True
    assert verify_postal_code_format(country_iso_code="SA", postal_code="75311-8538") is True
    assert verify_postal_code_format(country_iso_code="SD", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="SE", postal_code="113 51") is True
    assert verify_postal_code_format(country_iso_code="SG", postal_code="123456") is True
    assert verify_postal_code_format(country_iso_code="SH", postal_code="ASCN 1ZZ") is True
    assert verify_postal_code_format(country_iso_code="SH", postal_code="STHL 1ZZ") is True
    assert verify_postal_code_format(country_iso_code="SH", postal_code="TDCU 1ZZ") is True
    assert verify_postal_code_format(country_iso_code="SI", postal_code="8341") is True
    assert verify_postal_code_format(country_iso_code="SK", postal_code="123 45") is True
    assert verify_postal_code_format(country_iso_code="SK", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="SM", postal_code="47892") is True
    assert verify_postal_code_format(country_iso_code="SN", postal_code="10200") is True
    assert verify_postal_code_format(country_iso_code="SS", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="SV", postal_code="1201") is True
    assert verify_postal_code_format(country_iso_code="SZ", postal_code="A123") is True
    assert verify_postal_code_format(country_iso_code="TC", postal_code="TKCA 1ZZ") is True
    assert verify_postal_code_format(country_iso_code="TF", postal_code="98412") is True
    assert verify_postal_code_format(country_iso_code="TH", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="TJ", postal_code="799999") is True
    assert verify_postal_code_format(country_iso_code="TM", postal_code="745180") is True
    assert verify_postal_code_format(country_iso_code="TN", postal_code="1234") is True
    assert verify_postal_code_format(country_iso_code="TR", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="TT", postal_code="120110") is True
    assert verify_postal_code_format(country_iso_code="TW", postal_code="237-01") is True
    assert verify_postal_code_format(country_iso_code="TW", postal_code="407") is True
    assert verify_postal_code_format(country_iso_code="TW", postal_code="999-999") is True
    assert verify_postal_code_format(country_iso_code="TW", postal_code="999999") is True
    assert verify_postal_code_format(country_iso_code="TZ", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="UA", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="US", postal_code="00716") is True
    assert verify_postal_code_format(country_iso_code="US", postal_code="00716-9999") is True
    assert verify_postal_code_format(country_iso_code="US", postal_code="11550") is True
    assert verify_postal_code_format(country_iso_code="US", postal_code="11550-9999") is True
    assert verify_postal_code_format(country_iso_code="UY", postal_code="11700") is True
    assert verify_postal_code_format(country_iso_code="UZ", postal_code="123456") is True
    assert verify_postal_code_format(country_iso_code="VA", postal_code="00120") is True
    assert verify_postal_code_format(country_iso_code="VC", postal_code="VC1234") is True
    assert verify_postal_code_format(country_iso_code="VE", postal_code="1061") is True
    assert verify_postal_code_format(country_iso_code="VG", postal_code="VG1110") is True
    assert verify_postal_code_format(country_iso_code="VI", postal_code="00850") is True
    assert verify_postal_code_format(country_iso_code="VI", postal_code="00850-9999") is True
    assert verify_postal_code_format(country_iso_code="VN", postal_code="123456") is True
    assert verify_postal_code_format(country_iso_code="WF", postal_code="98600") is True
    assert verify_postal_code_format(country_iso_code="WS", postal_code="WS1382") is True
    assert verify_postal_code_format(country_iso_code="ZA", postal_code="1234") is True
    assert verify_postal_code_format(country_iso_code="ZM", postal_code="12345") is True
    # Aland Islands (Finland system)
    assert verify_postal_code_format(country_iso_code="AX", postal_code="12345") is True
    # french territories
    assert verify_postal_code_format(country_iso_code="BL", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="GF", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="GP", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="MC", postal_code="12345") is True  # Monaco (98000)
    assert verify_postal_code_format(country_iso_code="MF", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="MQ", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="PM", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="RE", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="YT", postal_code="12345") is True
    # end of french territories
    # Western Sahara (Morocco system)
    assert verify_postal_code_format(country_iso_code="EH", postal_code="12345") is True
    # Puerto Rico (US system)
    assert verify_postal_code_format(country_iso_code="PR", postal_code="12345") is True
    assert verify_postal_code_format(country_iso_code="PR", postal_code="12345-1234") is True
    # Svaldbard and Jan Mayen (Norway system)
    assert verify_postal_code_format(country_iso_code="SJ", postal_code="1234") is True


def test_countries_without_postal_code():
    assert country_without_postal_code("AE") is True
    assert country_without_postal_code("AO") is True
    assert country_without_postal_code("AW") is True
    assert country_without_postal_code("BI") is True
    assert country_without_postal_code("BJ") is True
    assert country_without_postal_code("BO") is True
    assert country_without_postal_code("BQ") is True
    assert country_without_postal_code("BS") is True
    assert country_without_postal_code("BV") is True
    assert country_without_postal_code("BW") is True
    assert country_without_postal_code("BZ") is True
    assert country_without_postal_code("CD") is True
    assert country_without_postal_code("CF") is True
    assert country_without_postal_code("CG") is True
    assert country_without_postal_code("CI") is True
    assert country_without_postal_code("CK") is True
    assert country_without_postal_code("CM") is True
    assert country_without_postal_code("CW") is True
    assert country_without_postal_code("DJ") is True
    assert country_without_postal_code("DM") is True
    assert country_without_postal_code("ER") is True
    assert country_without_postal_code("FJ") is True
    assert country_without_postal_code("GA") is True
    assert country_without_postal_code("GD") is True
    assert country_without_postal_code("GH") is True
    assert country_without_postal_code("GM") is True
    assert country_without_postal_code("GQ") is True
    assert country_without_postal_code("GY") is True
    assert country_without_postal_code("KI") is True
    assert country_without_postal_code("KM") is True
    assert country_without_postal_code("KP") is True
    assert country_without_postal_code("ML") is True
    assert country_without_postal_code("MR") is True
    assert country_without_postal_code("QA") is True
    assert country_without_postal_code("RW") is True
    assert country_without_postal_code("SB") is True
    assert country_without_postal_code("SC") is True
    assert country_without_postal_code("SL") is True
    assert country_without_postal_code("SR") is True
    assert country_without_postal_code("ST") is True
    assert country_without_postal_code("SX") is True
    assert country_without_postal_code("SY") is True
    assert country_without_postal_code("TD") is True
    assert country_without_postal_code("TG") is True
    assert country_without_postal_code("TK") is True
    assert country_without_postal_code("TL") is True
    assert country_without_postal_code("TO") is True
    assert country_without_postal_code("TV") is True
    assert country_without_postal_code("UG") is True
    assert country_without_postal_code("UM") is True
    assert country_without_postal_code("VU") is True
    assert country_without_postal_code("XX") is True
    assert country_without_postal_code("YE") is True
    assert country_without_postal_code("ZW") is True
