# Initial shopping cart
shopping_cart = {
    "Bread": 2.50,
    "Milk": 1.99,
    "Eggs": 3.49
}
print(f"Initial Cart: {shopping_cart}")

# 1. Add a new product
shopping_cart["Apple"] = 4.00

# 2. Update the price of an existing product
shopping_cart["Milk"] = 2.20

# 3. Remove a product
shopping_cart.pop("Bread")

print(f"Updated Cart: {shopping_cart}")

# 4. Calculate total cart value
total_value = sum(shopping_cart.values())
print(f"Total Cart Value: ${total_value:.2f}")