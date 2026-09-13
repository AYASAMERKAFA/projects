import logging
from ..models.order import Order, OrderItem, OrderStatus
from ..exceptions import ProductNotFoundError, InsufficientStockError, InvalidOrderError
from .inventory_service import find_product
logger = logging.getLogger(__name__)

class OrderService:
    def __init__(self, products, orders=None): self.products=products; self.orders=orders or []
    def create_order(self, cart, customer=None):
        if not cart: raise InvalidOrderError("Cart is empty")
        items=[]
        for pid, qty in cart.items():
            if qty <= 0: raise InvalidOrderError("Quantity must be positive")
            p=find_product(self.products,pid)
            if p.quantity < qty: raise InsufficientStockError(f"Not enough stock for {p.name}")
            items.append(OrderItem(p.id,p.name,p.price,qty))
        oid=max((o.id for o in self.orders),default=0)+1
        order=Order(oid,customer,items)
        for i in items: find_product(self.products,i.product_id).stock_decrease(i.quantity)
        self.orders.append(order); logger.info("Created order %s",oid); return order
    def pay_order(self, order, processor):
        if not order.items: raise InvalidOrderError("Empty order cannot be paid")
        if order.status != OrderStatus.PENDING: raise InvalidOrderError("Only pending orders can be paid")
        ok=processor.pay(order.total)
        if ok: order.status=OrderStatus.PAID; logger.info("Paid order %s",order.id)
        return ok
    def cancel_order(self, order):
        if order.status == OrderStatus.CANCELLED: return
        if order.status == OrderStatus.PAID: raise InvalidOrderError("Paid order cannot be cancelled")
        for i in order.items: find_product(self.products,i.product_id).stock_increase(i.quantity)
        order.cancel(); logger.info("Cancelled order %s and restored stock",order.id)
