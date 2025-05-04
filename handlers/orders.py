from db.orders import OrderTable

class OrderHandler:
    def __init__(self):
        self.order_db_obj = OrderTable()

    def add_orders(self, new_order):
        try:
            order_id = self.order_db_obj.insert_order(new_order)
            return order_id
        except:
            pass