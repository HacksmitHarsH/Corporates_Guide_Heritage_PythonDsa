def bubble_sort_trace(arr):
    n = len(arr)
    print(f"Initial Array: {arr}\n")
    
    # We need at most n-1 passes
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        print(f"After Pass {i + 1}: {arr}")
        
        # Optimization: If no elements were swapped, the array is already sorted.
        if not swapped:
            print(f"\nArray became fully sorted early at Pass {i + 1}!")
            return i + 1
            
    return n - 1

array = [29, 10, 14, 37, 13]
total_passes = bubble_sort_trace(array)
print(f"Total passes required: {total_passes}")