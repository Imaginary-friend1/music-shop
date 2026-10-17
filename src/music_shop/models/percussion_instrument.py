from .instrument import Instrument

class PercussionInstrument(Instrument):
    """Класс ударного музыкального инструмента."""

    def __init__(self, article: str, name: str, price: int, membrane_material: str, size: int):
        super().__init__(article, name, price)
        self.membrane_material = membrane_material
        self.size = size

    def replace_membrane(self, membrane_material: str, size: int) -> None:
        """Заменяет мембрану и обновляет её характеристики."""
        self.membrane_material = membrane_material
        self.size = size
