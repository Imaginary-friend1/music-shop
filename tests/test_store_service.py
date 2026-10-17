from music_shop.models.instrument import Instrument
from music_shop.models.store import Store
from music_shop.models.warehouse import Warehouse
from music_shop.services.store_service import StoreService

def create_store():
    warehouse = Warehouse("ул. Ленина, 10")
    store = Store("ул. Пушкина, 5", warehouse)

    instrument = Instrument(
        article="GTR001",
        name="Yamaha F310",
        price=25000,
    )

    warehouse.store_instrument(instrument)
    store.receive_instrument(instrument)

    return store

def test_receive_instrument():
    service = StoreService()

    warehouse = Warehouse("ул. Ленина, 10")
    store = Store("ул. Пушкина, 5", warehouse)

    instrument = Instrument(
        article="GTR001",
        name="Yamaha F310",
        price=25000,
    )

    service.receive_instrument(store, instrument)

    assert instrument in store.sold_instruments

def test_search_instrument():
    service = StoreService()
    store = create_store()

    result = service.search_instrument(
        store,
        "GTR001",
    )

    assert result is not None
    assert result.article == "GTR001"

def test_sell_instrument():
    service = StoreService()
    store = create_store()

    result = service.sell_instrument(
        store,
        "GTR001",
    )

    assert result is not None
    assert result.article == "GTR001"
    assert store.search_instrument("GTR001") is None
