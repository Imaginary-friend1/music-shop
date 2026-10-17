from music_shop.models.string_instrument import StringInstrument

def test_create_string_instrument():
    instrument = StringInstrument(article="GTR002", name="Yamaha C40", price=20000, string_count=6, string_material="нейлон")

    assert instrument.article == "GTR002"
    assert instrument.name == "Yamaha C40"
    assert instrument.price == 20000
    assert instrument.string_count == 6
    assert instrument.string_material == "нейлон"

def test_tune():
    instrument = StringInstrument(article="GTR002", name="Yamaha C40", price=20000, string_count=6, string_material="нейлон")

    assert instrument.tune() == "Yamaha C40 настроен."

def test_replace_strings():
    instrument = StringInstrument(article="GTR002", name="Yamaha C40", price=20000, string_count=6, string_material="нейлон")

    instrument.replace_strings(6, "металл")

    assert instrument.string_count == 6
    assert instrument.string_material == "металл"
