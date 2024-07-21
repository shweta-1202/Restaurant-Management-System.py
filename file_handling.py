import menu     # Import the menu module to use MenuItem class

def read_menu_from_file(filename='menu.txt'):
    menu_items = []     # Initialize an empty list to store menu items
    try:
        with open(filename, 'r') as file:       # Open the file for reading
            for line in file:       # Read each line from the file
                name, price, quantity = line.strip().split(",")
                menu_items.append(menu.MenuItem(name, float(price), int(quantity)))     # Create a MenuItem object and add it to the list
    except FileNotFoundError:       # Handle the case where the file does not exist
        pass
    return menu_items       # Return the list of menu items

def write_menu_to_file(menu_items, filename='menu.txt'):
    with open(filename, 'w') as file:       # Open the file for writing
        for item in menu_items:
            file.write(f"{item.name},{item.price},{item.quantity}\n")       # Write the menu item details to the file

def read_orders_from_file(filename='orders.txt'):
    orders = []     # Initialize an empty list for orders
    try:
        with open(filename, 'r') as file:       # Open the file for reading
            orders = [eval(line.strip()) for line in file]      # Read each line, evaluate it to convert back to a list, and add to orders
    except FileNotFoundError:       # Handle the case where the file does not exist
        pass
    return orders       # Return the list of orders


def write_orders_to_file(orders, filename='orders.txt'):
    with open(filename, 'w') as file:       # Open the file for writing
        for order in orders:
            file.write(f"{order}\n")        # Write the order to the file
