from typing import List
from pydantic import BaseModel, Field

class OrderItem(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)

class Order(BaseModel):
    id: str
    products: List[OrderItem]
    total_price: float
    status: str

class OrderModel(BaseModel):
    products: str
    total_price: float
    status: str

class OrderCreate(BaseModel):
    products: List[OrderItem]