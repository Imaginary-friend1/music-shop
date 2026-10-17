from .instrument import Instrument

class StringInstrument(Instrument):
    """Класс струнного музыкального инструмента."""

    def __init__(self, article: str, name: str, price: int, string_count: int, string_material: str):
        super().__init__(article, name, price)
        self.string_count = string_count
        self.string_material = string_material

    def tune(self) -> str:
        """Возвращает сообщение о настройке инструмента."""
        return f"{self.name} настроен."

    def replace_strings(self, string_count: int, string_material: str) -> None:
        """Заменяет струны и обновляет их характеристики."""
        self.string_count = string_count
        self.string_material = string_material
