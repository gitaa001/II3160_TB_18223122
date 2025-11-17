const Order = require("../domain/entities/Order");
const OrderItem = require("../domain/entities/OrderItem");
const ScheduledTime = require("../domain/value-objects/ScheduledTime");
const OrderRepository = require("../infrastructure/OrderRepository");
const OrderCreated = require("../domain/events/OrderCreated");
const OrderDelivered = require("../domain/events/OrderDelivered");

class OrderService {
  createOrder(userId, restaurantId) {
    const order = new Order(userId, restaurantId);
    OrderRepository.save(order);

    const event = new OrderCreated(order.orderId, restaurantId);
    console.log("EVENT:", event);

    return order;
  }

  addItem(orderId, menuId, menuName, price, quantity) {
    const order = OrderRepository.find(orderId);
    if (!order) throw new Error("Order not found");

    const item = new OrderItem(menuId, menuName, price, quantity);
    order.addItem(item);

    OrderRepository.update(order);
    return order;
  }

  removeItem(orderId, menuId) {
    const order = OrderRepository.find(orderId);
    if (!order) throw new Error("Order not found");

    order.items = order.items.filter((item) => item.menuId !== menuId);

    OrderRepository.update(order);
    return order;
  }

  scheduleOrder(orderId, datetime) {
    const order = OrderRepository.find(orderId);
    if (!order) throw new Error("Order not found");

    const time = new ScheduledTime(datetime);
    order.setScheduledTime(time);

    OrderRepository.update(order);
    return order;
  }


  cancelOrder(orderId) {
    const order = OrderRepository.find(orderId);
    if (!order) throw new Error("Order not found");

    order.status = "Canceled";

    OrderRepository.update(order);
    return order;
  }

  checkoutOrder(orderId) {
    const order = OrderRepository.find(orderId);
    if (!order) throw new Error("Order not found");

    if (!order.scheduledTime) {
      throw new Error("Order must be scheduled before checkout");
    }

    order.status = "Pending";

    OrderRepository.update(order);
    return order;
  }

  getOrder(orderId) {
    return OrderRepository.find(orderId);
  }

  getOrdersByUser(userId) {
    return OrderRepository.findByUserId(userId);
  }

  markDelivered(orderId) {
    const order = OrderRepository.find(orderId);
    if (!order) throw new Error("Order not found");

    order.status = "Completed";
    OrderRepository.update(order);

    const event = new OrderDelivered(orderId);
    console.log("EVENT:", event);

    return order;
  }
}

module.exports = new OrderService();
