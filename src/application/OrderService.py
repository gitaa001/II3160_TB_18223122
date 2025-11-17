from src.domain.entities.Order import Order
from src.domain.entities.OrderItem import OrderItem
from src.domain.value_objects.ScheduledTime import ScheduledTime
from src.infrastructure.OrderRepository import OrderRepository
from src.domain.events.OrderCreated import OrderCreated
from src.domain.events.OrderDelivered import OrderDelivered


class OrderService:

    def create_order(self, customer_id: str, restaurant_id: str):
        order = Order(customer_id, restaurant_id)
        OrderRepository.save(order)

        event = OrderCreated(order.order_id, restaurant_id)
        print("EVENT:", event)

        return order

    def add_item(self, order_id: str, menu_id: str, menu_name: str, price: int, quantity: int):
        order = OrderRepository.find(order_id)
        if not order:
            raise ValueError("Order not found")

        item = OrderItem(menu_id, menu_name, price, quantity)
        order.add_item(item)

        OrderRepository.update(order)
        return order

    def remove_item(self, order_id: str, menu_id: str):
        order = OrderRepository.find(order_id)
        if not order:
            raise ValueError("Order not found")

        order.items = [item for item in order.items if item.menu_id != menu_id]

        OrderRepository.update(order)
        return order

    def schedule_order(self, order_id: str, datetime_str: str):
        order = OrderRepository.find(order_id)
        if not order:
            raise ValueError("Order not found")

        time = ScheduledTime(datetime_str)
        order.set_scheduled_time(time)

        OrderRepository.update(order)
        return order

    def cancel_order(self, order_id: str):
        order = OrderRepository.find(order_id)
        if not order:
            raise ValueError("Order not found")

        order.status = "Canceled"
        OrderRepository.update(order)

        return order

    def checkout_order(self, order_id: str):
        order = OrderRepository.find(order_id)
        if not order:
            raise ValueError("Order not found")

        if not order.scheduled_time:
            raise ValueError("Order must be scheduled before checkout")

        order.status = "Pending"
        OrderRepository.update(order)

        return order

    def get_order(self, order_id: str):
        return OrderRepository.find(order_id)

    def get_orders_by_customer(self, customer_id: str):
        return OrderRepository.find_by_customer_id(customer_id)

    def mark_delivered(self, order_id: str):
        order = OrderRepository.find(order_id)
        if not order:
            raise ValueError("Order not found")

        # Domain rule: canceled orders cannot be delivered
        if order.status == "Canceled":
            raise ValueError("Canceled orders cannot be marked as delivered")

        # Domain rule: must be scheduled and checked out before delivery
        if order.status not in ["Pending", "OnDelivery"]:
            raise ValueError(f"Cannot deliver order in status {order.status}")

        order.status = "Completed"
        OrderRepository.update(order)

        event = OrderDelivered(order_id)
        print("EVENT:", event)

        return order

OrderServiceInstance = OrderService()
