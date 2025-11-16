const Order = require("../domain/entities/Order");
const OrderItem = require("../domain/entities/OrderItem");
const ScheduledTime = require("../domain/value-objects/ScheduledTime");
const OrderRepository = require("../infrastructure/OrderRepository");
const OrderCreated = require("../domain/events/OrderCreated");

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

  scheduleOrder(orderId, datetime) {
    const order = OrderRepository.find(orderId);
    if (!order) throw new Error("Order not found");

    const time = new ScheduledTime(datetime);
    order.setScheduledTime(time);

    OrderRepository.update(order);
    return order;
  }

  getOrder(orderId) {
    return OrderRepository.find(orderId);
  }
}

module.exports = new OrderService();
