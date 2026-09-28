from fastapi import FastAPI

app = FastAPI(
    title="E-Commerce API",
    description="Backend API for an E-Commerce application",
    version="1.0.0"
)


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