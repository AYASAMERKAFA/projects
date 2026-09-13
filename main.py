import logging
from store.models.product import Product
from store.storage import JsonRepository, export_products, export_orders
from store.services.order_service import OrderService
from store.services.report_service import total_revenue, average_order_value, best_selling_product, top_customer, low_stock_products
from store.models.payment import CashPayment, CreditCardPayment, BankTransferPayment
from store.utils import search_products, sort_products
from store.exceptions import InsufficientStockError, InvalidOrderError, ProductNotFoundError

logging.basicConfig(filename="logs/application.log",level=logging.INFO,format="%(asctime)s | %(levelname)s | %(message)s")
repo=JsonRepository(); products=repo.load_products(); orders=repo.load_orders()
if not products: products=[Product(1,"Keyboard","Electronics",80.0,10),Product(2,"Mouse","Electronics",25.0,20)]; repo.save_products(products)
service=OrderService(products,orders)

def main():
    while True:
        print("\n1 Add product | 2 List | 3 Search | 4 Sort | 5 Order | 6 Reports | 7 Export CSV | 8 Cancel | 9 Exit")
        c=input("Choose: ").strip()
        try:
            if c=="1":
                p=Product(max((x.id for x in products),default=0)+1,input("Name: "),input("Category: "),float(input("Price: ")),int(input("Quantity: "))); products.append(p); repo.save_products(products)
            elif c=="2":
                for p in products: print(p)
            elif c=="3":
                for p in search_products(products,input("Search: ")): print(p)
            elif c=="4":
                for p in sort_products(products,input("price/name/quantity: ").strip()): print(p)
            elif c=="5":
                cart={};
                while True:
                    pid=int(input("Product ID (0 finish): "))
                    if pid==0: break
                    cart[pid]=int(input("Quantity: "))
                o=service.create_order(cart,input("Customer: ")); print(o)
                method=input("Payment cash/card/bank: ").casefold(); processor={"cash":CashPayment(),"card":CreditCardPayment(),"bank":BankTransferPayment()}.get(method)
                if processor and service.pay_order(o,processor): repo.save_products(products); repo.save_orders(service.orders)
            elif c=="6": print("Revenue:",total_revenue(orders),"Orders:",len(orders),"Average:",average_order_value(orders),"Best:",best_selling_product(orders),"Top customer:",top_customer(orders),"Low stock:",low_stock_products(products))
            elif c=="7": export_products(products); export_orders(orders); print("CSV exported")
            elif c=="8":
                oid=int(input("Order ID: ")); o=next((x for x in orders if x.id==oid),None)
                if not o: raise InvalidOrderError("Order not found")
                service.cancel_order(o); repo.save_products(products); repo.save_orders(orders)
            elif c=="9": break
        except (ProductNotFoundError,InsufficientStockError,InvalidOrderError,ValueError) as e: print("Error:",e)
if __name__=="__main__": main()
