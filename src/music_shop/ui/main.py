import tkinter as tk
from tkinter import messagebox

class MusicShopApp:
    """Графический интерфейс музыкального магазина."""

    def __init__(self, root):
        self.root = root
        self.root.title("Музыкальный магазин")
        self.root.geometry("700x500")

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

        article = self.article_entry.get()

        if not article:
            messagebox.showwarning(
                "Предупреждение",
                "Введите артикул товара.",
            )
            return

        self.result_label.config(
            text=f"Поиск товара: {article}"
        )

    def add_product(self):
        """Открывает форму добавления товара."""

        messagebox.showinfo(
            "Добавление товара",
            "Здесь будет форма добавления товара.",
        )

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
    app = MusicShopApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
