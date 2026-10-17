from music_shop.database.database import Database
from music_shop.models.instrument import Instrument
from music_shop.repositories.instrument_repository import InstrumentRepository
from music_shop.services.product_service import ProductService

def create_service(tmp_path):
    database_file = tmp_path / "test_music_shop.db"

    database = Database(str(database_file))
    database.create_tables()

    repository = InstrumentRepository(str(database_file))

    return ProductService(repository)

def test_add_product(tmp_path):
    service = create_service(tmp_path)

    instrument = Instrument(
        article="GTR001",
        name="Yamaha F310",
        price=25000,
    )

    service.add_product(instrument, "string")

    result = service.get_product("GTR001")

    assert result == (
        "GTR001",
        "Yamaha F310",
        25000,
        "string",
    )

def test_get_product(tmp_path):
    service = create_service(tmp_path)

    instrument = Instrument(
        article="GTR001",
        name="Yamaha F310",
        price=25000,
    )

    service.add_product(instrument, "string")

    result = service.get_product("GTR001")

    assert result is not None
    assert result[0] == "GTR001"

def test_update_product(tmp_path):
    service = create_service(tmp_path)

    instrument = Instrument(
        article="GTR001",
        name="Yamaha F310",
        price=25000,
    )

    service.add_product(instrument, "string")

    service.update_product(
        article="GTR001",
        name="Yamaha F310 Natural",
        price=28000,
    )

    result = service.get_product("GTR001")

    assert result == (
        "GTR001",
        "Yamaha F310 Natural",
        28000,
        "string",
    )

def test_delete_product(tmp_path):
    service = create_service(tmp_path)

    instrument = Instrument(
        article="GTR001",
        name="Yamaha F310",
        price=25000,
    )

    service.add_product(instrument, "string")

    service.delete_product("GTR001")

    result = service.get_product("GTR001")

    assert result is None
