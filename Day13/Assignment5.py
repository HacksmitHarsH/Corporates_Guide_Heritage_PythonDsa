def partition_trace(arr):
    print(f"Initial Array: {arr}")
    pivot = arr[-1]
    print(f"Selected Pivot: {pivot}")
    
    i = -1  # Pointer for smaller element
    for j in range(len(arr) - 1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    # Place pivot in its correct position
    arr[i + 1], arr[-1] = arr[-1], arr[i + 1]
    print(f"After Partition Pass: {arr}")
    return arr

array = [15, 3, 9, 8, 5, 2, 7, 1, 6]
partition_trace(array)