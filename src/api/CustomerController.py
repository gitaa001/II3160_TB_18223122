from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.application.OrderService import OrderServiceInstance as service

router = APIRouter(tags=["Customer Order"])

# ===========================
# Request Body Models
# ===========================
class CreateOrderRequest(BaseModel):
    customer_id: str
    restaurant_id: str


class AddItemRequest(BaseModel):
    menu_id: str
    menu_name: str
    price: int
    quantity: int


class ScheduleOrderRequest(BaseModel):
    datetime: str


# ===========================
# CONTROLLER ENDPOINTS
# ===========================

# 1. CREATE ORDER
@router.post("/order/create")
def create_order(body: CreateOrderRequest):
    try:
        return service.create_order(body.customer_id, body.restaurant_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# 2. ADD ITEM
@router.post("/order/{order_id}/add-item")
def add_item(order_id: str, body: AddItemRequest):
    try:
        return service.add_item(order_id, body.menu_id, body.menu_name, body.price, body.quantity)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# 3. REMOVE ITEM
@router.delete("/order/{order_id}/remove-item/{menu_id}")
def remove_item(order_id: str, menu_id: str):
    try:
        return service.remove_item(order_id, menu_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# 4. SCHEDULE ORDER
@router.post("/order/{order_id}/schedule")
def schedule_order(order_id: str, body: ScheduleOrderRequest):
    try:
        return service.schedule_order(order_id, body.datetime)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# 5. CANCEL ORDER
@router.post("/order/{order_id}/cancel")
def cancel_order(order_id: str):
    try:
        return service.cancel_order(order_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# 6. CHECKOUT ORDER
@router.post("/order/{order_id}/checkout")
def checkout_order(order_id: str):
    try:
        return service.checkout_order(order_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# 7. GET ORDER DETAILS
@router.get("/order/{order_id}")
def get_order(order_id: str):
    order = service.get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


# 8. GET ORDERS BY USER
@router.get("/orders/user/{customer_id}")
def get_orders_by_customer(customer_id: str):
    return service.get_orders_by_customer(customer_id)


# 9. MARK DELIVERED
@router.post("/order/{order_id}/deliver")
def mark_delivered(order_id: str):
    try:
        return service.mark_delivered(order_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# 10. LIST ALL ORDERS 
@router.get("/orders")
def list_all_orders():
    from src.infrastructure.OrderRepository import OrderRepository
    return OrderRepository.list_all()
