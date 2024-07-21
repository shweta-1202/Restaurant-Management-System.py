from file_handling import read_menu_from_file   # Import function to read menu items from file
from exception import InvalidMenuItemError, InsufficientQuantityError   # Import custom exceptions

class Order:
    def __init__(self):
        self.items = [] # Initialize the list to store items in the order

    def add_item(self, name, quantity):
        menu_items = read_menu_from_file()  # Load menu items from file
        for item in menu_items: # Iterate over each menu item
            if item.name == name:   # Check if item matches the requested name
                if item.quantity < quantity:    # Check if sufficient quantity is available
                    raise InsufficientQuantityError("Insufficient quantity.")
                self.items.append((item, quantity)) # Add item and quantity to the order
                return
        raise InvalidMenuItemError("Menu item not found.")  # Raise error if item not found

    def calculate_total(self):
        total = sum(item.price * quantity for item, quantity in self.items) # Calculate total
        return total # Return the total cost

    def generate_receipt(self):
        print("Receipt:")
        for item, quantity in self.items:   # Iterate over each ordered item
            print(f"{item.name} x {quantity}: ${item.price * quantity:.2f}")    # Print item name, quantity, and cost
        print(f"Total: ${self.calculate_total():.2f}")  # Print the total cost

    def take_order():
        order = Order() # Create a new Order object
        while True:
            name = input("Enter menu item name (or 'done' to finish): ")    # Prompt user to enter menu item name or 'done' to finish
            if name.lower() == 'done':  # Check if user wants to finish the order
                break
            quantity = int(input("Enter quantity: "))   # Prompt user for quantity
            try:
                order.add_item(name, quantity)  # Attempt to add item to order
            except Exception as e:  # Handle exceptions
                print(f"Error: {e}")    # Print error message
        return order    # Return the completed order
