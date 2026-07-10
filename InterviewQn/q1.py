def reverse_list_inplace(lst):
    left = 0
    right = len(lst) - 1
    
    while left < right:
        # Swappinng
        lst[left], lst[right] = lst[right], lst[left]
        # Move pointers closer to the center
        left += 1
        right -= 1
    return lst

# Example Usage
original_list = [10, 20, 30, 40, 50]
print("\nTwo-Pointer Method (In-place):")
print("Input: ", original_list)
reverse_list_inplace(original_list)
print("Output:", original_list)