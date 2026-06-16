customer_ids = [101, 102, 103, 101, 104, 102, 105, 103]

# Remove duplicates by converting the list to a set
unique_ids_set = set(customer_ids)

# Convert back to a list and sort it
sorted_unique_ids = sorted(list(unique_ids_set))

print(f"Unique Customer IDs (Sorted): {sorted_unique_ids}")