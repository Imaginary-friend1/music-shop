from music_shop.models.instrument import Instrument
from music_shop.models.warehouse import Warehouse
from music_shop.services.warehouse_service import WarehouseService

def test_add_instrument():
    service = WarehouseService()
    warehouse = Warehouse("ул. Ленина, 10")

    instrument = Instrument(
        article="GTR001",
        name="Yamaha F310",
        price=25000,
    )

    service.add_instrument(warehouse, instrument)

    assert instrument in warehouse.instruments

def test_remove_instrument():
    service = WarehouseService()
    warehouse = Warehouse("ул. Ленина, 10")

    instrument = Instrument(
        article="GTR001",
        name="Yamaha F310",
        price=25000,
    )

    service.add_instrument(warehouse, instrument)

    result = service.remove_instrument(
        warehouse,
        "GTR001",
    )

    assert result is instrument
    assert instrument not in warehouse.instruments

def test_remove_missing_instrument():
    service = WarehouseService()
    warehouse = Warehouse("ул. Ленина, 10")

    result = service.remove_instrument(
        warehouse,
        "UNKNOWN",
    )

    assert result is None
