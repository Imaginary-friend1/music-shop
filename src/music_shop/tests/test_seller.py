from music_shop.models.instrument import Instrument
from music_shop.models.store import Store
from music_shop.models.warehouse import Warehouse
from music_shop.models.seller import Seller

def test_find_instrument():
    warehouse = Warehouse("ул. Ленина, 10")
    store = Store("ул. Пушкина, 5", warehouse)
    seller = Seller("Иванов Иван Иванович", 3)
    instrument = Instrument("GTR001", "Yamaha F310", 25000)

    warehouse.store_instrument(instrument)
    store.receive_instrument(instrument)

    result = seller.find_instrument(store, "GTR001")

    assert result is instrument

def test_sell_instrument():
    warehouse = Warehouse("ул. Ленина, 10")
    store = Store("ул. Пушкина, 5", warehouse)
    seller = Seller("Иванов Иван Иванович", 3)
    instrument = Instrument("GTR001", "Yamaha F310", 25000)

    warehouse.store_instrument(instrument)
    store.receive_instrument(instrument)

    result = seller.sell_instrument(store, "GTR001")

    assert result is instrument
    assert instrument not in store.sold_instruments

def test_find_missing_instrument():
    warehouse = Warehouse("ул. Ленина, 10")
    store = Store("ул. Пушкина, 5", warehouse)
    seller = Seller("Иванов Иван Иванович", 3)

    result = seller.find_instrument(store, "UNKNOWN")

    assert result is None
