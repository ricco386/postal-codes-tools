import pytest

from postal_codes_tools.postal_codes import (
    verify_postal_code_format,
    country_without_postal_code,
    has_postal_code,
    get_countries_without_postal_code,
    get_postal_code_regex,
)


def test_verify_postal_code_formats():
    # Samples from European Central Bank spreadsheet
    assert verify_postal_code_format(postal_code="12345", country_iso2="DE") is True
    assert verify_postal_code_format(postal_code="123", country_iso2="DE") is False

    assert verify_postal_code_format(postal_code="AD123", country_iso2="AD") is True
    assert verify_postal_code_format(postal_code="AD1234", country_iso2="AD") is False
    assert verify_postal_code_format(postal_code="AD12", country_iso2="AD") is False
    assert verify_postal_code_format(postal_code="12345", country_iso2="AD") is False


def test_check_country_which_has_postal_code():
    assert verify_postal_code_format(postal_code="TKCA 1ZZ", country_iso2="TC") is True
    assert verify_postal_code_format(postal_code="TKCA1ZZ", country_iso2="TC") is False
    assert verify_postal_code_format(postal_code="1234", country_iso2="TC") is False
    assert verify_postal_code_format(postal_code="", country_iso2="TC") is False
    assert verify_postal_code_format(postal_code=None, country_iso2="TC") is False

    assert country_without_postal_code("TC") is False
    assert has_postal_code("TC") is True


def test_verify_postal_code_for_countries_without_postal_code():
    assert country_without_postal_code("AO") is True
    assert country_without_postal_code("DE") is False

    assert has_postal_code("AO") is False

    with pytest.raises(KeyError):
        verify_postal_code_format(postal_code="", country_iso2="AO")
    with pytest.raises(KeyError):
        assert verify_postal_code_format(postal_code="ASFAFS", country_iso2="AO")


def test_verify_postal_code_for_unknown_countries():
    with pytest.raises(KeyError):
        assert verify_postal_code_format(postal_code="12345", country_iso2="KK")
    with pytest.raises(KeyError):
        assert verify_postal_code_format(postal_code="", country_iso2="KK")

    assert country_without_postal_code("KK") is False
    assert has_postal_code("KK") is False


