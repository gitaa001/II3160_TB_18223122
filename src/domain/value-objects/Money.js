class Money {
  constructor(value) {
    if (value < 0) throw new Error("Money cannot be negative");
    this.value = value;
  }
}

module.exports = Money;
