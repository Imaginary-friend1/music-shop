import tkinter as tk
from tkinter import messagebox

from music_shop.database.database import Database
from music_shop.repositories.instrument_repository import InstrumentRepository
from music_shop.services.product_service import ProductService

class MusicShopApp:
    """Графический интерфейс музыкального магазина."""

    def __init__(self, root):
        self.root = root
        self.root.title("Музыкальный магазин")
        self.root.geometry("700x500")

        self.database = Database()
        self.database.create_tables()

        self.repository = InstrumentRepository()
        self.product_service = ProductService(self.repository)

        self.create_widgets()

    def create_widgets(self):
        """Создаёт элементы интерфейса."""

        title = tk.Label(
            self.root,
            text="Информационная система музыкального магазина",
            font=("Arial", 16),
        )
        title.pack(pady=20)

        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=10)

        tk.Label(
            search_frame,
            text="Артикул:",
        ).pack(side=tk.LEFT)

        self.article_entry = tk.Entry(search_frame)
        self.article_entry.pack(
            side=tk.LEFT,
            padx=10,
        )

        tk.Button(
            search_frame,
            text="Найти",
            command=self.search_product,
        ).pack(side=tk.LEFT)

        self.result_label = tk.Label(
            self.root,
            text="Введите артикул товара",
            font=("Arial", 12),
        )
        self.result_label.pack(pady=20)

        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=20)

        tk.Button(
            buttons_frame,
            text="Добавить товар",
            width=20,
            command=self.add_product,
        ).pack(pady=5)

        tk.Button(
            buttons_frame,
            text="Изменить товар",
            width=20,
            command=self.update_product,
        ).pack(pady=5)

        tk.Button(
            buttons_frame,
            text="Удалить товар",
            width=20,
            command=self.delete_product,
        ).pack(pady=5)

        tk.Button(
            buttons_frame,
            text="Сформировать чек",
            width=20,
            command=self.create_receipt,
        ).pack(pady=5)

    def search_product(self):
        """Ищет товар по артикулу."""

        article = self.article_entry.get().strip()

        if not article:
            messagebox.showwarning(
                "Предупреждение",
                "Введите артикул товара.",
            )
            return

        product = self.product_service.get_product(article)

        if product is None:
            self.result_label.config(
                text="Товар не найден."
            )
            return

        self.result_label.config(
            text=(
                f"Артикул: {product[0]}\n"
                f"Название: {product[1]}\n"
                f"Цена: {product[2]} руб.\n"
                f"Тип: {product[3]}"
            )
        )

    def add_product(self):
    """Открывает форму добавления товара."""

    window = tk.Toplevel(self.root)
    window.title("Добавление товара")
    window.geometry("400x350")

    tk.Label(window, text="Артикул:").pack(pady=5)
    article_entry = tk.Entry(window)
    article_entry.pack()

    tk.Label(window, text="Название:").pack(pady=5)
    name_entry = tk.Entry(window)
    name_entry.pack()

    tk.Label(window, text="Цена:").pack(pady=5)
    price_entry = tk.Entry(window)
    price_entry.pack()

    tk.Label(window, text="Тип инструмента:").pack(pady=5)
    type_entry = tk.Entry(window)
    type_entry.pack()

    def save_product():
        """Сохраняет новый товар."""

        article = article_entry.get().strip()
        name = name_entry.get().strip()
        price = price_entry.get().strip()
        instrument_type = type_entry.get().strip()

        if not article or not name or not price or not instrument_type:
            messagebox.showwarning(
                "Предупреждение",
                "Заполните все поля.",
            )
            return

        try:
            price = int(price)
        except ValueError:
            messagebox.showwarning(
                "Предупреждение",
                "Цена должна быть числом.",
            )
            return

        from music_shop.models.instrument import Instrument

        instrument = Instrument(
            article=article,
            name=name,
            price=price,
        )

        self.product_service.add_product(
            instrument,
            instrument_type,
        )

        messagebox.showinfo(
            "Готово",
            "Товар успешно добавлен.",
        )

        window.destroy()

    tk.Button(
        window,
        text="Сохранить",
        command=save_product,
    ).pack(pady=20)

    def update_product(self):
        """Открывает форму изменения товара."""

        messagebox.showinfo(
            "Изменение товара",
            "Здесь будет форма изменения товара.",
        )

    def delete_product(self):
        """Удаляет выбранный товар."""

        messagebox.showinfo(
            "Удаление товара",
            "Здесь будет удаление товара.",
        )

    def create_receipt(self):
        """Формирует чек."""

        messagebox.showinfo(
            "Чек",
            "Здесь будет формирование чека.",
        )

def main():
    """Запускает приложение."""

    root = tk.Tk()
    MusicShopApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
