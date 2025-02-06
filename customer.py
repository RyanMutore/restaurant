class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.order_history = []

    def add_order(self, order):
        self.order_history.append(order)

    def display_orders(self):
        return [order.display_info() for order in self.order_history]