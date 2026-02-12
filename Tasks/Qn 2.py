# Check whether the list have prime number or not

nums = [10, 501, 22, 37, 100, 999, 87, 351]

# To store the prime numbers in the list
prime_numbers = []

# To check each number in the list
for num in nums:
    count = 0

    # Prime numbers are greater than 1
    if num > 1:
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count == 2:
            prime_numbers.append(num)

# Print the Prime Number
print("Prime numbers:", prime_numbers)
print("Count:", len(prime_numbers))