def test_countries_with_postal_code():
    assert verify_postal_code_format(country_iso2="AD", postal_code="AD100") is True
    assert verify_postal_code_format(country_iso2="AF", postal_code="1057") is True
    assert verify_postal_code_format(country_iso2="AG", postal_code="33901") is True
    assert verify_postal_code_format(country_iso2="AI", postal_code="AI-2640") is True
    assert verify_postal_code_format(country_iso2="AL", postal_code="5300") is True
    assert verify_postal_code_format(country_iso2="AM", postal_code="0010") is True
    assert verify_postal_code_format(country_iso2="AM", postal_code="001011") is True
    assert verify_postal_code_format(country_iso2="AQ", postal_code="7151") is True
    assert verify_postal_code_format(country_iso2="AR", postal_code="G5861URB") is True
    assert verify_postal_code_format(country_iso2="AR", postal_code="U5601") is True
    assert verify_postal_code_format(country_iso2="AS", postal_code="96799") is True
    assert verify_postal_code_format(country_iso2="AS", postal_code="96799-9999") is True
    assert verify_postal_code_format(country_iso2="AT", postal_code="1010") is True
    assert verify_postal_code_format(country_iso2="AU", postal_code="2599") is True
    assert verify_postal_code_format(country_iso2="AZ", postal_code="AZ 1234") is True
    assert verify_postal_code_format(country_iso2="AZ", postal_code="AZ1000") is True
    assert verify_postal_code_format(country_iso2="BA", postal_code="71000") is True
    assert verify_postal_code_format(country_iso2="BB", postal_code="BB12345") is True
    assert verify_postal_code_format(country_iso2="BB", postal_code="BB15094") is True
    assert verify_postal_code_format(country_iso2="BD", postal_code="1219") is True
    assert verify_postal_code_format(country_iso2="BE", postal_code="1049") is True
    assert verify_postal_code_format(country_iso2="BF", postal_code="99999") is True
    assert verify_postal_code_format(country_iso2="BG", postal_code="1000") is True
    assert verify_postal_code_format(country_iso2="BH", postal_code="317") is True
    assert verify_postal_code_format(country_iso2="BH", postal_code="1216") is True
    assert verify_postal_code_format(country_iso2="BM", postal_code="CR 03") is True
    assert verify_postal_code_format(country_iso2="BN", postal_code="KB2333") is True
    assert verify_postal_code_format(country_iso2="BR", postal_code="28999-999") is True
    assert verify_postal_code_format(country_iso2="BT", postal_code="31002") is True
    assert verify_postal_code_format(country_iso2="BY", postal_code="231300") is True
    assert verify_postal_code_format(country_iso2="CA", postal_code="K1A 0T6") is True
    assert verify_postal_code_format(country_iso2="CC", postal_code="6799") is True
    assert verify_postal_code_format(country_iso2="CH", postal_code="8050") is True
    assert verify_postal_code_format(country_iso2="CL", postal_code="9340000") is True
    assert verify_postal_code_format(country_iso2="CN", postal_code="710000") is True
    assert verify_postal_code_format(country_iso2="CO", postal_code="111121") is True
    assert verify_postal_code_format(country_iso2="CR", postal_code="10101") is True
    assert verify_postal_code_format(country_iso2="CU", postal_code="CP10400") is True
    assert verify_postal_code_format(country_iso2="CV", postal_code="5110") is True
    assert verify_postal_code_format(country_iso2="CX", postal_code="6798") is True
    assert verify_postal_code_format(country_iso2="CY", postal_code="4999") is True
    assert verify_postal_code_format(country_iso2="CZ", postal_code="160 00") is True
    assert verify_postal_code_format(country_iso2="CZ", postal_code="16000") is True
    assert verify_postal_code_format(country_iso2="DE", postal_code="60320") is True
    assert verify_postal_code_format(country_iso2="DK", postal_code="2000") is True
    assert verify_postal_code_format(country_iso2="DO", postal_code="10103") is True
    assert verify_postal_code_format(country_iso2="DZ", postal_code="16000") is True
    assert verify_postal_code_format(country_iso2="EC", postal_code="170515") is True
    assert verify_postal_code_format(country_iso2="EE", postal_code="10111") is True
    assert verify_postal_code_format(country_iso2="EG", postal_code="12411") is True
    assert verify_postal_code_format(country_iso2="ES", postal_code="28006") is True
    assert verify_postal_code_format(country_iso2="ET", postal_code="3020") is True
    assert verify_postal_code_format(country_iso2="FI", postal_code="00180") is True
    assert verify_postal_code_format(country_iso2="FK", postal_code="FIQQ 1ZZ") is True
    assert verify_postal_code_format(country_iso2="FM", postal_code="96942") is True
    assert verify_postal_code_format(country_iso2="FM", postal_code="96942-9999") is True
    assert verify_postal_code_format(country_iso2="FO", postal_code="927") is True
    assert verify_postal_code_format(country_iso2="FR", postal_code="75008") is True
    assert verify_postal_code_format(country_iso2="GB", postal_code="DT3 6GB") is True
    assert verify_postal_code_format(country_iso2="GB", postal_code="L2 2DP") is True
    assert verify_postal_code_format(country_iso2="GE", postal_code="1234") is True
    assert verify_postal_code_format(country_iso2="GG", postal_code="GY1 2AX") is True
    assert verify_postal_code_format(country_iso2="GG", postal_code="GYD3 4FY") is True
    assert verify_postal_code_format(country_iso2="GG", postal_code="GYK60 2FE") is True
    assert verify_postal_code_format(country_iso2="GI", postal_code="GX11 1AA") is True
    assert verify_postal_code_format(country_iso2="GL", postal_code="3905") is True
    assert verify_postal_code_format(country_iso2="GN", postal_code="001") is True
    assert verify_postal_code_format(country_iso2="GR", postal_code="241 00") is True
    assert verify_postal_code_format(country_iso2="GR", postal_code="24100") is True
    assert verify_postal_code_format(country_iso2="GS", postal_code="SIQQ 1ZZ") is True
    assert verify_postal_code_format(country_iso2="GT", postal_code="01002") is True
    assert verify_postal_code_format(country_iso2="GU", postal_code="96911") is True
    assert verify_postal_code_format(country_iso2="GU", postal_code="96911-9999") is True
    assert verify_postal_code_format(country_iso2="GW", postal_code="1000") is True
    assert verify_postal_code_format(country_iso2="HK", postal_code="999077") is True
    assert verify_postal_code_format(country_iso2="HM", postal_code="7151") is True
    assert verify_postal_code_format(country_iso2="HN", postal_code="34101") is True
    assert verify_postal_code_format(country_iso2="HR", postal_code="21000") is True
    assert verify_postal_code_format(country_iso2="HT", postal_code="HT 1440") is True
    assert verify_postal_code_format(country_iso2="HT", postal_code="HT1440") is True
    assert verify_postal_code_format(country_iso2="HU", postal_code="2310") is True
    assert verify_postal_code_format(country_iso2="ID", postal_code="15360") is True
    assert verify_postal_code_format(country_iso2="IE", postal_code="D6W-5R40") is True
    assert verify_postal_code_format(country_iso2="IE", postal_code="D02 AF30") is True
    assert verify_postal_code_format(country_iso2="IE", postal_code="P35A0DY") is True
    assert verify_postal_code_format(country_iso2="IL", postal_code="1029200") is True
    assert verify_postal_code_format(country_iso2="IM", postal_code="IM5 1JS") is True
    assert verify_postal_code_format(country_iso2="IN", postal_code="500012") is True
    assert verify_postal_code_format(country_iso2="IO", postal_code="BB9D 1ZZ") is True
    assert verify_postal_code_format(country_iso2="IQ", postal_code="58019") is True
    assert verify_postal_code_format(country_iso2="IR", postal_code="9187158198") is True
    assert verify_postal_code_format(country_iso2="IR", postal_code="15119-43943") is True
    assert verify_postal_code_format(country_iso2="IS", postal_code="101") is True
    assert verify_postal_code_format(country_iso2="IT", postal_code="36051") is True
    assert verify_postal_code_format(country_iso2="JE", postal_code="JE1 1AG") is True
    assert verify_postal_code_format(country_iso2="JM", postal_code="JMAAW19") is True
    assert verify_postal_code_format(country_iso2="JO", postal_code="11118") is True
    assert verify_postal_code_format(country_iso2="JP", postal_code="408-0307") is True
    assert verify_postal_code_format(country_iso2="KE", postal_code="40406") is True
    assert verify_postal_code_format(country_iso2="KG", postal_code="720020") is True
    assert verify_postal_code_format(country_iso2="KH", postal_code="010102") is True
    assert verify_postal_code_format(country_iso2="KH", postal_code="01501") is True
    assert verify_postal_code_format(country_iso2="KH", postal_code="120209") is True
    assert verify_postal_code_format(country_iso2="KI", postal_code="KI0107") is True
    assert verify_postal_code_format(country_iso2="KN", postal_code="KN0101") is True
    assert verify_postal_code_format(country_iso2="KN", postal_code="KN0801-0802") is True
    assert verify_postal_code_format(country_iso2="KN", postal_code="KN0802") is True
    assert verify_postal_code_format(country_iso2="KN", postal_code="KN0901-0902") is True
    assert verify_postal_code_format(country_iso2="KR", postal_code="11962") is True
    assert verify_postal_code_format(country_iso2="KW", postal_code="60000") is True
    assert verify_postal_code_format(country_iso2="KY", postal_code="KY6-2299") is True
    assert verify_postal_code_format(country_iso2="KZ", postal_code="010010") is True
    assert verify_postal_code_format(country_iso2="KZ", postal_code="A10A5T4") is True
    assert verify_postal_code_format(country_iso2="LA", postal_code="13000") is True
    assert verify_postal_code_format(country_iso2="LB", postal_code="2038 3054") is True
    assert verify_postal_code_format(country_iso2="LB", postal_code="1103") is True
    assert verify_postal_code_format(country_iso2="LC", postal_code="LC05 201") is True
    assert verify_postal_code_format(country_iso2="LI", postal_code="9490") is True
    assert verify_postal_code_format(country_iso2="LK", postal_code="80212") is True
    assert verify_postal_code_format(country_iso2="LR", postal_code="1000") is True
    assert verify_postal_code_format(country_iso2="LS", postal_code="100") is True
    assert verify_postal_code_format(country_iso2="LT", postal_code="01100") is True
    assert verify_postal_code_format(country_iso2="LT", postal_code="LT-01100") is True
    assert verify_postal_code_format(country_iso2="LU", postal_code="1019") is True
    assert verify_postal_code_format(country_iso2="LU", postal_code="L-2530") is True
    assert verify_postal_code_format(country_iso2="LV", postal_code="1010") is True
    assert verify_postal_code_format(country_iso2="LV", postal_code="LV-1010") is True
    assert verify_postal_code_format(country_iso2="LY", postal_code="13.05.312") is True
    assert verify_postal_code_format(country_iso2="MA", postal_code="20192") is True
    assert verify_postal_code_format(country_iso2="MD", postal_code="2001") is True
    assert verify_postal_code_format(country_iso2="MD", postal_code="MD-2001") is True
    assert verify_postal_code_format(country_iso2="MD", postal_code="MD2001") is True
    assert verify_postal_code_format(country_iso2="ME", postal_code="81250") is True
    assert verify_postal_code_format(country_iso2="MG", postal_code="101") is True
    assert verify_postal_code_format(country_iso2="MH", postal_code="96960") is True
    assert verify_postal_code_format(country_iso2="MH", postal_code="96960-9999") is True
    assert verify_postal_code_format(country_iso2="MK", postal_code="1045") is True
    assert verify_postal_code_format(country_iso2="MM", postal_code="11121") is True
    assert verify_postal_code_format(country_iso2="MN", postal_code="16080") is True
    assert verify_postal_code_format(country_iso2="MO", postal_code="999078") is True
    assert verify_postal_code_format(country_iso2="MP", postal_code="96950") is True
    assert verify_postal_code_format(country_iso2="MP", postal_code="96950-9999") is True
    assert verify_postal_code_format(country_iso2="MS", postal_code="MSR1120") is True
    assert verify_postal_code_format(country_iso2="MT", postal_code="BOR 9267") is True
    assert verify_postal_code_format(country_iso2="MT", postal_code="VLT 1117") is True
    assert verify_postal_code_format(country_iso2="MT", postal_code="BKR 01") is True
    assert verify_postal_code_format(country_iso2="MT", postal_code="QRM09") is True
    assert verify_postal_code_format(country_iso2="MT", postal_code="RBT1676") is True
    assert verify_postal_code_format(country_iso2="MT", postal_code="TP 01") is True
    assert verify_postal_code_format(country_iso2="MT", postal_code="TP01") is True
    assert verify_postal_code_format(country_iso2="MU", postal_code="20101") is True
    assert verify_postal_code_format(country_iso2="MU", postal_code="A0000") is True
    assert verify_postal_code_format(country_iso2="MV", postal_code="20195") is True
    assert verify_postal_code_format(country_iso2="MW", postal_code="101100") is True
    assert verify_postal_code_format(country_iso2="MW", postal_code="307100") is True
    assert verify_postal_code_format(country_iso2="MX", postal_code="97229") is True
    assert verify_postal_code_format(country_iso2="MY", postal_code="50050") is True
    assert verify_postal_code_format(country_iso2="MZ", postal_code="1104") is True
    assert verify_postal_code_format(country_iso2="NA", postal_code="10003") is True
    assert verify_postal_code_format(country_iso2="NC", postal_code="98814") is True
    assert verify_postal_code_format(country_iso2="NE", postal_code="8001") is True
    assert verify_postal_code_format(country_iso2="NF", postal_code="2899") is True
    assert verify_postal_code_format(country_iso2="NG", postal_code="100001") is True
    assert verify_postal_code_format(country_iso2="NI", postal_code="11001") is True
    assert verify_postal_code_format(country_iso2="NL", postal_code="1011 AC") is True
    assert verify_postal_code_format(country_iso2="NL", postal_code="1011AC") is True
    assert verify_postal_code_format(country_iso2="NO", postal_code="5262") is True
    assert verify_postal_code_format(country_iso2="NP", postal_code="44600") is True
    assert verify_postal_code_format(country_iso2="NR", postal_code="NRU68") is True
    assert verify_postal_code_format(country_iso2="NU", postal_code="9974") is True
    assert verify_postal_code_format(country_iso2="NZ", postal_code="8041") is True
    assert verify_postal_code_format(country_iso2="OM", postal_code="112") is True
    assert verify_postal_code_format(country_iso2="PA", postal_code="0601") is True
    assert verify_postal_code_format(country_iso2="PA", postal_code="1001") is True
    assert verify_postal_code_format(country_iso2="PE", postal_code="15001") is True
    assert verify_postal_code_format(country_iso2="PF", postal_code="98712") is True
    assert verify_postal_code_format(country_iso2="PG", postal_code="244") is True
    assert verify_postal_code_format(country_iso2="PH", postal_code="4104") is True
    assert verify_postal_code_format(country_iso2="PK", postal_code="75600") is True
    assert verify_postal_code_format(country_iso2="PL", postal_code="87-100") is True
    assert verify_postal_code_format(country_iso2="PN", postal_code="PCR9 1ZZ") is True
    assert verify_postal_code_format(country_iso2="PS", postal_code="600-699") is True
    assert verify_postal_code_format(country_iso2="PS", postal_code="P3600700") is True
    assert verify_postal_code_format(country_iso2="PT", postal_code="1000-260") is True
    assert verify_postal_code_format(country_iso2="PW", postal_code="96939") is True
    assert verify_postal_code_format(country_iso2="PW", postal_code="96940") is True
    assert verify_postal_code_format(country_iso2="PY", postal_code="3180") is True
    assert verify_postal_code_format(country_iso2="RO", postal_code="507085") is True
    assert verify_postal_code_format(country_iso2="RS", postal_code="24430") is True
    assert verify_postal_code_format(country_iso2="RS", postal_code="456769") is True
    assert verify_postal_code_format(country_iso2="RU", postal_code="385100") is True
    assert verify_postal_code_format(country_iso2="SA", postal_code="11564") is True
    assert verify_postal_code_format(country_iso2="SA", postal_code="75311-8538") is True
    assert verify_postal_code_format(country_iso2="SD", postal_code="13315") is True
    assert verify_postal_code_format(country_iso2="SE", postal_code="113 51") is True
    assert verify_postal_code_format(country_iso2="SG", postal_code="570150") is True
    assert verify_postal_code_format(country_iso2="SH", postal_code="ASCN 1ZZ") is True
    assert verify_postal_code_format(country_iso2="SH", postal_code="STHL 1ZZ") is True
    assert verify_postal_code_format(country_iso2="SH", postal_code="TDCU 1ZZ") is True
    assert verify_postal_code_format(country_iso2="SI", postal_code="8341") is True
    assert verify_postal_code_format(country_iso2="SK", postal_code="811 01") is True
    assert verify_postal_code_format(country_iso2="SK", postal_code="81101") is True
    assert verify_postal_code_format(country_iso2="SM", postal_code="47892") is True
    assert verify_postal_code_format(country_iso2="SN", postal_code="10200") is True
    assert verify_postal_code_format(country_iso2="SO", postal_code="JH 09010") is True
    assert verify_postal_code_format(country_iso2="SS", postal_code="11111") is True
    assert verify_postal_code_format(country_iso2="SV", postal_code="1201") is True
    assert verify_postal_code_format(country_iso2="SZ", postal_code="M201") is True
    assert verify_postal_code_format(country_iso2="TC", postal_code="TKCA 1ZZ") is True
    assert verify_postal_code_format(country_iso2="TF", postal_code="98413") is True
    assert verify_postal_code_format(country_iso2="TH", postal_code="10240") is True
    assert verify_postal_code_format(country_iso2="TJ", postal_code="799999") is True
    assert verify_postal_code_format(country_iso2="TM", postal_code="745180") is True
    assert verify_postal_code_format(country_iso2="TN", postal_code="3200") is True
    assert verify_postal_code_format(country_iso2="TR", postal_code="34000") is True
    assert verify_postal_code_format(country_iso2="TT", postal_code="120110") is True
    assert verify_postal_code_format(country_iso2="TW", postal_code="237-01") is True
    assert verify_postal_code_format(country_iso2="TW", postal_code="407") is True
    assert verify_postal_code_format(country_iso2="TW", postal_code="999-999") is True
    assert verify_postal_code_format(country_iso2="TW", postal_code="999999") is True
    assert verify_postal_code_format(country_iso2="TZ", postal_code="31324") is True
    assert verify_postal_code_format(country_iso2="UA", postal_code="65000") is True
    assert verify_postal_code_format(country_iso2="US", postal_code="00716") is True
    assert verify_postal_code_format(country_iso2="US", postal_code="00716-9999") is True
    assert verify_postal_code_format(country_iso2="US", postal_code="11550") is True
    assert verify_postal_code_format(country_iso2="US", postal_code="11550-9999") is True
    assert verify_postal_code_format(country_iso2="UY", postal_code="11700") is True
    assert verify_postal_code_format(country_iso2="UZ", postal_code="702100") is True
    assert verify_postal_code_format(country_iso2="VA", postal_code="00120") is True
    assert verify_postal_code_format(country_iso2="VC", postal_code="VC1234") is True
    assert verify_postal_code_format(country_iso2="VE", postal_code="1061") is True
    assert verify_postal_code_format(country_iso2="VG", postal_code="VG1110") is True
    assert verify_postal_code_format(country_iso2="VI", postal_code="00850") is True
    assert verify_postal_code_format(country_iso2="VI", postal_code="00850-9999") is True
    assert verify_postal_code_format(country_iso2="VN", postal_code="112132") is True
    assert verify_postal_code_format(country_iso2="WF", postal_code="98600") is True
    assert verify_postal_code_format(country_iso2="WS", postal_code="WS1382") is True
    assert verify_postal_code_format(country_iso2="ZA", postal_code="6001") is True
    assert verify_postal_code_format(country_iso2="ZM", postal_code="50100") is True
    # Aland Islands (Finland system)
    assert verify_postal_code_format(country_iso2="AX", postal_code="22100") is True
    # french territories
    assert verify_postal_code_format(country_iso2="BL", postal_code="97133") is True
    assert verify_postal_code_format(country_iso2="GF", postal_code="97310") is True
    assert verify_postal_code_format(country_iso2="GP", postal_code="97122") is True
    assert verify_postal_code_format(country_iso2="MC", postal_code="98000") is True
    assert verify_postal_code_format(country_iso2="MF", postal_code="97150") is True
    assert verify_postal_code_format(country_iso2="MQ", postal_code="97212") is True
    assert verify_postal_code_format(country_iso2="PM", postal_code="97500") is True
    assert verify_postal_code_format(country_iso2="RE", postal_code="97450") is True
    assert verify_postal_code_format(country_iso2="YT", postal_code="97600") is True
    # end of french territories
    # Western Sahara (Morocco system)
    assert verify_postal_code_format(country_iso2="EH", postal_code="70000") is True
    assert verify_postal_code_format(country_iso2="EH", postal_code="71000") is True
    # Puerto Rico (US system)
    assert verify_postal_code_format(country_iso2="PR", postal_code="00716") is True
    assert verify_postal_code_format(country_iso2="PR", postal_code="00601") is True
    assert verify_postal_code_format(country_iso2="PR", postal_code="00716-9999") is True
    # Svaldbard and Jan Mayen (Norway system)
    assert verify_postal_code_format(country_iso2="SJ", postal_code="8099") is True
    assert verify_postal_code_format(country_iso2="SJ", postal_code="9170") is True
    assert verify_postal_code_format(country_iso2="SJ", postal_code="9171") is True


