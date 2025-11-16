const { v4: uuid } = require("uuid");

class Order {
  constructor(userId, restaurantId) {
    this.orderId = uuid();
    this.userId = userId;
    this.restaurantId = restaurantId;
    this.items = [];
    this.status = "PENDING";
    this.scheduledTime = null;
  }

  addItem(orderItem) {
    this.items.push(orderItem);
  }

  setScheduledTime(timeVO) {
    this.scheduledTime = timeVO;
  }

  totalPrice() {
    return this.items.reduce((sum, item) => sum + item.total(), 0);
  }
}

module.exports = Order;
