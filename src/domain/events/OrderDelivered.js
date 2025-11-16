class OrderDelivered {
  constructor(orderId) {
    this.orderId = orderId;
    this.eventName = "OrderDelivered";
    this.timestamp = new Date();
  }
}

module.exports = OrderDelivered;
