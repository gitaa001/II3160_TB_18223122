const Money = require("../value-objects/Money");
const Quantity = require("../value-objects/Quantity");

class OrderItem {
  constructor(menuId, menuName, price, quantity) {
    this.menuId = menuId;
    this.menuName = menuName;
    this.price = new Money(price);
    this.quantity = new Quantity(quantity);
  }

  total() {
    return this.price.value * this.quantity.value;
  }
}

module.exports = OrderItem;
