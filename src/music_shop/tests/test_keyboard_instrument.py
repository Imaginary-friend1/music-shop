from music_shop.models.keyboard_instrument import KeyboardInstrument

def test_create_keyboard_instrument():
    instrument = KeyboardInstrument(article="KEY001", name="Yamaha P-45", price=55000, key_count=88, has_pedals=True)

    assert instrument.article == "KEY001"
    assert instrument.name == "Yamaha P-45"
    assert instrument.price == 55000
    assert instrument.key_count == 88
    assert instrument.has_pedals is True

def test_adjust_keys():
    instrument = KeyboardInstrument(article="KEY001", name="Yamaha P-45", price=55000, key_count=88, has_pedals=True)

    instrument.adjust_keys(76)

    assert instrument.key_count == 76
