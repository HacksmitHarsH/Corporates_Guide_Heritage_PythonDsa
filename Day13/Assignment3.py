def insertion_sort_count(arr):
    comparisons = 0
    # Start from the 1st index as the 0th index is trivially sorted
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comparisons += 1  # A comparison happens here
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break # Comparison failed, loop terminates
        arr[j + 1] = key
    return comparisons

# Part A
array_a = [3, 5, 7, 9, 11]
comp_a = insertion_sort_count(array_a)
print(f"Part A (Sorted) Comparisons: {comp_a}")

# Part B
array_b = [11, 9, 7, 5, 3]
comp_b = insertion_sort_count(array_b)
print(f"Part B (Reverse Sorted) Comparisons: {comp_b}")