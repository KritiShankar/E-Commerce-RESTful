from fastapi.testclient import TestClient
from main import app

print(app)
client = TestClient(app, base_url="http://localhost:9193")

# Sample product payload for tests
sample_product = {
    "name": "Test Product",
    "description": "A test product",
    "price": 100.0,
    "stock": 10
}

def test_add_product():
    response = client.post("/product/products", json=sample_product)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == sample_product["name"]
    assert data["price"] == sample_product["price"]
    assert data["stock"] == sample_product["stock"]


def test_get_products():
    # Ensure at least one product exists (use the one added earlier)
    response = client.get("/product/products")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(p["name"] == sample_product["name"] for p in data)


def test_create_order_success():
    # First, add a product to order
    response = client.post("/product/products", json={
        "name": "Order Product",
        "description": "Product for order",
        "price": 50.0,
        "stock": 5
    })
    product_id = response.json()["id"]

    order_payload = {
        "products": [
            {"product_id": product_id, "quantity": 2}
        ]
    }
    response = client.post("/order/orders", json=order_payload)
    assert response.status_code == 201
    data = response.json()
    assert data["total_price"] == 100.0
    assert data["status"] == "completed"


def test_create_order_insufficient_stock():
    # Add product with limited stock
    response = client.post("/product/products", json={
        "name": "Low Stock Product",
        "description": "Only one in stock",
        "price": 10.0,
        "stock": 1
    })
    product_id = response.json()["id"]

    order_payload = {
        "products": [
            {"product_id": product_id, "quantity": 2}  # More than stock
        ]
    }
    response = client.post("/order/orders", json=order_payload)
    assert response.status_code == 400
    assert response.json()["status"] == "pending"
