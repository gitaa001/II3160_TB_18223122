class OrderRepository {
  constructor() {
    this.orders = new Map();
  }

  save(order) {
    this.orders.set(order.orderId, order);
    return order;
  }

  find(orderId) {
    return this.orders.get(orderId) || null;
  }

  update(order) {
    this.orders.set(order.orderId, order);
  }
}

module.exports = new OrderRepository();
