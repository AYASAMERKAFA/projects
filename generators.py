def product_generator(products):
    for product in products: yield product

def order_total_generator(orders):
    for order in orders: yield order.total

def positive_totals(orders):
    return (order.total for order in orders if order.total > 0)
