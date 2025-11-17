class OrderRepository:
    def __init__(self):
        self.orders = {}

    def save(self, order):
        self.orders[order.order_id] = order
        return order

    def find(self, order_id):
        return self.orders.get(order_id, None)

    def update(self, order):
        self.orders[order.order_id] = order
        return order

    def find_by_customer_id(self, customer_id):
        results = []

        for order in self.orders.values():
            if order.customer_id == customer_id:
                results.append(order)

        return results

    def delete(self, order_id):
        return self.orders.pop(order_id, None) is not None

    def list_all(self):
        return list(self.orders.values())


# Singleton instance (equivalent to module.exports = new OrderRepository())
OrderRepository = OrderRepository()
