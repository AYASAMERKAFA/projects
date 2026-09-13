from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum

class OrderStatus(Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"

@dataclass
class OrderItem:
    product_id: int
    product_name: str
    unit_price: float
    quantity: int
    @property
    def subtotal(self): return self.unit_price * self.quantity

@dataclass
class Order:
    id: int
    customer: str | None
    items: list[OrderItem] = field(default_factory=list)
    status: OrderStatus = OrderStatus.PENDING
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    @property
    def total(self): return sum(i.subtotal for i in self.items)
    def __len__(self): return sum(i.quantity for i in self.items)
    def __str__(self): return f"Order #{self.id} | {self.status.value} | {self.total:.2f}"
    def cancel(self):
        if self.status == OrderStatus.PAID: raise ValueError("Paid order cannot be cancelled")
        self.status = OrderStatus.CANCELLED; self.updated_at = datetime.now(timezone.utc)
