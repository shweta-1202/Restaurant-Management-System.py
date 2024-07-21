from exception import InvalidMenuItemError, DuplicateMenuItemError
from file_handling import read_menu_from_file,write_menu_to_file

class MenuItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Menu:
    def __init__(self):
        self.menu_items = read_menu_from_file()# Load existing menu items from file

    def add_item(self, name, price, quantity):
        for item in self.menu_items:
            if item.name == name:  # Check if item already exists
                raise DuplicateMenuItemError("Menu item already exists.")
        self.menu_items.append(MenuItem(name, price, quantity))# Add new item to the menu
        write_menu_to_file(self.menu_items)# Save updated menu to file

    def update_item(self, name, price, quantity):
        for item in self.menu_items:
            if item.name == name:  # Find the item to update
                item.price = price # Update the price
                item.quantity = quantity   # Update the quantity
                write_menu_to_file(self.menu_items)# Save updated menu to file
                return
        raise InvalidMenuItemError("Item not found in menu.")  # Raise error if item not found

    def delete_item(self, name):
        for item in self.menu_items:
            if item.name == name:  # Find the item to delete
                self.menu_items.remove(item)   # Remove item from the menu
                write_menu_to_file(self.menu_items)# Save updated menu to file
                return
        raise InvalidMenuItemError("Item not found in menu.")  # Raise error if item not found

    def display_menu(self):
        if not self.menu_items:# Check if the menu is empty
            print("The menu is empty.")
        for item in self.menu_items:   # Iterate through each item in the menu
            print(f"{item.name}: ${item.price:.2f} (Quantity: {item.quantity})")   # Print item details
