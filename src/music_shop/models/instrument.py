class Instrument:
  """Базовый класс музыкального инструмента."""
  
  def __init__(self, article: str, name: str, price: int):
    self.article = article
    self.name = name
    self.price = price

def get_info(self) -> str:
  """Возвращает информацию об инструменте."""
  return f"{self.article}: {self.name}, цена: {self.price} руб."
