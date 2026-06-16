# 1. Factorial Function
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

# 2. Sum of Digits Function
def sum_of_digits(n):
    if n < 10:  # Base case: single digit
        return n
    return (n % 10) + sum_of_digits(n // 10)  # Last digit + sum of remaining digits

# Testing
print(f"Factorial of 5: {factorial(5)}")
print(f"Sum of digits of 1234: {sum_of_digits(1234)}")