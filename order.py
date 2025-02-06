class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.menu_items = []
        self.status = "Pending"

    def add_item(self, menu_item):
        self.menu_items.append(menu_item)

    def complete_order(self):
        self.status = "Completed"

    def display_info(self):
        items_info = ', '.join(item.name for item in self.menu_items)
        return f"Order ID: {self.order_id}, Customer: {self.customer.name}, Items: [{items_info}], Status: {self.status}"