import pytest
from store.models.product import Product
from store.models.order import Order, OrderItem
@pytest.fixture
def product(): return Product(1,"Keyboard","Electronics",80.0,10)
@pytest.fixture
def order(): return Order(1,"Aya",[OrderItem(1,"Keyboard",80.0,2)])
