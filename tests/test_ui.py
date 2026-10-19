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
