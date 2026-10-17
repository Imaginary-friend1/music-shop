from music_shop.models.store import Store
from music_shop.models.instrument import Instrument

class StoreService:
    """Сервис для работы с музыкальным магазином."""

    def receive_instrument(self, store: Store, instrument: Instrument) -> None:
        """Принимает инструмент в магазин."""
        store.receive_instrument(instrument)

    def search_instrument(self, store: Store, article: str) -> Instrument | None:
        """Ищет инструмент по артикулу."""
        return store.search_instrument(article)

    def sell_instrument(self, store: Store, article: str) -> Instrument | None:
        """Продаёт инструмент."""
        return store.sell_instrument(article)
