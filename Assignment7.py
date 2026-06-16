def find_all_pairs(arr, target):
    left = 0
    right = len(arr) - 1
    pairs = []
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1  # Shift both pointers inward
        elif current_sum < target:
            left += 1  # We need a larger sum
        else:
            right -= 1  # We need a smaller sum
            
    return pairs

# Testing
arr = [1, 2, 3, 4, 5, 6, 7]
target = 8
print(f"Pairs adding up to {target}: {find_all_pairs(arr, target)}")