import sqlite3

from music_shop.models.instrument import Instrument

class InstrumentRepository:
    """Репозиторий для работы с инструментами в базе данных."""

    def __init__(self, database_name: str = "music_shop.db"):
        self.database_name = database_name

    def add(self, instrument: Instrument, instrument_type: str) -> None:
        """Добавляет инструмент в базу данных."""
        connection = sqlite3.connect(self.database_name)

        connection.execute(
            """
            INSERT INTO instruments (
                article,
                name,
                price,
                instrument_type
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                instrument.article,
                instrument.name,
                instrument.price,
                instrument_type,
            ),
        )

        connection.commit()
        connection.close()

    def get_by_article(self, article: str):
        """Находит инструмент по артикулу."""
        connection = sqlite3.connect(self.database_name)

        cursor = connection.execute(
            """
            SELECT article, name, price, instrument_type
            FROM instruments
            WHERE article = ?
            """,
            (article,),
        )

        result = cursor.fetchone()

        connection.close()

        return result

    def delete(self, article: str) -> None:
        """Удаляет инструмент по артикулу."""
        connection = sqlite3.connect(self.database_name)

        connection.execute(
            """
            DELETE FROM instruments
            WHERE article = ?
            """,
            (article,),
        )

        connection.commit()
        connection.close()
