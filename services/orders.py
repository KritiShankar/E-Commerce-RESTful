from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse
from services.products import products_db
from uuid import uuid4
import json
from models.orders_models import *
from handlers.orders import OrderHandler
from handlers.products import ProductHandler
orders_router = APIRouter(prefix="/order")

orders_db = {}



# @orders_router.post("/orders", response_model=Order, status_code=201)
# def create_order(order_data: OrderCreate):
#     total_price = 0.0
#     stock_updates = {}
#
#     for item in order_data.products:
#         product = products_db.get(item.product_id)
#         if not product:
#             raise HTTPException(status_code=404, detail=f"Product {item.product_id} not found")
#         if product.stock < item.quantity:
#             raise HTTPException(status_code=400, detail=f"Insufficient stock for {product.name}")
#         total_price += item.quantity * product.price
#         stock_updates[item.product_id] = product.stock - item.quantity
#
#     # Apply stock updates
#     for pid, new_stock in stock_updates.items():
#         products_db[pid].stock = new_stock
#
#     order_id = str(uuid4())
#     new_order = Order(id=order_id, products=order_data.products, total_price=total_price, status="completed")
#     orders_db[order_id] = new_order
#     return new_order


@orders_router.post("/orders", response_model=Order, status_code=201)
def create_order(order_data: OrderCreate):
    total_price = 0.0
    stock_updates = {}
    order_handler = OrderHandler()
    product_handler = ProductHandler()
    try:
        for item in order_data.products:
            product = product_handler.get_product_details_by_id(item.product_id)
            # product = products_db.get(item.product_id)
            if not product:
                raise HTTPException(status_code=404, detail=f"Product {item.product_id} not found")
            if product.stock < item.quantity:
                raise HTTPException(status_code=400, detail=f"Insufficient stock for {product.name}")
            total_price += item.quantity * product.price
            stock_updates[item.product_id] = product.stock - item.quantity

        # Apply stock updates
        update_records = [ (new_stock,pid) for pid, new_stock in stock_updates.items()]
        product_handler.update_product_stock(update_records)

        # order_id = str(uuid4())
        items_json = json.dumps([item.dict() for item in order_data.products])
        new_order = OrderModel(products=items_json, total_price=total_price, status="completed")
        order_id = order_handler.add_orders(new_order)
        new_order = Order(id=order_id, products=order_data.products, total_price=total_price, status="completed")
        orders_db[order_id] = new_order
        return new_order
    except HTTPException as exc:
        items_json = json.dumps([item.dict() for item in order_data.products])
        new_order = OrderModel(products=items_json, total_price=total_price, status="pending")
        order_id = order_handler.add_orders(new_order)
        new_order = Order(id=order_id, products=order_data.products, total_price=total_price, status="pending")
        return JSONResponse(
            status_code=exc.status_code,
            content=new_order.dict(),
        )




