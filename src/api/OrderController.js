const express = require("express");
const router = express.Router();
const orderService = require("../application/OrderService");

router.post("/create", (req, res) => {
  const { userId, restaurantId } = req.body;
  try {
    const order = orderService.createOrder(userId, restaurantId);
    res.status(201).json(order);
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

router.post("/:orderId/add-item", (req, res) => {
  const { orderId } = req.params;
  const { menuId, menuName, price, quantity } = req.body;

  try {
    const order = orderService.addItem(orderId, menuId, menuName, price, quantity);
    res.json(order);
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

router.post("/:orderId/schedule", (req, res) => {
  const { orderId } = req.params;
  const { datetime } = req.body;

  try {
    const order = orderService.scheduleOrder(orderId, datetime);
    res.json(order);
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

router.get("/:orderId", (req, res) => {
  const { orderId } = req.params;
  const order = orderService.getOrder(orderId);

  if (!order) return res.status(404).json({ error: "Order not found" });

  res.json(order);
});

module.exports = router;
