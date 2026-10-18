from openpyxl import load_workbook

from music_shop.models.instrument import Instrument
from music_shop.models.receipt import Receipt
from music_shop.services.receipt_service import ReceiptService

def test_export_to_excel(tmp_path):
    service = ReceiptService()

    receipt = Receipt(
        receipt_number=1,
        payment_method="карта",
    )

    instrument = Instrument(
        article="GTR001",
        name="Yamaha F310",
        price=25000,
    )

    receipt.add_item(instrument)

    filename = tmp_path / "receipt.xlsx"

    service.export_to_excel(
        receipt,
        str(filename),
    )

    workbook = load_workbook(filename)
    sheet = workbook["Чек"]

    assert sheet["A1"].value == "Чек"
    assert sheet["B2"].value == 1
    assert sheet["B3"].value == "карта"
    assert sheet["A5"].value == "Артикул"
    assert sheet["B5"].value == "Наименование"
    assert sheet["C5"].value == "Цена"
    assert sheet["A6"].value == "GTR001"
    assert sheet["B6"].value == "Yamaha F310"
    assert sheet["C6"].value == 25000
    assert sheet["B7"].value == "Итого"
    assert sheet["C7"].value == 25000

    workbook.close()
