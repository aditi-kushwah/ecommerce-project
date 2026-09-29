from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: float
    stock: int = 0


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str | None
    price: float
    stock: int

    class Config:
        from_attributes = True