from collections import Counter, defaultdict

def active_orders(orders): return [o for o in orders if o.status.value != "cancelled"]
def total_revenue(orders): return sum(o.total for o in active_orders(orders))
def total_orders(orders): return len(active_orders(orders))
def average_order_value(orders):
    n=total_orders(orders); return total_revenue(orders)/n if n else 0.0
def best_selling_product(orders):
    c=Counter()
    for o in active_orders(orders):
        for i in o.items: c[i.product_name] += i.quantity
    return c.most_common(1)[0] if c else None
def top_customer(orders):
    d=defaultdict(float)
    for o in active_orders(orders):
        if o.customer: d[o.customer]+=o.total
    return max(d.items(), key=lambda x:x[1]) if d else None
def low_stock_products(products, threshold=5): return [p for p in products if p.quantity <= threshold]
