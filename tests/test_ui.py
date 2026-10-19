from unittest.mock import MagicMock, patch

from music_shop.models.instrument import Instrument
from music_shop.ui.main import MusicShopApp


def create_app():
    root = MagicMock()

    with patch.object(MusicShopApp, "create_widgets"):
        app = MusicShopApp(root)

    app.product_service = MagicMock()
    app.article_entry = MagicMock()
    app.result_label = MagicMock()

    return app


def test_search_product_empty_article():
    app = create_app()

    app.article_entry.get.return_value = ""

    with patch("music_shop.ui.main.messagebox.showwarning") as warning:
        app.search_product()

    warning.assert_called_once()


def test_search_product_not_found():
    app = create_app()

    app.article_entry.get.return_value = "UNKNOWN"
    app.product_service.get_product.return_value = None

    app.search_product()

    app.result_label.config.assert_called_once_with(
        text="Товар не найден."
    )


def test_search_product_found():
    app = create_app()

    app.article_entry.get.return_value = "GTR001"
    app.product_service.get_product.return_value = (
        "GTR001",
        "Yamaha F310",
        25000,
        "string",
    )

    app.search_product()

    app.result_label.config.assert_called_once_with(
        text=(
            "Артикул: GTR001\n"
            "Название: Yamaha F310\n"
            "Цена: 25000 руб.\n"
            "Тип: string"
        )
    )


def test_add_product_opens_window():
    app = create_app()

    with patch("music_shop.ui.main.tk.Toplevel") as window:
        with patch("music_shop.ui.main.tk.Label"):
            with patch("music_shop.ui.main.tk.Entry"):
                with patch("music_shop.ui.main.tk.Button"):
                    app.add_product()

    window.assert_called_once()


def test_update_product_opens_window():
    app = create_app()

    with patch("music_shop.ui.main.tk.Toplevel") as window:
        with patch("music_shop.ui.main.tk.Label"):
            with patch("music_shop.ui.main.tk.Entry"):
                with patch("music_shop.ui.main.tk.Button"):
                    app.update_product()

    window.assert_called_once()


def test_delete_product_empty_article():
    app = create_app()

    app.article_entry.get.return_value = ""

    with patch("music_shop.ui.main.messagebox.showwarning") as warning:
        app.delete_product()

    warning.assert_called_once()


def test_delete_product_not_found():
    app = create_app()

    app.article_entry.get.return_value = "UNKNOWN"
    app.product_service.get_product.return_value = None

    with patch("music_shop.ui.main.messagebox.showwarning") as warning:
        app.delete_product()

    warning.assert_called_once()


def test_delete_product():
    app = create_app()

    app.article_entry.get.return_value = "GTR001"
    app.product_service.get_product.return_value = (
        "GTR001",
        "Yamaha F310",
        25000,
        "string",
    )

    with patch("music_shop.ui.main.messagebox.showinfo"):
        app.delete_product()

    app.product_service.delete_product.assert_called_once_with(
        "GTR001"
    )

    app.result_label.config.assert_called_once_with(
        text="Товар удалён."
    )


def test_create_receipt_opens_window():
    app = create_app()

    with patch("music_shop.ui.main.tk.Toplevel") as window:
        with patch("music_shop.ui.main.tk.Label"):
            with patch("music_shop.ui.main.tk.Entry"):
                with patch("music_shop.ui.main.tk.Button"):
                    app.create_receipt()

    window.assert_called_once()
    
def test_create_widgets():
    root = MagicMock()
    app = MusicShopApp.__new__(MusicShopApp)
    app.root = root

    with patch("music_shop.ui.main.tk.Label") as label:
        with patch("music_shop.ui.main.tk.Entry") as entry:
            with patch("music_shop.ui.main.tk.Button") as button:
                app.create_widgets()

    assert label.call_count == 2
    assert entry.call_count == 1
    assert button.call_count == 5


