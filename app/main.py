from fastapi import FastAPI

from app.routes.auth import router as auth_router
from app.routes.products import router as product_router


app = FastAPI(
    title="E-Commerce API",
    description="Backend API for an E-Commerce application",
    version="1.0.0"
)


app.include_router(auth_router)
app.include_router(product_router)


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