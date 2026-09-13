import pytest
from store.services.inventory_service import decrease_stock
from store.exceptions import InsufficientStockError

def test_insufficient_stock(product):
    with pytest.raises(InsufficientStockError): decrease_stock([product],1,11)
