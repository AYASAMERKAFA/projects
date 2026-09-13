from typing import Protocol
from enum import Enum

class PaymentMethod(Enum):
    CASH = "cash"; CARD = "card"; BANK = "bank"

class PaymentProcessor(Protocol):
    def pay(self, amount: float) -> bool: ...

class CashPayment:
    def pay(self, amount): return True
class CreditCardPayment:
    def pay(self, amount): return True
class BankTransferPayment:
    def pay(self, amount): return True
