from pydantic import BaseModel, Field


class AddressCreate(BaseModel):
    full_name: str
    phone: str = Field(..., min_length=10, max_length=15)
    address_line: str
    city: str
    state: str
    pincode: str = Field(..., min_length=6, max_length=6)


class AddressResponse(BaseModel):
    id: int
    user_id: int
    full_name: str
    phone: str
    address_line: str
    city: str
    state: str
    pincode: str

    class Config:
        from_attributes = True