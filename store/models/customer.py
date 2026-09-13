from dataclasses import dataclass

@dataclass
class Customer:
    id: int
    name: str
    email: str

    def __str__(self):
        return f"{self.name} <{self.email}>"
