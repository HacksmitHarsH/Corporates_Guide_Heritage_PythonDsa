# a) Create a list of product tuples: (product_id, name, price, quantity)
#    with at least 8 products.
#    Note: Since tuples are immutable, our list functions will replace tuples 
#    when modifications (like quantity updates) are needed.
inventory = [
    (101, "Laptop", 850.00, 12),
    (102, "Mouse", 25.00, 4),
    (103, "Keyboard", 45.00, 3),
    (104, "Monitor", 200.00, 8),
    (105, "HDMI Cable", 15.00, 25),
    (106, "Headphones", 60.00, 2),
    (107, "USB Drive", 12.50, 40),
    (108, "Desk Lamp", 35.00, 5)
]


# b) Write functions: add_product(), remove_product(name), update_quantity(name, qty).
def add_product(product_id, name, price, quantity):
    """Appends a new product tuple to the inventory."""
    new_item = (product_id, name, price, quantity)
    inventory.append(new_item)
    print(f"Success: Added '{name}' to inventory.")

def remove_product(name):
    """Removes a product from the inventory by its name."""
    for item in inventory:
        if item[1].lower() == name.lower():
            inventory.remove(item)
            print(f"Success: Removed '{name}' from inventory.")
            return
    print(f"Error: Product '{name}' not found.")

def update_quantity(name, qty):
    """Updates the quantity of an existing product by recreating its tuple."""
    for i, item in enumerate(inventory):
        prod_id, prod_name, price, current_qty = item
        if prod_name.lower() == name.lower():
            # Tuples are immutable, so we replace the old tuple with a updated one
            inventory[i] = (prod_id, prod_name, price, qty)
            print(f"Success: Updated '{prod_name}' quantity to {qty}.")
            return
    print(f"Error: Product '{name}' not found.")


# Testing the functions from part b
print("--- b) Testing Inventory Functions ---")
add_product(109, "Webcam", 55.00, 6)
remove_product("Keyboard")
update_quantity("Mouse", 15)  # Restocking the mouse
print()


# c) Write a function total_inventory_value() that returns the sum of (price * quantity).
def total_inventory_value():
    """Calculates total value: sum of (price * quantity) for all items."""
    return sum(price * quantity for _, _, price, quantity in inventory)

print("--- c) Total Inventory Value ---")
print(f"Total Portfolio Value: ${total_inventory_value():,.2f}\n")


# d) Use a loop to display all products where quantity < 5 (low stock alert).
print("--- d) Low Stock Alert (Quantity < 5) ---")
for prod_id, name, price, qty in inventory:
    if qty < 5:
        print(f"ALERT: '{name}' (ID: {prod_id}) is low on stock! Only {qty} left.")
print()


# e) Sort and display products by price (ascending).
#    Note: key=lambda x: x[2] targets the price element at index 2 of the tuple.
print("--- e) Products Sorted by Price (Ascending) ---")
sorted_inventory = sorted(inventory, key=lambda item: item[2])

for prod_id, name, price, qty in sorted_inventory:
    print(f"ID: {prod_id} | {name:<12} | Price: ${price:>6.2f} | Qty: {qty}")
print()


# f) Search for a product by name using a loop and print its full details.
print("--- f) Product Search ---")
search_query = "Headphones"
found = False

for prod_id, name, price, qty in inventory:
    if name.lower() == search_query.lower():
        print(f"Match Found for '{search_query}':")
        print(f"  - Product ID : {prod_id}")
        print(f"  - Name       : {name}")
        print(f"  - Unit Price : ${price:.2f}")
        print(f"  - Stock Qty  : {qty}")
        found = True
        break  # Stop searching once found

if not found:
    print(f"Product '{search_query}' was not found in the inventory.")