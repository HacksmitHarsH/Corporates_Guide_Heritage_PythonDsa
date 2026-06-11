# Initialize the original list
scores = [55, 72, 88, 43, 91, 67, 55, 76]
print(f"Initial list: {scores}\n")

# a) Append the value 80 to the end of the list.
scores.append(80)
print(f"a) After appending 80: {scores}")

# b) Insert the value 100 at index 3.
scores.insert(3, 100)
print(f"b) After inserting 100 at index 3: {scores}")

# f) Use count() to find how many times 55 originally appears.
# We are doing this calculation here before '55' gets removed in the next step.
original_55_count = scores.count(55)

# c) Remove the first occurrence of 55.
scores.remove(55)
print(f"c) After removing the first 55: {scores}")

# d) Sort the list in ascending order and print it.
scores.sort()
print(f"d) Sorted in ascending order: {scores}")

# e) Sort the list in descending order and print it.
scores.sort(reverse=True)
print(f"e) Sorted in descending order: {scores}")

# Printing the result of step f) now to keep the output answers in order
print(f"f) The number 55 originally appeared {original_55_count} times.")

# g) Use index() to find the position of 88.
# Note: Because the list is now sorted descending, the index will reflect its new position.
position_88 = scores.index(88)
print(f"g) The current index of 88 is: {position_88}")

# h) Pop the last element and print both the popped value and the remaining list.
popped_value = scores.pop()
print(f"h) Popped value: {popped_value}")
print(f"   Remaining list: {scores}")