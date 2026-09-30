from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    category: str
    price: float
    stock: int = 0


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str | None
    category: str
    price: float
    stock: int

    class Config:
        from_attributes = True