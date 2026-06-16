# Create employee dictionary (ID -> Name)
employees = {
    "E101": "Alice",
    "E102": "Bob",
    "E103": "Charlie",
    "E104": "Diana"
}

# Ask user for input
search_id = input("Enter Employee ID to search: ").strip()

# Use get() with a default fallback message
result = employees.get(search_id, "Employee Not Found")

print(result)