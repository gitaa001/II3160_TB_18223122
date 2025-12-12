import uuid

class Order:
    def __init__(self, customer_id: str, restaurant_id: str):
        self.order_id = str(uuid.uuid4())
        self.customer_id = customer_id
        self.restaurant_id = restaurant_id
        self.items = []
        self.status = "PENDING"
        self.scheduled_time = None

    def add_item(self, order_item):
        self.items.append(order_item)

    def set_scheduled_time(self, scheduled_time_vo):
        self.scheduled_time = scheduled_time_vo

    def total_price(self):
        return sum(item.total() for item in self.items)
