from music_shop.models.percussion_instrument import PercussionInstrument

def test_create_percussion_instrument():
    instrument = PercussionInstrument(article="DRM001", name="Pearl Export", price=45000, membrane_material="пластик", size=22)

    assert instrument.article == "DRM001"
    assert instrument.name == "Pearl Export"
    assert instrument.price == 45000
    assert instrument.membrane_material == "пластик"
    assert instrument.size == 22

def test_replace_membrane():
    instrument = PercussionInstrument(article="DRM001", name="Pearl Export", price=45000, membrane_material="пластик", size=22)

    instrument.replace_membrane("кожа", 24)

    assert instrument.membrane_material == "кожа"
    assert instrument.size == 24
