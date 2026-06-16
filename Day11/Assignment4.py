inventory = {
    "Laptop": 15,
    "Mouse": 50,
    "Keyboard": 30
}

# 1. Display all products using keys()
print("Products:")
for product in inventory.keys():
    print(f"- {product}")

print("-" * 20)

# 2. Display all quantities using values()
print("Quantities:")
for quantity in inventory.values():
    print(f"- {quantity}")

print("-" * 20)

# 3. Display product and quantity pairs using items()
print("Inventory Details:")
for product, quantity in inventory.items():
    print(f"{product}: {quantity}")