def test_add_product_empty_fields():
    app = create_app()

    article_entry = MagicMock()
    name_entry = MagicMock()
    price_entry = MagicMock()
    type_entry = MagicMock()

    article_entry.get.return_value = ""
    name_entry.get.return_value = "Yamaha"
    price_entry.get.return_value = "25000"
    type_entry.get.return_value = "string"

    with patch("music_shop.ui.main.tk.Toplevel"):
        with patch("music_shop.ui.main.tk.Label"):
            with patch(
                "music_shop.ui.main.tk.Entry",
                side_effect=[
                    article_entry,
                    name_entry,
                    price_entry,
                    type_entry,
                ],
            ):
                with patch("music_shop.ui.main.tk.Button") as button:
                    app.add_product()

                    save_product = button.call_args.kwargs["command"]

                    with patch(
                        "music_shop.ui.main.messagebox.showwarning"
                    ) as warning:
                        save_product()

    warning.assert_called_once()


def test_add_product_invalid_price():
    app = create_app()

    article_entry = MagicMock()
    name_entry = MagicMock()
    price_entry = MagicMock()
    type_entry = MagicMock()

    article_entry.get.return_value = "GTR001"
    name_entry.get.return_value = "Yamaha F310"
    price_entry.get.return_value = "abc"
    type_entry.get.return_value = "string"

    with patch("music_shop.ui.main.tk.Toplevel"):
        with patch("music_shop.ui.main.tk.Label"):
            with patch(
                "music_shop.ui.main.tk.Entry",
                side_effect=[
                    article_entry,
                    name_entry,
                    price_entry,
                    type_entry,
                ],
            ):
                with patch("music_shop.ui.main.tk.Button") as button:
                    app.add_product()

                    save_product = button.call_args.kwargs["command"]

                    with patch(
                        "music_shop.ui.main.messagebox.showwarning"
                    ) as warning:
                        save_product()

    warning.assert_called_once()
    app.product_service.add_product.assert_not_called()


def test_add_product_success():
    app = create_app()

    article_entry = MagicMock()
    name_entry = MagicMock()
    price_entry = MagicMock()
    type_entry = MagicMock()

    article_entry.get.return_value = "GTR001"
    name_entry.get.return_value = "Yamaha F310"
    price_entry.get.return_value = "25000"
    type_entry.get.return_value = "string"

    with patch("music_shop.ui.main.tk.Toplevel") as window:
        with patch("music_shop.ui.main.tk.Label"):
            with patch(
                "music_shop.ui.main.tk.Entry",
                side_effect=[
                    article_entry,
                    name_entry,
                    price_entry,
                    type_entry,
                ],
            ):
                with patch("music_shop.ui.main.tk.Button") as button:
                    app.add_product()

                    save_product = button.call_args.kwargs["command"]

                    with patch(
                        "music_shop.ui.main.messagebox.showinfo"
                    ) as info:
                        save_product()

    app.product_service.add_product.assert_called_once()

    instrument = app.product_service.add_product.call_args.args[0]
    instrument_type = app.product_service.add_product.call_args.args[1]

    assert instrument.article == "GTR001"
    assert instrument.name == "Yamaha F310"
    assert instrument.price == 25000
    assert instrument_type == "string"

    info.assert_called_once()
    window.return_value.destroy.assert_called_once()


def test_update_product_empty_fields():
    app = create_app()

    article_entry = MagicMock()
    name_entry = MagicMock()
    price_entry = MagicMock()

    article_entry.get.return_value = ""
    name_entry.get.return_value = "Yamaha"
    price_entry.get.return_value = "25000"

    with patch("music_shop.ui.main.tk.Toplevel"):
        with patch("music_shop.ui.main.tk.Label"):
            with patch(
                "music_shop.ui.main.tk.Entry",
                side_effect=[
                    article_entry,
                    name_entry,
                    price_entry,
                ],
            ):
                with patch("music_shop.ui.main.tk.Button") as button:
                    app.update_product()

                    save_changes = button.call_args.kwargs["command"]

                    with patch(
                        "music_shop.ui.main.messagebox.showwarning"
                    ) as warning:
                        save_changes()

    warning.assert_called_once()


