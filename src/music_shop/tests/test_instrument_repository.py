from music_shop.database.database import Database
from music_shop.models.instrument import Instrument
from music_shop.repositories.instrument_repository import InstrumentRepository

def test_add_and_get_instrument(tmp_path):
    database_file = tmp_path / "test_music_shop.db"

    database = Database(str(database_file))
    database.create_tables()

    repository = InstrumentRepository(str(database_file))

    instrument = Instrument(article="GTR001", name="Yamaha F310", price=25000)

    repository.add(instrument, "string")

    result = repository.get_by_article("GTR001")

    assert result == ("GTR001", "Yamaha F310", 25000, "string")

def test_get_missing_instrument(tmp_path):
    database_file = tmp_path / "test_music_shop.db"

    database = Database(str(database_file))
    database.create_tables()

    repository = InstrumentRepository(str(database_file))

    result = repository.get_by_article("UNKNOWN")

    assert result is None

def test_delete_instrument(tmp_path):
    database_file = tmp_path / "test_music_shop.db"

    database = Database(str(database_file))
    database.create_tables()

    repository = InstrumentRepository(str(database_file))

    instrument = Instrument(
        article="GTR001",
        name="Yamaha F310",
        price=25000,
    )

    repository.add(instrument, "string")
    repository.delete("GTR001")

    result = repository.get_by_article("GTR001")

    assert result is None
