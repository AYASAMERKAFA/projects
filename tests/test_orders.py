import pytest
from store.services.order_service import OrderService
from store.exceptions import InvalidOrderError

def test_create_order_reduces_stock(product):
    s=OrderService([product]); s.create_order({1:3}); assert product.quantity==7

def test_cancel_restores_stock(product):
    s=OrderService([product]); o=s.create_order({1:3}); s.cancel_order(o); assert product.quantity==10

def test_empty_order_cannot_be_paid():
    from store.models.order import Order
    from store.models.payment import CashPayment
    s=OrderService([]); o=Order(1,None,[])
    with pytest.raises(InvalidOrderError): s.pay_order(o,CashPayment())
