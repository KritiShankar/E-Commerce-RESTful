# E-Commerce RESTful API (FastAPI)

This project is a **production-grade RESTful API** for a simple e-commerce platform. It allows users to:

* View available products
* Add new products
* Place orders with stock validation

Built with **FastAPI**, it includes robust exception handling, test cases using `pytest`, and Dockerization for containerized deployment.

---

## 🚀 Features

### 📦 Endpoints

* `GET /products`: Retrieve a list of all available products.
* `POST /products`: Add a new product with fields: `id`, `name`, `description`, `price`, and `stock`.
* `POST /orders`: Place an order by specifying a list of products and quantities.

### 🧱 Data Models

#### Product

* `id` (Primary Key integer)
* `name` (string)
* `description` (string)
* `price` (float)
* `stock` (integer)

#### Order

* `id` (Primary Key integer)
* `products` (list of `product_id` and `quantity`)
* `total_price` (float)
* `status` ("pending" or "completed")

### 🧠 Business Logic

* Validates stock availability before placing an order.
* Automatically deducts ordered quantities from stock.
* Returns errors for insufficient stock or invalid product IDs.

---

## 🛠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/KritiShankar/E-Commerce-RESTful.git
cd E-Commerce-RESTful
```

### 2. Create Virtual Environment and Install Dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python main.py
```

Access the interactive API docs at [http://127.0.0.1:9193/docs](http://127.0.0.1:9193/docs)

---

## ✅ Running Tests

Make sure the app is not already running, then run:

```bash
pytest test/pytest_fastapi.py
```

Test cases include:

* Adding a product
* Retrieving product list
* Placing valid orders
* Handling insufficient stock

---

## 🐳 Docker Deployment

### 1. Build Docker Image

```bash
docker build -t ecommerce-api .
```

### 2. Run the Container

```bash
docker run -d -p 9193:9193 ecommerce-api
```

Then visit [http://localhost:9193/docs](http://localhost:9193/docs)

---

## 📁 Project Structure

```
.
├── db/
│   ├── __init__.py
│   ├── orders.py
│   └── productss.py
├── handlers/
│   ├── __init__.py
│   ├── orders.py
│   └── productss.py
├── models/
│   ├── __init__.py
│   ├── orders_models.py
│   └── products_models.py    
├── services/
│   ├── __init__.py
│   ├── orders.py
│   └── products.py
├── test/
│   └── pytest_fastapi.py
├── Dockerfile
├── main.py
├── requirements.txt
└── Readme.md
```

