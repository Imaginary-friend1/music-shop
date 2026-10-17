from music_shop.models.instrument import Instrument
from music_shop.models.store import Store
from music_shop.models.warehouse import Warehouse

def test_receive_instrument():
    warehouse = Warehouse("ул. Ленина, 10")
    store = Store("ул. Пушкина, 5", warehouse)
    instrument = Instrument("GTR001", "Yamaha F310", 25000)

    warehouse.store_instrument(instrument)
    store.receive_instrument(instrument)

    assert instrument not in warehouse.instruments
    assert instrument in store.sold_instruments

def test_search_instrument():
    warehouse = Warehouse("ул. Ленина, 10")
    store = Store("ул. Пушкина, 5", warehouse)
    instrument = Instrument("GTR001", "Yamaha F310", 25000)

    warehouse.store_instrument(instrument)
    store.receive_instrument(instrument)

    result = store.search_instrument("GTR001")

    assert result is instrument

def test_search_missing_instrument():
    warehouse = Warehouse("ул. Ленина, 10")
    store = Store("ул. Пушкина, 5", warehouse)

    result = store.search_instrument("UNKNOWN")

    assert result is None

def test_sell_instrument():
    warehouse = Warehouse("ул. Ленина, 10")
    store = Store("ул. Пушкина, 5", warehouse)
    instrument = Instrument("GTR001", "Yamaha F310", 25000)

    warehouse.store_instrument(instrument)
    store.receive_instrument(instrument)

    result = store.sell_instrument("GTR001")

    assert result is instrument
    assert instrument not in store.sold_instruments

def test_sell_missing_instrument():
    warehouse = Warehouse("ул. Ленина, 10")
    store = Store("ул. Пушкина, 5", warehouse)

    result = store.sell_instrument("UNKNOWN")

    assert result is None
