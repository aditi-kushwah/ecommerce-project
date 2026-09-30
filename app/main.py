from fastapi import FastAPI

from app.routes.auth import router as auth_router
from app.routes.products import router as product_router
from app.routes.cart import router as cart_router
from app.routes.orders import router as order_router
from app.routes.wishlist import router as wishlist_router
from app.routes.reviews import router as review_router
from app.routes.address import router as address_router
from app.routes.admin import router as admin_router

app = FastAPI(
    title="E-Commerce API",
    description="Backend API for an E-Commerce application",
    version="1.0.0"
)


app.include_router(auth_router)
app.include_router(product_router)
app.include_router(cart_router)
app.include_router(order_router)
app.include_router(wishlist_router)
app.include_router(review_router)
app.include_router(address_router)
app.include_router(admin_router)

@app.get("/")
def home():
    return {
        "message": "E-Commerce API is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }