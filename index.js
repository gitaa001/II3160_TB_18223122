const express = require("express");
const app = express();
app.use(express.json());

// Customer-facing API
const customerController = require("./src/api/CustomerController");
app.use("/customer/order", customerController);

// Belum diimplementasi
/** Driver-facing API
const driverController = require("./src/api/DriverController");
app.use("/driver", driverController);

// Restaurant-facing API
const restaurantController = require("./src/api/RestaurantController");
app.use("/restaurant", restaurantController);
**/

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server berjalan di http://localhost:${PORT}`);
});
