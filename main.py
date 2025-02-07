from menu_item import MenuItem
from customer import Customer
from order import Order

if __name__ == "__main__":
    
    menu_items = [
        MenuItem("Cheeseburger", "Main Course", "A delicious cheeseburger with lettuce and tomato."),
        MenuItem("Caesar Salad", "Appetizer", "Fresh romaine lettuce with Caesar dressing.")
    ]

    customer_name = input("Enter customer name: ")
    customer_email = input("Enter customer email: ")


    customer1 = Customer(customer_name, customer_email)
    order1 = Order(order_id=1, customer=customer1)

    
    print("Available Menu Items:")
    item_number = 1  
    for item in menu_items:
        print(f"{item_number}. {item.display_info()}")
        item_number += 1  
    
    while True:
        item_index = int(input("Select a menu item by number to add to the order (0 to finish): ")) - 1

        if item_index == -1:  
            break

        if 0 <= item_index < len(menu_items):  
            order1.add_item(menu_items[item_index])
            print(f"Added '{menu_items[item_index].name}' to the order.")
        else: 
            print("Invalid menu item selection.")

        
        add_another = input("Add another item? (yes/no): ")
        if not add_another == 'yes':  
            break

    
    customer1.add_order(order1)
    order1.complete_order()

    print("Customer's Order History:")
    for order in customer1.display_orders():
        print(order)  