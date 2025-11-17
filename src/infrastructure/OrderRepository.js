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
    return order;
  }

  findByUserId(userId) {
    const results = [];

    for (const order of this.orders.values()) {
      if (order.userId === userId) {
        results.push(order);
      }
    }

    return results;
  }

  delete(orderId) {
    return this.orders.delete(orderId);
  }

  listAll() {
    return Array.from(this.orders.values());
  }
}

module.exports = new OrderRepository();
