from store.models.payment import CashPayment, CreditCardPayment, BankTransferPayment

def test_payment_processors():
    for p in (CashPayment(),CreditCardPayment(),BankTransferPayment()): assert p.pay(10.0) is True
