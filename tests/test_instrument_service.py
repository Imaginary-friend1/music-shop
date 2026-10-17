from music_shop.models.instrument import Instrument
from music_shop.services.instrument_service import InstrumentService

def test_create_instrument():
    service = InstrumentService()

    instrument = service.create_instrument(
        article="GTR001",
        name="Yamaha F310",
        price=25000,
    )

    assert instrument.article == "GTR001"
    assert instrument.name == "Yamaha F310"
    assert instrument.price == 25000

def test_get_instrument_info():
    service = InstrumentService()

    instrument = Instrument(
        article="GTR001",
        name="Yamaha F310",
        price=25000,
    )

    result = service.get_instrument_info(instrument)

    assert result == (
        "GTR001: Yamaha F310, цена: 25000 руб."
    )