def test_update_product_invalid_price():
    app = create_app()

    article_entry = MagicMock()
    name_entry = MagicMock()
    price_entry = MagicMock()

    article_entry.get.return_value = "GTR001"
    name_entry.get.return_value = "Yamaha F310"
    price_entry.get.return_value = "abc"

    with patch("music_shop.ui.main.tk.Toplevel"):
        with patch("music_shop.ui.main.tk.Label"):
            with patch(
                "music_shop.ui.main.tk.Entry",
                side_effect=[
                    article_entry,
                    name_entry,
                    price_entry,
                ],
            ):
                with patch("music_shop.ui.main.tk.Button") as button:
                    app.update_product()

                    save_changes = button.call_args.kwargs["command"]

                    with patch(
                        "music_shop.ui.main.messagebox.showwarning"
                    ) as warning:
                        save_changes()

    warning.assert_called_once()
    app.product_service.update_product.assert_not_called()


def test_update_product_not_found():
    app = create_app()

    article_entry = MagicMock()
    name_entry = MagicMock()
    price_entry = MagicMock()

    article_entry.get.return_value = "UNKNOWN"
    name_entry.get.return_value = "Yamaha"
    price_entry.get.return_value = "25000"

    app.product_service.get_product.return_value = None

    with patch("music_shop.ui.main.tk.Toplevel"):
        with patch("music_shop.ui.main.tk.Label"):
            with patch(
                "music_shop.ui.main.tk.Entry",
                side_effect=[
                    article_entry,
                    name_entry,
                    price_entry,
                ],
            ):
                with patch("music_shop.ui.main.tk.Button") as button:
                    app.update_product()

                    save_changes = button.call_args.kwargs["command"]

                    with patch(
                        "music_shop.ui.main.messagebox.showwarning"
                    ) as warning:
                        save_changes()

    warning.assert_called_once()
    app.product_service.update_product.assert_not_called()


def test_update_product_success():
    app = create_app()

    article_entry = MagicMock()
    name_entry = MagicMock()
    price_entry = MagicMock()

    article_entry.get.return_value = "GTR001"
    name_entry.get.return_value = "Yamaha F310 New"
    price_entry.get.return_value = "30000"

    app.product_service.get_product.return_value = (
        "GTR001",
        "Yamaha F310",
        25000,
        "string",
    )

    with patch("music_shop.ui.main.tk.Toplevel") as window:
        with patch("music_shop.ui.main.tk.Label"):
            with patch(
                "music_shop.ui.main.tk.Entry",
                side_effect=[
                    article_entry,
                    name_entry,
                    price_entry,
                ],
            ):
                with patch("music_shop.ui.main.tk.Button") as button:
                    app.update_product()

                    save_changes = button.call_args.kwargs["command"]

                    with patch(
                        "music_shop.ui.main.messagebox.showinfo"
                    ) as info:
                        save_changes()

    app.product_service.update_product.assert_called_once_with(
        "GTR001",
        "Yamaha F310 New",
        30000,
    )

    info.assert_called_once()
    window.return_value.destroy.assert_called_once()


def test_create_receipt_empty_fields():
    app = create_app()

    number_entry = MagicMock()
    payment_entry = MagicMock()
    article_entry = MagicMock()

    number_entry.get.return_value = ""
    payment_entry.get.return_value = "Карта"
    article_entry.get.return_value = "GTR001"

    with patch("music_shop.ui.main.tk.Toplevel"):
        with patch("music_shop.ui.main.tk.Label"):
            with patch(
                "music_shop.ui.main.tk.Entry",
                side_effect=[
                    number_entry,
                    payment_entry,
                    article_entry,
                ],
            ):
                with patch("music_shop.ui.main.tk.Button") as button:
                    app.create_receipt()

                    save_receipt = button.call_args.kwargs["command"]

                    with patch(
                        "music_shop.ui.main.messagebox.showwarning"
                    ) as warning:
                        save_receipt()

    warning.assert_called_once()


