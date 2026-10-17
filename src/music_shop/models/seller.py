class Seller:
    """Продавец музыкального магазина."""

    def __init__(self, full_name: str, experience: int):
        self.full_name = full_name
        self.experience = experience

    def find_instrument(self, store, article: str):
        """Находит инструмент в магазине по артикулу."""
        return store.search_instrument(article)

    def sell_instrument(self, store, article: str):
        """Продаёт инструмент покупателю."""
        return store.sell_instrument(article)
