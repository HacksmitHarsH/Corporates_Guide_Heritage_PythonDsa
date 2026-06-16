def find_max_average(arr, k):
    # Sum of the first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window across the rest of the array
    for i in range(k, len(arr)):
        # Add next element, drop the oldest element
        window_sum += arr[i] - arr[i - k]
        if window_sum > max_sum:
            max_sum = window_sum
            
    return max_sum / k

# Testing
arr = [1, 12, -5, -6, 50, 3]
k = 4
print(f"Max average of subarray length {k}: {find_max_average(arr, k)}")