class OrderCreated {
  constructor(orderId, restaurantId) {
    this.orderId = orderId;
    this.restaurantId = restaurantId;
    this.eventName = "OrderCreated";
    this.timestamp = new Date();
  }
}

module.exports = OrderCreated;
