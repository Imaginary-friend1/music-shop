from music_shop.models.instrument import Instrument
from music_shop.models.warehouse import Warehouse


def test_create_warehouse():
    warehouse = Warehouse("ул. Музыкальная, 1")

    assert warehouse.address == "ул. Музыкальная, 1"
    assert warehouse.instruments == []


def test_store_instrument():
    warehouse = Warehouse("ул. Музыкальная, 1")
    instrument = Instrument("GTR001", "Yamaha F310", 25000)

    warehouse.store_instrument(instrument)

    assert instrument in warehouse.instruments


def test_find_instrument():
    warehouse = Warehouse("ул. Музыкальная, 1")
    instrument = Instrument("GTR001", "Yamaha F310", 25000)

    warehouse.store_instrument(instrument)

    result = warehouse.find_instrument("GTR001")

    assert result == instrument


def test_remove_instrument():
    warehouse = Warehouse("ул. Музыкальная, 1")
    instrument = Instrument("GTR001", "Yamaha F310", 25000)

    warehouse.store_instrument(instrument)

    result = warehouse.remove_instrument("GTR001")

    assert result == instrument
    assert instrument not in warehouse.instruments


def test_find_instrument_not_found():
    warehouse = Warehouse("ул. Музыкальная, 1")

    result = warehouse.find_instrument("UNKNOWN")

    assert result is None


def test_remove_instrument_not_found():
    warehouse = Warehouse("ул. Музыкальная, 1")

    result = warehouse.remove_instrument("UNKNOWN")

    assert result is None
