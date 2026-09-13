import json
from pathlib import Path
from datetime import datetime
from ..models.product import Product
from ..models.customer import Customer
from ..models.order import Order, OrderItem, OrderStatus

class JsonRepository:
    def __init__(self, data_dir="data"):
        self.data_dir=Path(data_dir); self.data_dir.mkdir(parents=True,exist_ok=True)
    def _load(self,name,default):
        path=self.data_dir/name
        try:
            with path.open("r",encoding="utf-8") as f: return json.load(f)
        except FileNotFoundError: return default
        except json.JSONDecodeError: return default
    def _save(self,name,data):
        with (self.data_dir/name).open("w",encoding="utf-8") as f: json.dump(data,f,ensure_ascii=False,indent=4)
    def load_products(self): return [Product(**x) for x in self._load("products.json",[])]
    def save_products(self,items): self._save("products.json",[x.__dict__ for x in items])
    def load_customers(self): return [Customer(**x) for x in self._load("customers.json",[])]
    def save_customers(self,items): self._save("customers.json",[x.__dict__ for x in items])
    def load_orders(self):
        out=[]
        for x in self._load("orders.json",[]):
            items=[OrderItem(**i) for i in x["items"]]
            out.append(Order(x["id"],x.get("customer"),items,OrderStatus(x["status"]),datetime.fromisoformat(x["created_at"]),datetime.fromisoformat(x["updated_at"])))
        return out
    def save_orders(self,items):
        data=[]
        for o in items:
            data.append({"id":o.id,"customer":o.customer,"status":o.status.value,"created_at":o.created_at.isoformat(),"updated_at":o.updated_at.isoformat(),"items":[i.__dict__ for i in o.items]})
        self._save("orders.json",data)
