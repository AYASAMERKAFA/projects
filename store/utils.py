def search_products(products, query):
    q=query.strip().casefold(); return [p for p in products if q in p.name.casefold()]

def sort_products(products, field):
    if field == "price": return sorted(products,key=lambda p:p.price)
    if field == "name": return sorted(products,key=lambda p:p.name.casefold())
    if field == "quantity": return sorted(products,key=lambda p:p.quantity)
    return products
