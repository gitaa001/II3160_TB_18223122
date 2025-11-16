const express = require("express");
const app = express();

app.use(express.json());

const orderRoutes = require("./src/api/orderController");
app.use("/order", orderRoutes);

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server berjalan di http://localhost:${PORT}`);
});
