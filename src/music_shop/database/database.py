import sqlite3

class Database:
    """Работа с базой данных музыкального магазина."""

    def __init__(self, database_name: str = "music_shop.db"):
        self.database_name = database_name

    def connect(self):
        """Создаёт подключение к базе данных."""
        return sqlite3.connect(self.database_name)

    def create_tables(self) -> None:
        """Создаёт таблицы базы данных."""
        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS warehouses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                address TEXT NOT NULL
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS stores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                address TEXT NOT NULL,
                warehouse_id INTEGER NOT NULL,
                FOREIGN KEY (warehouse_id)
                    REFERENCES warehouses (id)
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS instruments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                article TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                price INTEGER NOT NULL,
                instrument_type TEXT NOT NULL
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS sellers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                experience INTEGER NOT NULL
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS receipts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                receipt_number INTEGER NOT NULL,
                payment_method TEXT NOT NULL
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS receipt_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                receipt_id INTEGER NOT NULL,
                instrument_id INTEGER NOT NULL,
                FOREIGN KEY (receipt_id)
                    REFERENCES receipts (id),
                FOREIGN KEY (instrument_id)
                    REFERENCES instruments (id)
            )
            """
        )

        connection.commit()
        connection.close()
