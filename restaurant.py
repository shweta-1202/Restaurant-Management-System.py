from menu import Menu   # Import the Menu class for managing menu items
from order import Order     # Import the Order class for handling customer orders
from file_handling import read_orders_from_file, write_orders_to_file   # Import file handling functions for orders

def main():
    menu = Menu()   # Create an instance of the Menu class

    while True:
        print("\nRestaurant Management System")
        print("1. Manage Menu")
        print("2. Place Order")
        print("3. View Orders")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            manage_menu(menu)   # Call function to manage menu items
        elif choice == '2':
            place_order(menu)   # Call function to Place Order
        elif choice == '3':
            view_orders()   # Call function to view Order
        elif choice == '4':
            break   # Exit the loop and end the program
        else:
            print("Invalid choice. Please try again.")

def manage_menu(menu):
    while True:
        print("\nMenu Management")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Delete Item")
        print("4. Display Menu")
        print("5. Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            try:
                menu.add_item(name, price, quantity)    # Attempt to add a new item to the menu
            except Exception as e:
                print(f"Error: {e}")     # Print error message if adding item fails
        elif choice == '2':
            name = input("Enter item name: ")
            price = float(input("Enter new price: "))
            quantity = int(input("Enter new quantity: "))
            try:
                menu.update_item(name, price, quantity)  # Attempt to update an existing item
            except Exception as e:
                print(f"Error: {e}")    # Print error message if updating item fails
        elif choice == '3':
            name = input("Enter item name: ")
            try:
                menu.delete_item(name)  # Attempt to delete an existing item
            except Exception as e:
                print(f"Error: {e}")    # Print error message if deleting item fails
        elif choice == '4':
            menu.display_menu() # Display the current menu
        elif choice == '5':
            break   # Go back to the main menu
        else:
            print("Invalid choice. Please try again.")  # Prompt for valid input

def place_order(menu):
    order = Order()     # Create a new Order instance
    order = Order.take_order()   # Prompt the user to take an order
    order.generate_receipt()    # Generate and display the receipt for the order
    orders = read_orders_from_file()    # Read existing orders from file
    orders.append([(item.name, quantity) for item, quantity in order.items])    # Add the new order to the list
    write_orders_to_file(orders)    # Save the updated orders to file

def view_orders():
    orders = read_orders_from_file()
    for i, order in enumerate(orders, start=1):
        print(f"Order {i}:")
        for item, quantity in order:
            print(f"{item} x {quantity}")
        print()

main()
