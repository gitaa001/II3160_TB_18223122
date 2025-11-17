from src.domain.value_objects.Money import Money
from src.domain.value_objects.Quantity import Quantity

class OrderItem:
    def __init__(self, menu_id: str, menu_name: str, price: int, quantity: int):
        self.menu_id = menu_id
        self.menu_name = menu_name
        self.price = Money(price)
        self.quantity = Quantity(quantity)

    def total(self):
        return self.price.value * self.quantity.value
