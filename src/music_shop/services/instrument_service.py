from music_shop.models.instrument import Instrument

class InstrumentService:
    """Сервис для работы с музыкальными инструментами."""

    def create_instrument(self, article: str, name: str, price: int) -> Instrument:
        """Создаёт новый музыкальный инструмент."""
        return Instrument(article, name, price)

    def get_instrument_info(self, instrument: Instrument) -> str:
        """Возвращает информацию об инструменте."""
        return instrument.get_info()
