from ..exceptions import ProductNotFoundError, InsufficientStockError

def find_product(products, product_id):
    for p in products:
        if p.id == product_id: return p
    raise ProductNotFoundError(f"Product {product_id} not found")

def decrease_stock(products, product_id, quantity):
    p = find_product(products, product_id)
    if quantity <= 0: raise ValueError("Quantity must be positive")
    if p.quantity < quantity: raise InsufficientStockError(f"Not enough stock for {p.name}")
    p.stock_decrease(quantity)

def increase_stock(products, product_id, quantity):
    find_product(products, product_id).stock_increase(quantity)
