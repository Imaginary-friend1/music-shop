from .instrument import Instrument

class KeyboardInstrument(Instrument):
    """Класс клавишного музыкального инструмента."""

    def __init__(self, article: str, name: str, price: int, key_count: int, has_pedals: bool):
        super().__init__(article, name, price)
        self.key_count = key_count
        self.has_pedals = has_pedals

    def adjust_keys(self, key_count: int) -> None:
        """Настраивает количество клавиш инструмента."""
        self.key_count = key_count
