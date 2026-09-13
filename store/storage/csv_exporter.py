import csv

def export_products(products, path="products.csv"):
    with open(path,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["id","name","category","price","quantity","active"]); w.writeheader()
        for p in products: w.writerow(p.__dict__)

def export_orders(orders, path="orders.csv"):
    with open(path,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["id","customer","status","total"]); w.writeheader()
        for o in orders: w.writerow({"id":o.id,"customer":o.customer,"status":o.status.value,"total":o.total})
