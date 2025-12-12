from src.domain.entities.Order import Order
from src.domain.entities.OrderItem import OrderItem
from src.domain.value_objects.ScheduledTime import ScheduledTime
from src.infrastructure.OrderRepository import OrderRepository
from src.domain.events.OrderCreated import OrderCreated
from src.domain.events.OrderDelivered import OrderDelivered


class OrderService:

    # ========================
    #  CREATE ORDER
    # ========================
    def create_order(self, customer_id: str, restaurant_id: str):
        order = Order(customer_id, restaurant_id)
        OrderRepository.save(order)

        event = OrderCreated(order.order_id, restaurant_id)
        print("EVENT:", event)

        return order

    # ========================
    #  ADD ITEM
    # ========================
    def add_item(self, order_id: str, menu_id: str, menu_name: str, price: int, quantity: int):
        order = OrderRepository.find(order_id)
        if not order:
            raise ValueError("Order not found")

        item = OrderItem(menu_id, menu_name, price, quantity)
        order.add_item(item)

        OrderRepository.update(order)
        return order

    # ========================
    #  REMOVE ITEM
    # ========================
    def remove_item(self, order_id: str, menu_id: str):
        order = OrderRepository.find(order_id)
        if not order:
            raise ValueError("Order not found")

        order.items = [item for item in order.items if item.menu_id != menu_id]

        OrderRepository.update(order)
        return order

    # ========================
    #  SCHEDULE ORDER
    # ========================
    def schedule_order(self, order_id: str, datetime_str: str):
        order = OrderRepository.find(order_id)
        if not order:
            raise ValueError("Order not found")

        time = ScheduledTime(datetime_str)
        order.set_scheduled_time(time)

        # Update status → SCHEDULED
        order.status = "SCHEDULED"

        OrderRepository.update(order)
        return order

    # ========================
    #  CANCEL ORDER
    # ========================
    def cancel_order(self, order_id: str):
        order = OrderRepository.find(order_id)
        if not order:
            raise ValueError("Order not found")

        order.status = "CANCELED"
        OrderRepository.update(order)

        return order

    # ========================
    #  CHECKOUT
    # ========================
    def checkout_order(self, order_id: str):
        order = OrderRepository.find(order_id)
        if not order:
            raise ValueError("Order not found")

        if not order.scheduled_time:
            raise ValueError("Order must be scheduled before checkout")

        # Update status → CHECKOUT
        order.status = "CHECKOUT"
        OrderRepository.update(order)

        return order

    # ========================
    #  GET ORDER
    # ========================
    def get_order(self, order_id: str):
        return OrderRepository.find(order_id)

    # ========================
    #  GET ORDERS BY CUSTOMER
    # ========================
    def get_orders_by_customer(self, customer_id: str):
        return OrderRepository.find_by_customer_id(customer_id)

    # ========================
    #  DELIVER ORDER
    # ========================
    def mark_delivered(self, order_id: str):
        order = OrderRepository.find(order_id)
        if not order:
            raise ValueError("Order not found")

        # Cannot deliver canceled orders
        if order.status == "CANCELED":
            raise ValueError("Canceled orders cannot be delivered")

        # Must have gone through checkout
        if order.status != "CHECKOUT":
            raise ValueError(f"Order must be CHECKOUT before delivery, current status: {order.status}")

        # Update status → DELIVERED
        order.status = "DELIVERED"
        OrderRepository.update(order)

        event = OrderDelivered(order_id)
        print("EVENT:", event)

        return order

OrderServiceInstance = OrderService()
