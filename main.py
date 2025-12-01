from fastapi import FastAPI
from src.api.CustomerController import router as customer_router
from src.api.AuthController import router as auth_router

app = FastAPI()

# Register domain routers
app.include_router(customer_router, prefix="/customer")
app.include_router(auth_router, prefix="/auth")