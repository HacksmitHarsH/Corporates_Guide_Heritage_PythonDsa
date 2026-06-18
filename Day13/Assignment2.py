def selection_sort(arr):
    n = len(arr)
    print(f"Initial Array: {arr}\n")
    
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element of unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Step {i + 1} (Swapped {arr[i]} with {arr[min_idx]}): {arr}")

array = [64, 25, 12, 22, 11, 90, 3]
selection_sort(array)