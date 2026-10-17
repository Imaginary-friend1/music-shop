from music_shop.models.instrument import Instrument
from music_shop.models.receipt import Receipt

def test_create_receipt():
    receipt = Receipt(receipt_number=1, payment_method="карта")

    assert receipt.receipt_number == 1
    assert receipt.payment_method == "карта"
    assert receipt.items == []

def test_add_item():
    receipt = Receipt(receipt_number=1, payment_method="карта")
    instrument = Instrument(article="GTR001", name="Yamaha F310", price=25000)

    receipt.add_item(instrument)

    assert instrument in receipt.items

def test_get_total():
    receipt = Receipt(receipt_number=1, payment_method="карта")
    guitar = Instrument(article="GTR001", name="Yamaha F310", price=25000)
    piano = Instrument(article="KEY001", name="Yamaha P-45", price=55000)

    receipt.add_item(guitar)
    receipt.add_item(piano)

    assert receipt.get_total() == 80000
