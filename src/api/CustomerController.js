const express = require("express");
const router = express.Router();
const orderService = require("../application/OrderService");

// CREATE ORDER
router.post("/create", (req, res) => {
  const { userId, restaurantId } = req.body;
  try {
    const order = orderService.createOrder(userId, restaurantId);
    res.status(201).json(order);
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

// ADD ITEM TO ORDER
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

// REMOVE ITEM FROM ORDER
router.delete("/:orderId/remove-item/:menuId", (req, res) => {
  const { orderId, menuId } = req.params;

  try {
    const order = orderService.removeItem(orderId, menuId);
    res.json({
      message: "Item removed",
      order
    });
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

// SCHEDULE ORDER
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

// CANCEL ORDER
router.delete("/:orderId/cancel", (req, res) => {
  const { orderId } = req.params;

  try {
    const order = orderService.cancelOrder(orderId);
    res.json({
      message: "Order canceled",
      order
    });
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

// GET ORDER DETAIL
router.get("/:orderId", (req, res) => {
  const { orderId } = req.params;
  const order = orderService.getOrder(orderId);

  if (!order) return res.status(404).json({ error: "Order not found" });

  res.json(order);
});

// GET ALL ORDERS FOR A USER
router.get("/list/:userId", (req, res) => {
  const { userId } = req.params;

  try {
    const orders = orderService.getOrdersByUser(userId);
    res.json(orders);
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

// CHECKOUT ORDER
router.post("/:orderId/checkout", (req, res) => {
  const { orderId } = req.params;

  try {
    const order = orderService.checkoutOrder(orderId);
    res.json(order);
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

module.exports = router;
