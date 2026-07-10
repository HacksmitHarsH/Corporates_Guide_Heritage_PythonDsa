
n = int(input())

#  Read the second line, split it by spaces, and convert to integers
user_input = input().split()
numbers = []
for x in user_input:
    numbers.append(int(x))

# Remove duplicate numbers using a set
unique_numbers = list(set(numbers))

#  Sort unique numbers  smallest to largest
unique_numbers.sort()

# Print the result exactly as required
if len(unique_numbers) < 2:
    print(-1)
else:
    # unique_numbers[-2] grabs the second-to-last item in the sorted list
    print(unique_numbers[-2])