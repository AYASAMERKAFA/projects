from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    category: str
    price: float
    quantity: int
    active: bool = True

    def stock_increase(self, amount: int) -> None:
        if amount <= 0: raise ValueError("Amount must be positive")
        self.quantity += amount

    def stock_decrease(self, amount: int) -> None:
        if amount <= 0: raise ValueError("Amount must be positive")
        if amount > self.quantity: raise ValueError("Insufficient stock")
        self.quantity -= amount

    @property
    def available(self) -> bool:
        return self.active and self.quantity > 0
