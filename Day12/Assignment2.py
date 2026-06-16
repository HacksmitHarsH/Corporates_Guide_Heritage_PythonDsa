def find_first(arr, target):
    low, high = 0, len(arr) - 1
    first_idx = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            first_idx = mid
            high = mid - 1  # Keep searching left
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return first_idx

def find_last(arr, target):
    low, high = 0, len(arr) - 1
    last_idx = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            last_idx = mid
            low = mid + 1  # Keep searching right
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return last_idx

def count_occurrences(arr, target):
    first = find_first(arr, target)
    if first == -1:
        return 0  # Element doesn't exist
    last = find_last(arr, target)
    return last - first + 1

# Testing
arr = [1, 2, 2, 2, 3, 4]
target = 2
print(f"Occurrences of {target}: {count_occurrences(arr, target)}")