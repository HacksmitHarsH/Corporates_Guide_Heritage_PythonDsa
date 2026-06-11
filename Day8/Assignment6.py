# a) Given: temperatures = [22, 35, 18, 40, 28, 15, 33, 27]
#    Use a for loop to print each temperature with its index (use enumerate).
temperatures = [22, 35, 18, 40, 28, 15, 33, 27]

print("--- a) Enumerate Loop ---")
for index, temp in enumerate(temperatures):
    print(f"Index {index}: {temp}°C")
print()


# b) Using the same list, count how many temperatures are above 30.
print("--- b) Counting Items with Conditions ---")
count_above_30 = 0

for temp in temperatures:
    if temp > 30:
        count_above_30 += 1

print(f"Number of temperatures above 30: {count_above_30}\n")


# c) Create two lists: names = ['Alice','Bob','Charlie'] and marks = [85, 92, 78].
#    Use zip() to print each student's name and mark together.
print("--- c) Zipping Multiple Lists ---")
names = ['Alice', 'Bob', 'Charlie']
marks = [85, 92, 78]

for name, mark in zip(names, marks):
    print(f"Student: {name} | Mark: {mark}")
print()


# d) Using a while loop, remove elements from temperatures one by one
#    until only temperatures above 25 remain. Print after each removal.
#    Note: We will check the elements from the list sequentially.
print("--- d) Conditional Removal via While Loop ---")
print(f"Starting list: {temperatures}")

# We will loop as long as there is any temperature <= 25 in the list
# We target the first item that breaks our condition, remove it, and print.
while any(temp <= 25 for temp in temperatures):
    for temp in temperatures:
        if temp <= 25:
            temperatures.remove(temp)
            print(f"Removed {temp} -> Remaining: {temperatures}")
            break  # Break the inner loop to re-evaluate the while condition

print(f"Final filtered list (Only > 25 remaining): {temperatures}\n")


# e) Write code using a nested loop to print the multiplication table (1 to 5)
#    as a formatted grid.
print("--- e) Multiplication Table Grid (1 to 5) ---")

# Outer loop for rows
for i in range(1, 6):
    # Inner loop for columns
    for j in range(1, 6):
        # Calculate product
        product = i * j
        # print with ':4d' formatting to ensure a neatly aligned grid (4 spaces width)
        print(f"{product:4d}", end="")
    
    print()