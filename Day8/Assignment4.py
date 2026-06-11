# a) Create a tuple called 'months' containing all 12 month names.
months = (
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
)
print(f"a) Months Tuple: {months}\n")


# b) Access and print the 3rd month, the last month, and months from index 3 to 6.
# Note: Slicing from index 3 to 6 (3:7) includes indices 3, 4, 5, and 6.
print("--- b) Tuple Access & Slicing ---")
print(f"3rd month: {months[2]}")
print(f"Last month: {months[-1]}")
print(f"Months from index 3 to 6: {months[3:7]}\n")


# c) Try to change the first element to 'January_New' and explain the error you get.
print("--- c) Immutability Test ---")
try:
    months[0] = 'January_New'
except TypeError as error:
    print(f"Error caught successfully: {error}")
    print("\nExplanation:")
    print("Tuples are 'immutable' data structures in Python. This means once a tuple is")
    print("created, its elements cannot be changed, added, or removed. Attempting to")
    print("reassign a value at a specific index triggers a 'TypeError' because the tuple")
    print("object does not support item assignment.\n")


# d) Create a single-element tuple containing your name. Prove it is a tuple using type().
# Note: The trailing comma is required, otherwise Python treats it as a regular string in parentheses.
name_tuple = ("AI Assistant",)
print("--- d) Single-element Tuple ---")
print(f"Value: {name_tuple}")
print(f"Proof of type: {type(name_tuple)}\n")


# e) Convert the 'months' tuple to a list, add 'Intercalary' as a 13th month,
#    then convert it back to a tuple and print.
print("--- e) Tuple Modification via List Conversion ---")
# Step 1: Convert tuple to list
months_list = list(months)

# Step 2: Append the 13th month
months_list.append("Intercalary")

# Step 3: Convert the list back to a tuple
modified_months_tuple = tuple(months_list)

print(f"Final modified tuple:\n{modified_months_tuple}")