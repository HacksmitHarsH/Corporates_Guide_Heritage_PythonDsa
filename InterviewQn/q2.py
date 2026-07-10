def find_min_max(lst):
    if not lst:
        return None, None  # Handle empty list case
        
    # Initialize both with the first element
    smallest = lst[0]
    largest = lst[0]
    
    # Loop through the list to compare
    for num in lst:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
            
    return largest, smallest

# Example Usage
numbers = [12, 45, 7, 89, 23]
largest, smallest = find_min_max(numbers)

print(" Loop Method:")
print(f"Largest = {largest}")
print(f"Smallest = {smallest}")