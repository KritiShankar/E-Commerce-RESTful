from db import get_connection_db
from models.orders_models import Order

connection = get_connection_db()
class OrderTable:
    def __init__(self):
        with get_connection_db() as connection:
            orders_cur = connection.cursor()
            orders_cur.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                products TEXT NOT NULL, 
                total_price REAL NOT NULL,
                status TEXT CHECK(status IN ('pending', 'completed')) NOT NULL
            );
            """)

    def insert_order(self, order_record:Order):
        with get_connection_db() as connection:
            orders_cur = connection.cursor()
            orders_cur.execute("""
                INSERT INTO orders (products, total_price, status)
                VALUES (?, ?, ?);
                """, (order_record.products,
                      order_record.total_price,
                      order_record.status))
            order_id = orders_cur.lastrowid
        return order_id