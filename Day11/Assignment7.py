library_A = {"Rahul", "Amit", "Priya", "Sneha"}
library_B = {"Priya", "Karan", "Amit", "Vikram"}

# 1. Members present in both libraries
both = library_A.intersection(library_B)
print(f"Members in both libraries: {both}")

# 2. Members present in either library
either = library_A.union(library_B)
print(f"Members in either library: {either}")

# 3. Members only in Library A
only_A = library_A.difference(library_B)
print(f"Members only in Library A: {only_A}")