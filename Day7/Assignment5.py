
# PART A: Integer Statistics

count = 0
total_sum = 0
maximum = float('-inf')
minimum = float('inf')

while True:
    num = int(input("Enter an integer (0 to stop): "))
    if num == 0:
        break
    
    count += 1
    total_sum += num
    
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print("\n--- Part A Results ---")
if count > 0:
    print(f"Count: {count}")
    print(f"Sum: {total_sum}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
else:
    print("No numbers were entered except 0.")



# PART B: Prime Numbers between 1 and 100

prime_count = 0

print("\n--- Part B Results ---")
print("Prime numbers between 1 and 100:")

for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        prime_count += 1

print(f"\nTotal number of primes: {prime_count}")



# PART C: Reverse a Number Arithmetically

print("\n--- Part C Results ---")
original_num = int(input("Enter an integer to reverse: "))

# Handle negative numbers gracefully if needed
temp_num = abs(original_num)
reversed_num = 0

while temp_num > 0:
    remainder = temp_num % 10
    reversed_num = (reversed_num * 10) + remainder
    temp_num //= 10

if original_num < 0:
    reversed_num = -reversed_num

print(f"Original number: {original_num}")
print(f"Reversed number: {reversed_num}")