from menu_item import MenuItem
from customer import Customer
from order import Order

if __name__ == "__main__":
    # Create menu items
    menu_item1 = MenuItem("Cheeseburger", "Main Course", "A delicious cheeseburger with lettuce and tomato.")
    menu_item2 = MenuItem("Caesar Salad", "Appetizer", "Fresh romaine lettuce with Caesar dressing.")

    # List to hold menu items
    menu_items = [menu_item1, menu_item2]

    # Get customer information from user input
    customer_name = input("Enter customer name: ")
    customer_email = input("Enter customer email: ")

    # Create a customer
    customer1 = Customer(customer_name, customer_email)

    # Create an order
    order1 = Order(order_id=1, customer=customer1)

    # Allow the customer to select menu items for their order
    print("Available Menu Items:")
    for idx, item in enumerate(menu_items):
        print(f"{idx + 1}. {item.display_info()}")

    while True:
        item_index = int(input("Select a menu item by number to add to the order (0 to finish): ")) - 1

        if item_index == -1:
            break
        elif item_index < 0 or item_index >= len(menu_items):
            print("Invalid menu item selection.")
        else:
            order1.add_item(menu_items[item_index])
            print(f"Added '{menu_items[item_index].name}' to the order.")

            # Ask if the user wants to add another item
            another_item = input("Do you want to add another item? (yes/no): ").strip().lower()
            if another_item != 'yes':
                break

    # Customer adds the order to their order history
    customer1.add_order(order1)

    # Complete the order
    order1.complete_order()

    # Display customer's order history
    print("Customer's Order History:")
    for order in customer1.display_orders():
        print(order)  # Order ID: 1, Customer: [Customer Name], Items: [...], Status: Completedrya