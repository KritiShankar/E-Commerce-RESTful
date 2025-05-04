from db import get_connection_db
from models.products_models import Product
import sqlite3

class ProductTable:
    def __init__(self):
        with get_connection_db() as connection:
            product_cur = connection.cursor()
            product_cur.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL,
                stock INTEGER NOT NULL
            );
            """)

    def insert_product(self, product_record:Product):
        with get_connection_db() as connection:
            product_cur = connection.cursor()
            product_cur.execute("""
                INSERT INTO products (name, description, price, stock)
                VALUES (?, ?, ?, ?);
                """, (product_record.name,
                      product_record.description,
                      product_record.price,
                      product_record.stock))
            product_id = product_cur.lastrowid
        return product_id

    def fetch_product_details(self, id = None):
        with get_connection_db() as connection:
            connection.row_factory = sqlite3.Row
            product_cur = connection.cursor()
            if id != None:
                product_cur.execute(
                    f"""
                    select * from products where id = {id} order by id;
                    """
                )
            else:
                product_cur.execute(
                    """
                    select * from products order by id;
                    """
                )
            records = product_cur.fetchall()
        return records

    def update_product_stock(self, update_stock_records):
        with get_connection_db() as connection:
            product_cur = connection.cursor()
            product_cur.executemany("""
                UPDATE products
                    SET stock = ?
                    WHERE id = ?;
                """, update_stock_records)
        return True