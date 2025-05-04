from pydantic import BaseModel, Field

class ProductIn(BaseModel):
    name: str
    description: str
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)

class Product(ProductIn):
    id: int

