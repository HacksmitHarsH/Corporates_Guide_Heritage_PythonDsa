def merge_sort_verbose(arr):
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left = merge_sort_verbose(arr[:mid])
    right = merge_sort_verbose(arr[mid:])
    
    # Merge Step
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    print(f"Merging {left} and {right} -> {merged}")
    return merged

array = [8, 3, 5, 4, 2, 7, 1, 6]
print("--- Merge Steps ---")
sorted_array = merge_sort_verbose(array)