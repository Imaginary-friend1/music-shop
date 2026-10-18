import tkinter as tk
from tkinter import messagebox

from music_shop.models.instrument import Instrument
from music_shop.models.receipt import Receipt
from music_shop.repositories.instrument_repository import InstrumentRepository
from music_shop.services.product_service import ProductService
from music_shop.services.receipt_service import ReceiptService


class MusicShopApp:
    """Графический интерфейс музыкального магазина."""

    def __init__(self, root):
        self.root = root
        self.root.title("Музыкальный магазин")

        self.repository = InstrumentRepository()
        self.product_service = ProductService(self.repository)

        self.create_widgets()

    def create_widgets(self):
        """Создаёт элементы главного окна."""
        tk.Label(self.root, text="Артикул товара:").pack()

        self.article_entry = tk.Entry(self.root)
        self.article_entry.pack()

        tk.Button(
            self.root,
            text="Найти товар",
            command=self.search_product,
        ).pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        tk.Button(
            self.root,
            text="Добавить товар",
            command=self.add_product,
        ).pack()

        tk.Button(
            self.root,
            text="Изменить товар",
            command=self.update_product,
        ).pack()

        tk.Button(
            self.root,
            text="Удалить товар",
            command=self.delete_product,
        ).pack()

        tk.Button(
            self.root,
            text="Сформировать чек",
            command=self.create_receipt,
        ).pack()

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
            self.result_label.config(text="Товар не найден.")
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
        """Открывает окно добавления товара."""
        window = tk.Toplevel(self.root)
        window.title("Добавить товар")

        tk.Label(window, text="Артикул:").pack()
        article_entry = tk.Entry(window)
        article_entry.pack()

        tk.Label(window, text="Название:").pack()
        name_entry = tk.Entry(window)
        name_entry.pack()

        tk.Label(window, text="Цена:").pack()
        price_entry = tk.Entry(window)
        price_entry.pack()

        tk.Label(window, text="Тип:").pack()
        type_entry = tk.Entry(window)
        type_entry.pack()

        def save_product():
            """Сохраняет новый товар."""
            article = article_entry.get().strip()
            name = name_entry.get().strip()
            price_text = price_entry.get().strip()
            instrument_type = type_entry.get().strip()

            if not article or not name or not price_text or not instrument_type:
                messagebox.showwarning(
                    "Предупреждение",
                    "Заполните все поля.",
                )
                return

            try:
                price = int(price_text)
            except ValueError:
                messagebox.showwarning(
                    "Предупреждение",
                    "Цена должна быть числом.",
                )
                return

            instrument = Instrument(article, name, price)

            self.product_service.add_product(
                instrument,
                instrument_type,
            )

            messagebox.showinfo(
                "Успешно",
                "Товар добавлен.",
            )

            window.destroy()

        tk.Button(
            window,
            text="Сохранить",
            command=save_product,
        ).pack()

    def update_product(self):
        """Открывает окно изменения товара."""
        window = tk.Toplevel(self.root)
        window.title("Изменить товар")

        tk.Label(window, text="Артикул:").pack()
        article_entry = tk.Entry(window)
        article_entry.pack()

        tk.Label(window, text="Новое название:").pack()
        name_entry = tk.Entry(window)
        name_entry.pack()

        tk.Label(window, text="Новая цена:").pack()
        price_entry = tk.Entry(window)
        price_entry.pack()

        def save_changes():
            """Сохраняет изменения товара."""
            article = article_entry.get().strip()
            name = name_entry.get().strip()
            price_text = price_entry.get().strip()

            if not article or not name or not price_text:
                messagebox.showwarning(
                    "Предупреждение",
                    "Заполните все поля.",
                )
                return

            try:
                price = int(price_text)
            except ValueError:
                messagebox.showwarning(
                    "Предупреждение",
                    "Цена должна быть числом.",
                )
                return

            if self.product_service.get_product(article) is None:
                messagebox.showwarning(
                    "Предупреждение",
                    "Товар не найден.",
                )
                return

            self.product_service.update_product(
                article,
                name,
                price,
            )

            messagebox.showinfo(
                "Успешно",
                "Товар изменён.",
            )

            window.destroy()

        tk.Button(
            window,
            text="Сохранить",
            command=save_changes,
        ).pack()

    def delete_product(self):
        """Удаляет товар по артикулу."""
        article = self.article_entry.get().strip()

        if not article:
            messagebox.showwarning(
                "Предупреждение",
                "Введите артикул товара.",
            )
            return

        if self.product_service.get_product(article) is None:
            messagebox.showwarning(
                "Предупреждение",
                "Товар не найден.",
            )
            return

        self.product_service.delete_product(article)

        self.result_label.config(
            text="Товар удалён."
        )

        messagebox.showinfo(
            "Успешно",
            "Товар удалён.",
        )

    def create_receipt(self):
        """Открывает окно формирования чека."""
        window = tk.Toplevel(self.root)
        window.title("Формирование чека")

        tk.Label(window, text="Номер чека:").pack()
        number_entry = tk.Entry(window)
        number_entry.pack()

        tk.Label(window, text="Способ оплаты:").pack()
        payment_entry = tk.Entry(window)
        payment_entry.pack()

        tk.Label(window, text="Артикул товара:").pack()
        article_entry = tk.Entry(window)
        article_entry.pack()

        def save_receipt():
            """Формирует и сохраняет чек."""
            number_text = number_entry.get().strip()
            payment_method = payment_entry.get().strip()
            article = article_entry.get().strip()

            if not number_text or not payment_method or not article:
                messagebox.showwarning(
                    "Предупреждение",
                    "Заполните все поля.",
                )
                return

            try:
                receipt_number = int(number_text)
            except ValueError:
                messagebox.showwarning(
                    "Предупреждение",
                    "Номер чека должен быть числом.",
                )
                return

            product = self.product_service.get_product(article)

            if product is None:
                messagebox.showwarning(
                    "Предупреждение",
                    "Товар не найден.",
                )
                return

            instrument = Instrument(
                product[0],
                product[1],
                product[2],
            )

            receipt = Receipt(
                receipt_number,
                payment_method,
            )

            receipt.add_item(instrument)

            filename = f"receipt_{receipt_number}.xlsx"

            ReceiptService().export_to_excel(
                receipt,
                filename,
            )

            messagebox.showinfo(
                "Успешно",
                f"Чек сохранён в файл {filename}.",
            )

            window.destroy()

        tk.Button(
            window,
            text="Сохранить чек",
            command=save_receipt,
        ).pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicShopApp(root)
    root.mainloop()