def test_create_receipt_invalid_number():
    app = create_app()

    number_entry = MagicMock()
    payment_entry = MagicMock()
    article_entry = MagicMock()

    number_entry.get.return_value = "abc"
    payment_entry.get.return_value = "Карта"
    article_entry.get.return_value = "GTR001"

    with patch("music_shop.ui.main.tk.Toplevel"):
        with patch("music_shop.ui.main.tk.Label"):
            with patch(
                "music_shop.ui.main.tk.Entry",
                side_effect=[
                    number_entry,
                    payment_entry,
                    article_entry,
                ],
            ):
                with patch("music_shop.ui.main.tk.Button") as button:
                    app.create_receipt()

                    save_receipt = button.call_args.kwargs["command"]

                    with patch(
                        "music_shop.ui.main.messagebox.showwarning"
                    ) as warning:
                        save_receipt()

    warning.assert_called_once()


def test_create_receipt_product_not_found():
    app = create_app()

    number_entry = MagicMock()
    payment_entry = MagicMock()
    article_entry = MagicMock()

    number_entry.get.return_value = "1001"
    payment_entry.get.return_value = "Карта"
    article_entry.get.return_value = "UNKNOWN"

    app.product_service.get_product.return_value = None

    with patch("music_shop.ui.main.tk.Toplevel"):
        with patch("music_shop.ui.main.tk.Label"):
            with patch(
                "music_shop.ui.main.tk.Entry",
                side_effect=[
                    number_entry,
                    payment_entry,
                    article_entry,
                ],
            ):
                with patch("music_shop.ui.main.tk.Button") as button:
                    app.create_receipt()

                    save_receipt = button.call_args.kwargs["command"]

                    with patch(
                        "music_shop.ui.main.messagebox.showwarning"
                    ) as warning:
                        save_receipt()

    warning.assert_called_once()


def test_create_receipt_success():
    app = create_app()

    number_entry = MagicMock()
    payment_entry = MagicMock()
    article_entry = MagicMock()

    number_entry.get.return_value = "1001"
    payment_entry.get.return_value = "Карта"
    article_entry.get.return_value = "GTR001"

    app.product_service.get_product.return_value = (
        "GTR001",
        "Yamaha F310",
        25000,
        "string",
    )

    with patch("music_shop.ui.main.tk.Toplevel") as window:
        with patch("music_shop.ui.main.tk.Label"):
            with patch(
                "music_shop.ui.main.tk.Entry",
                side_effect=[
                    number_entry,
                    payment_entry,
                    article_entry,
                ],
            ):
                with patch("music_shop.ui.main.tk.Button") as button:
                    app.create_receipt()

                    save_receipt = button.call_args.kwargs["command"]

                    with patch(
                        "music_shop.ui.main.ReceiptService.export_to_excel"
                    ) as export:
                        with patch(
                            "music_shop.ui.main.messagebox.showinfo"
                        ) as info:
                            save_receipt()

    export.assert_called_once()

    receipt = export.call_args.args[0]
    filename = export.call_args.args[1]

    assert receipt.receipt_number == 1001
    assert receipt.payment_method == "Карта"
    assert len(receipt.items) == 1
    assert receipt.items[0].article == "GTR001"
    assert receipt.items[0].name == "Yamaha F310"
    assert receipt.items[0].price == 25000
    assert filename == "receipt_1001.xlsx"

    info.assert_called_once_with(
        "Успешно",
        "Чек сохранён в файл receipt_1001.xlsx.",
    )

    window.return_value.destroy.assert_called_once()
