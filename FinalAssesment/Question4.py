#   number of elements (N)
n = int(input())

# line of space-separated integers and convert them into a list of numbers
numbers = list(map(int, input().split()))

# Create an empty list to store our unique numbers in order
unique_numbers = []

#  Loop through each number in the input list
for num in numbers:
    # If the number is NOT already in our unique list, add it
    if num not in unique_numbers:
        unique_numbers.append(num)

# Print the final list of unique numbers separated by a space
# The * symbol unpacks the list so they print on a single line separated by spaces
print(*unique_numbers)