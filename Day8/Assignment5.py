# a) Create a tuple: employee = ('Rajesh Kumar', 34, 'Data Analyst', 75000, 'Bangalore')
#    Unpack it into 5 separate variables and print each with a label.
employee = ('Rajesh Kumar', 34, 'Data Analyst', 75000, 'Bangalore')

name, age, role, salary, location = employee

print("--- a) Basic Tuple Unpacking ---")
print(f"Name:     {name}")
print(f"Age:      {age}")
print(f"Role:     {role}")
print(f"Salary:   ${salary}")
print(f"Location: {location}\n")


# b) Use the * (star) operator to unpack: first item, last two items, and the middle items.
#    Note: The star (*) operator collects the remaining elements into a list.
print("--- b) Star (*) Unpacking ---")
first_item, *middle_items, second_last, last_item = employee

print(f"First item:      {first_item}")
print(f"Middle items:    {middle_items}")
print(f"Last two items:  {second_last}, {last_item}\n")


# c) Swap the values of three variables x=10, y=20, z=30 in a single line
#    so that x gets z's value, y gets x's value, and z gets y's value.
#    Target outcome: x=30, y=10, z=20
x, y, z = 10, 20, 30
print("--- c) Single-Line Multi-Variable Swapping ---")
print(f"Before swapping: x = {x}, y = {y}, z = {z}")

x, y, z = z, x, y

print(f"After swapping:  x = {x}, y = {y}, z = {z}\n")


# d) Given a list of tuples: data = [('Alice',90), ('Bob',85), ('Charlie',78), ('Diana',92)]
#    Use a loop with tuple unpacking to print: 'Alice scored 90/100'
data = [('Alice', 90), ('Bob', 85), ('Charlie', 78), ('Diana', 92)]

print("--- d) Looping with Tuple Unpacking ---")
for student_name, score in data:
    print(f"{student_name} scored {score}/100")
print()


# e) Write a function min_max(numbers) that returns the minimum and maximum
#    of a list as a tuple. Unpack the return value when calling it.
print("--- e) Function Returning a Tuple ---")

def min_max(numbers):
    # Returns a tuple containing (min, max)
    return min(numbers), max(numbers)

# Sample list to test the function
scores_list = [43, 88, 91, 55, 72, 67]

# Call the function and unpack the returned tuple in a single step
lowest_score, highest_score = min_max(scores_list)

print(f"Tested List: {scores_list}")
print(f"Minimum Score: {lowest_score}")
print(f"Maximum Score: {highest_score}")