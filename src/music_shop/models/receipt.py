class Receipt:
    """Чек о покупке музыкальных инструментов."""

    def __init__(self, receipt_number: int, payment_method: str):
        self.receipt_number = receipt_number
        self.payment_method = payment_method
        self.items = []

    def add_item(self, instrument) -> None:
        """Добавляет инструмент в чек."""
        self.items.append(instrument)

    def get_total(self) -> int:
        """Возвращает общую стоимость товаров в чеке."""
        return sum(instrument.price for instrument in self.items)
