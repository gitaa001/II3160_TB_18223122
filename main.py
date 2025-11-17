from fastapi import FastAPI
from src.api.CustomerController import router as customer_router

app = FastAPI()

# Register domain routers
app.include_router(customer_router, prefix="/customer")
