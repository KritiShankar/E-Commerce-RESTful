from db.products import ProductTable
from models.products_models import Product

class ProductHandler:
    def __init__(self):
        self.product_db_obj = ProductTable()

    def add_products(self, new_product):
        try:
            product_id = self.product_db_obj.insert_product(new_product)
            return product_id
        except:
            pass

    def get_product_details(self, id = None):
        try:
            records = self.product_db_obj.fetch_product_details(id)
            return records
        except:
            pass

    def get_product_details_by_id(self, id = None):
        try:
            records = self.product_db_obj.fetch_product_details(id)
            return Product(**records[0])
        except:
            return None

    def update_product_stock(self, update_records):
        return self.product_db_obj.update_product_stock(update_records)