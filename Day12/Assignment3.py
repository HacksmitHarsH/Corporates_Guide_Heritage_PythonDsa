def binary_search_recursive(arr, target, low, high):
    # Base case: Search space is exhausted
    if low > high:
        return -1
        
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

# Testing
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
print(f"Recursive Index of {target}: {binary_search_recursive(arr, target, 0, len(arr) - 1)}")