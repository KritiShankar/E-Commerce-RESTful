from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from services.products import products_router
from services.orders import orders_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(products_router)
app.include_router(orders_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host='localhost', port=9192)