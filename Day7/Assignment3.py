def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fibonacci(n):
    if n <= 0:
        print("Please enter a positive integer greater than 0.")
        return
    a, b = 0, 1
    count = 0
    terms = []
    while count < n:
        terms.append(str(a))
        a, b = b, a + b
        count += 1
    print(", ".join(terms) + "...")

try:
    num = int(input("Enter a number: "))
    print(f"\nMultiplication Table for {num}:")
    print("-" * 20)
    for i in range(1, 13):
        print(f"{num} x {i:>2} = {num * i:>3}")
except ValueError:
    print("Please enter a valid integer.")

print("\nRunning FizzBuzz Extended (1 to 100):")
print("-" * 20)
for i in range(1, 101):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    if i % 7 == 0:
        output += "Bang"
    if not output:
        print(i)
    else:
        print(output)

print("\nTesting Factorial and Fibonacci Functions:")
print("-" * 20)
try:
    print(f"Factorial of 5: {factorial(5)}")
    print("First 7 terms of Fibonacci: ", end="")
    fibonacci(7)
except ValueError as e:
    print(e)