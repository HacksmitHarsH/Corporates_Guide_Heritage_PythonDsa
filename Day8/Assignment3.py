# a) Generate a list of squares of numbers from 1 to 15.
# Note: range(1, 16) goes from 1 up to 15.
squares = [x**2 for x in range(1, 16)]
print(f"a) Squares from 1 to 15:\n{squares}\n")


# b) Generate a list of all even numbers from 1 to 50.
# Note: range(2, 51, 2) starts at 2 and steps by 2 up to 50.
evens = [x for x in range(1, 51) if x % 2 == 0]
print(f"b) Even numbers from 1 to 50:\n{evens}\n")


# c) Given words = ['hello', 'world', 'python', 'is', 'great'],
#    create a new list with words that have more than 4 characters.
words = ['hello', 'world', 'python', 'is', 'great']
long_words = [word for word in words if len(word) > 4]
print(f"c) Words with more than 4 characters:\n{long_words}\n")


# d) Flatten the nested list: matrix = [[1,2,3], [4,5,6], [7,8,9]]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# The outer loop 'for row in matrix' runs first, then 'for num in row'
flattened = [num for row in matrix for num in row]
print(f"d) Flattened matrix:\n{flattened}\n")


# e) Create a list of tuples (number, square) for numbers 1 to 8.
number_tuples = [(x, x**2) for x in range(1, 9)]
print(f"e) Tuples of (number, square) from 1 to 8:\n{number_tuples}")
