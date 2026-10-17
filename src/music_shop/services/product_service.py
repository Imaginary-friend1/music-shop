from music_shop.models.instrument import Instrument
from music_shop.repositories.instrument_repository import InstrumentRepository

class ProductService:
    """Сервис управления товарами магазина."""

    def __init__(self, repository: InstrumentRepository):
        self.repository = repository

    def add_product(self, instrument: Instrument, instrument_type: str) -> None:
        """Добавляет новый товар в базу данных."""
        self.repository.add(instrument, instrument_type)

    def get_product(self, article: str):
        """Находит товар по артикулу."""
        return self.repository.get_by_article(article)

    def update_product(self, article: str, name: str, price: int) -> None:
        """Изменяет название и цену товара."""
        self.repository.update(article, name, price)

    def delete_product(self, article: str) -> None:
        """Удаляет товар по артикулу."""
        self.repository.delete(article)
