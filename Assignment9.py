def longest_subarray(arr, K):
    left = 0
    current_sum = 0
    max_length = 0
    
    for right in range(len(arr)):
        current_sum += arr[right]  # Expand window
        
        # Shrink window from the left until sum <= K
        while current_sum > K:
            current_sum -= arr[left]
            left += 1
            
        # Calculate maximum window width seen so far
        max_length = max(max_length, right - left + 1)
        
    return max_length

# Testing
arr = [1, 2, 3, 4, 5]
K = 9
print(f"Longest subarray length: {longest_subarray(arr, K)}")