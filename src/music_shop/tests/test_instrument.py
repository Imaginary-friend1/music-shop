from music_shop.models.instrument import Instrument

def test_create_instrument():
  instrument = Instrument(article="GTR001", name="Yamaha F310", price=25000)

    assert instrument.article == "GTR001"
    assert instrument.name == "Yamaha F310"
    assert instrument.price == 25000

def test_get_info():
    instrument = Instrument(article="GTR001", name="Yamaha F310", price=25000)

    assert instrument.get_info() == ("GTR001: Yamaha F310, цена: 25000 руб.")
