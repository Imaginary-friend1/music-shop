def create_receipt(self):
    """Открывает форму формирования чека."""

    window = tk.Toplevel(self.root)
    window.title("Формирование чека")
    window.geometry("450x400")

    tk.Label(
        window,
        text="Номер чека:",
    ).pack(pady=5)

    receipt_number_entry = tk.Entry(window)
    receipt_number_entry.pack()

    tk.Label(
        window,
        text="Способ оплаты:",
    ).pack(pady=5)

    payment_entry = tk.Entry(window)
    payment_entry.pack()

    tk.Label(
        window,
        text="Артикул товара:",
    ).pack(pady=5)

    article_entry = tk.Entry(window)
    article_entry.pack()

    def save_receipt():
        """Формирует и сохраняет чек."""

        receipt_number = receipt_number_entry.get().strip()
        payment_method = payment_entry.get().strip()
        article = article_entry.get().strip()

        if not receipt_number or not payment_method or not article:
            messagebox.showwarning(
                "Предупреждение",
                "Заполните все поля.",
            )
            return

        try:
            receipt_number = int(receipt_number)
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

        instrument = self.product_service.repository.get_by_article(
            article
        )

        if instrument is None:
            messagebox.showwarning(
                "Предупреждение",
                "Товар не найден.",
            )
            return

        from music_shop.models.instrument import Instrument

        instrument_object = Instrument(
            article=instrument[0],
            name=instrument[1],
            price=instrument[2],
        )

        receipt = Receipt(
            receipt_number=receipt_number,
            payment_method=payment_method,
        )

        receipt.add_item(instrument_object)

        filename = f"receipt_{receipt_number}.xlsx"

        receipt_service = ReceiptService()

        receipt_service.export_to_excel(
            receipt,
            filename,
        )

        messagebox.showinfo(
            "Готово",
            f"Чек сохранён в файл:\n{filename}",
        )

        window.destroy()

    tk.Button(
        window,
        text="Сохранить чек",
        command=save_receipt,
    ).pack(pady=25)