def test_countries_with_postal_code():
    # Aland Islands (Finland system)
    assert verify_postal_code_format(country_iso2="AX", postal_code="22100", strict=True) is True
    # french territories
    assert verify_postal_code_format(country_iso2="BL", postal_code="97133", strict=True) is True
    assert verify_postal_code_format(country_iso2="GF", postal_code="97310", strict=True) is True
    assert verify_postal_code_format(country_iso2="GP", postal_code="97122", strict=True) is True
    assert verify_postal_code_format(country_iso2="MC", postal_code="98000", strict=True) is True
    assert verify_postal_code_format(country_iso2="MF", postal_code="97150", strict=True) is True
    assert verify_postal_code_format(country_iso2="MQ", postal_code="97212", strict=True) is True
    assert verify_postal_code_format(country_iso2="PM", postal_code="97500", strict=True) is True
    assert verify_postal_code_format(country_iso2="RE", postal_code="97450", strict=True) is True
    assert verify_postal_code_format(country_iso2="YT", postal_code="97600", strict=True) is True
    # end of french territories
    # Western Sahara (Morocco system)
    assert verify_postal_code_format(country_iso2="EH", postal_code="70000", strict=True) is True
    assert verify_postal_code_format(country_iso2="EH", postal_code="71000", strict=True) is True
    # Puerto Rico (US system)
    assert verify_postal_code_format(country_iso2="PR", postal_code="00716", strict=True) is True
    assert verify_postal_code_format(country_iso2="PR", postal_code="00601", strict=True) is True
    assert verify_postal_code_format(country_iso2="PR", postal_code="00716-9999", strict=True) is True
    # Svaldbard and Jan Mayen (Norway system)
    assert verify_postal_code_format(country_iso2="SJ", postal_code="8099", strict=True) is True
    assert verify_postal_code_format(country_iso2="SJ", postal_code="9170", strict=True) is True
    assert verify_postal_code_format(country_iso2="SJ", postal_code="9171", strict=True) is True


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


def test_get_countries_without_postal_code():
    assert isinstance(get_countries_without_postal_code(), tuple)
    assert len(get_countries_without_postal_code()) > 0
    assert len(get_countries_without_postal_code()[:1]) == 1


def test_get_regex_for_given_postal_code():
    assert get_postal_code_regex("SK") == r"^(\d{3} \d{2})|\d{5}$"
    assert get_postal_code_regex("KK") is None
