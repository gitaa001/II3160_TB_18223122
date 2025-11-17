from datetime import datetime

class OrderCreated:
    def __init__(self, order_id: str, restaurant_id: str):
        self.order_id = order_id
        self.restaurant_id = restaurant_id
        self.event_name = "OrderCreated"
        self.timestamp = datetime.utcnow()

    def __repr__(self):
        return f"<OrderCreated order_id={self.order_id} restaurant_id={self.restaurant_id} at={self.timestamp}>"
