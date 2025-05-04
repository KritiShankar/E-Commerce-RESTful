from typing import List
from fastapi import APIRouter
from uuid import uuid4
from models.products_models import *
from handlers.products import ProductHandler


products_router = APIRouter(prefix="/product")

products_db = {}



# @products_router.get("/products", response_model=List[Product])
# def get_products():
#     return list(products_db.values())

@products_router.get("/products", response_model=List[Product])
def get_products():
    products_handlers = ProductHandler()
    records = products_handlers.get_product_details()
    response = [Product(**item) for item in records]
    return response

# @products_router.post("/products", response_model=Product, status_code=201)
# def add_product(product: ProductIn):
#     product_id = str(uuid4())
#     new_product = Product(id=product_id, **product.dict())
#     products_db[product_id] = new_product
#     return new_product

@products_router.post("/products", response_model=Product, status_code=201)
def add_product(new_product: ProductIn):
    products_handlers = ProductHandler()
    # product_id = str(uuid4())
    # new_product = ProductIn(**product.dict())
    product_id = products_handlers.add_products(new_product)
    # products_db[product_id] = new_product
    new_product = Product(id=product_id, **new_product.dict())
    return new_product