class Quantity {
  constructor(value) {
    if (value <= 0) throw new Error("Quantity must be positive");
    this.value = value;
  }
}

module.exports = Quantity;
