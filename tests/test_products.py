def test_stock_decrease(product):
    product.stock_decrease(3); assert product.quantity==7
