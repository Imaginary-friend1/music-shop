import sqlite3

from music_shop.database.database import Database

def test_create_tables(tmp_path):
    database_file = tmp_path / "test_music_shop.db"

    database = Database(str(database_file))
    database.create_tables()

    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        """
    )

    tables = {row[0] for row in cursor.fetchall()}

    connection.close()

    assert "warehouses" in tables
    assert "stores" in tables
    assert "instruments" in tables
    assert "sellers" in tables
    assert "receipts" in tables
    assert "receipt_items" in tables
