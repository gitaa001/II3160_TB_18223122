from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

from src.application.OrderService import OrderServiceInstance as service
from src.auth.dependency import get_current_user  

router = APIRouter(tags=["Customer Order"])


# ===========================
# Request Body Models
# ===========================
class CreateOrderRequest(BaseModel):
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

@router.post("/order/create")
def create_order(body: CreateOrderRequest, user=Depends(get_current_user)):
    try:
        return service.create_order(customer_id=user["username"], restaurant_id=body.restaurant_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/order/{order_id}/add-item")
def add_item(order_id: str, body: AddItemRequest, user=Depends(get_current_user)):
    try:
        return service.add_item(order_id, body.menu_id, body.menu_name, body.price, body.quantity)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/order/{order_id}/remove-item/{menu_id}")
def remove_item(order_id: str, menu_id: str, user=Depends(get_current_user)):
    try:
        return service.remove_item(order_id, menu_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/order/{order_id}/schedule")
def schedule_order(order_id: str, body: ScheduleOrderRequest, user=Depends(get_current_user)):
    try:
        return service.schedule_order(order_id, body.datetime)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/order/{order_id}/cancel")
def cancel_order(order_id: str, user=Depends(get_current_user)):
    try:
        return service.cancel_order(order_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/order/{order_id}/checkout")
def checkout_order(order_id: str, user=Depends(get_current_user)):
    try:
        return service.checkout_order(order_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/order/{order_id}")
def get_order(order_id: str, user=Depends(get_current_user)):
    order = service.get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.get("/orders")
def get_orders_by_customer(user=Depends(get_current_user)):
    return service.get_orders_by_customer(user["username"])


@router.post("/order/{order_id}/deliver")
def mark_delivered(order_id: str, user=Depends(get_current_user)):
    try:
        return service.mark_delivered(order_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/orders/all")
def list_all_orders(user=Depends(get_current_user)):
    from src.infrastructure.OrderRepository import OrderRepository
    return OrderRepository.list_all()
