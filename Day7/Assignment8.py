import time

# === PART 1: Performance Benchmarking ===
print("--- Part 1: Performance Benchmarking (Squares 1 to 1M) ---")

s = time.time()
for_loop_squares = []
for i in range(1, 1000001): for_loop_squares.append(i * i)
print(f"For loop with append time : {time.time() - s:.6f} seconds")

s = time.time()
list_comp_squares = [i * i for i in range(1, 1000001)]
print(f"List comprehension time   : {time.time() - s:.6f} seconds")

s = time.time()
sum(i * i for i in range(1, 1000001))
print(f"Generator expression time : {time.time() - s:.6f} seconds\n")


# === PART 2: Divisible by 3 and 7 Comparison ===
print("--- Part 2: Divisible by 3 & 7 Implementation ---")

def find_divisible_for(n):
    res = []
    for i in range(1, n * 22):
        if i % 21 == 0: res.append(i)
        if len(res) == n: break
    return res

def find_divisible_while(n):
    res, i = [], 1
    while len(res) < n:
        if i % 21 == 0: res.append(i)
        i += 1
    return res

def find_divisible_list_comp(n):
    return [i for i in range(1, n * 21 + 1) if i % 21 == 0][:n]

print(f"For Loop Result           : {find_divisible_for(5)}")
print(f"While Loop Result         : {find_divisible_while(5)}")
print(f"List Comprehension Result : {find_divisible_list_comp(5)}")

print("\nReadability: 'while' explicitly checks collection length; 'for' needs an artificial limit and 'break'; 'list comp' is concise but requires pre-calculating boundaries.")


# === PART 3: Matrix Multiplication (3x3) ===
print("\n--- Part 3: Matrix Multiplication (3x3) ---")
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Version A: Nested Loops
result_nested = [[0]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        for k in range(3): result_nested[i][j] += A[i][k] * B[k][j]

print("Nested Loops Matrix Result:")
for r in result_nested: print(r)

# Version B: List Comprehension
result_comp = [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

print("\nList Comprehension Matrix Result:")
for r in result_comp: print(r)

print("\nComparison: Nested loops use explicit tracking and mutable steps (easier to debug). List comprehensions pack the tracking and evaluation into a single immutable, declarative layer (cleaner but denser).")