# a) Create a list called 'student_marks' with 10 integer values between 40 and 100.
# We will initialize it with some sample values within that range.
student_marks = [45, 82, 67, 91, 55, 78, 88, 42, 99, 73]
print(f"Original list: {student_marks}\n")

# b) Print the first 3 elements, the last 3 elements, and every alternate element.
print("--- b) Slicing ---")
print(f"First 3 elements: {student_marks[:3]}")
print(f"Last 3 elements: {student_marks[-3:]}")
print(f"Every alternate element: {student_marks[::2]}\n")

# c) Print the total number of elements using len().
print("--- c) Total Elements ---")
total_elements = len(student_marks)
print(f"Total number of elements: {total_elements}\n")

# d) Update the 5th element to 95 and print the updated list.
# Note: Python uses 0-based indexing, so the 5th element is at index 4.
print("--- d) Updating an Element ---")
student_marks[4] = 95
print(f"Updated list (5th element changed to 95): {student_marks}\n")

# e) Print the list in reverse order using slicing (without modifying the original).
print("--- e) Reverse Order ---")
reversed_list = student_marks[::-1]
print(f"List in reverse order: {reversed_list}")