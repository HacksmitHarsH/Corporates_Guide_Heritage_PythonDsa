def find_second_largest(nums):
    # A list must have at least two elements to have a second largest
    if len(nums) < 2:
        return None

    # Initialize the largest and second largest with negative infinity
    largest = second_largest = float('-inf')

    for num in nums:
        if num > largest:
            # Current largest becomes the second largest
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            # Update second largest if num is between largest and second largest
            second_largest = num

    # If second_largest was never updated, it means all elements were identical
    return second_largest if second_largest != float('-inf') else None


# --- Example Usage ---
input_list = [15, 10, 45, 32, 60]
output = find_second_largest(input_list)

print(f"Input: {input_list}")
print(f"Output: {output}")