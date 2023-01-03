from postal_codes_tools.mappers import territory_to_parent_mapper


def test_territory_to_parent_mapper():
    assert territory_to_parent_mapper("CZ") == "CZ"  # case if country is not in territory list
    assert territory_to_parent_mapper("AX") == "FI"
    assert territory_to_parent_mapper("BL") == "FR"
    assert territory_to_parent_mapper("GF") == "FR"
    assert territory_to_parent_mapper("GP") == "FR"
    assert territory_to_parent_mapper("MC") == "FR"
    assert territory_to_parent_mapper("MF") == "FR"
    assert territory_to_parent_mapper("MQ") == "FR"
    assert territory_to_parent_mapper("PM") == "FR"
    assert territory_to_parent_mapper("RE") == "FR"
    assert territory_to_parent_mapper("YT") == "FR"
    assert territory_to_parent_mapper("EH") == "MA"
    assert territory_to_parent_mapper("SJ") == "NO"
    assert territory_to_parent_mapper("PR") == "US"
