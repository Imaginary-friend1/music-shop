from music_shop.models.warehouse import Warehouse
from music_shop.models.instrument import Instrument

class WarehouseService:
    """Сервис для работы со складом."""

    def add_instrument(
        self, warehouse: Warehouse, instrument: Instrument) -> None:
        """Добавляет инструмент на склад."""
        warehouse.store_instrument(instrument)

    def remove_instrument(self, warehouse: Warehouse, article: str) -> Instrument | None:
        """Удаляет инструмент со склада по артикулу."""
        return warehouse.remove_instrument(article)
