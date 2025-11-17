from datetime import datetime

class OrderDelivered:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.event_name = "OrderDelivered"
        self.timestamp = datetime.utcnow()

    def __repr__(self):
        return f"<OrderDelivered order_id={self.order_id} at={self.timestamp}>"
