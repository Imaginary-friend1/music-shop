from .warehouse import Warehouse

class Store:
    """Магазин музыкальных инструментов."""

    def __init__(self, address: str, warehouse: Warehouse):
        self.address = address
        self.warehouse = warehouse
        self.sold_instruments = []

    def receive_instrument(self, instrument) -> None:
        """Принимает инструмент со склада."""
        self.warehouse.remove_instrument(instrument.article)
        self.sold_instruments.append(instrument)

    def search_instrument(self, article: str):
        """Ищет инструмент по артикулу."""
        for instrument in self.sold_instruments:
            if instrument.article == article:
                return instrument

        return None

    def sell_instrument(self, article: str):
        """Продаёт инструмент по артикулу."""
        instrument = self.search_instrument(article)

        if instrument is not None:
            self.sold_instruments.remove(instrument)

        return instrument
