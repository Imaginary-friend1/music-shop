class Warehouse:
    """Склад музыкальных инструментов."""

    def __init__(self, address: str):
        self.address = address
        self.instruments = []

    def store_instrument(self, instrument) -> None:
        """Добавляет инструмент на склад."""
        self.instruments.append(instrument)

    def remove_instrument(self, article: str):
        """Удаляет инструмент со склада по артикулу."""
        for instrument in self.instruments:
            if instrument.article == article:
                self.instruments.remove(instrument)
                return instrument

        return None

    def find_instrument(self, article: str):
        """Ищет инструмент на складе по артикулу."""
        for instrument in self.instruments:
            if instrument.article == article:
                return instrument

        return None
