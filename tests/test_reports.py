from store.models.order import Order, OrderItem
from store.services.report_service import total_revenue, average_order_value, best_selling_product

def test_reports():
    orders=[Order(1,"Aya",[OrderItem(1,"Keyboard",100.0,2)])]
    assert total_revenue(orders)==200.0
    assert average_order_value(orders)==200.0
    assert best_selling_product(orders)==("Keyboard",2)
