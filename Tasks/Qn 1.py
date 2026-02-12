# Create Odd and Even Number List from the given List

nums = [10, 501, 22, 37, 100, 999, 87, 351]

# To save the Value
even_numbers = []
odd_numbers = []

# Loop to check all the numbers
for n in nums:
    if n % 2 == 0:
        even_numbers.append(n)
    else:
        odd_numbers.append(n)

# Print the values after the loop ends
print("Even numbers:- ", even_numbers)
print("Odd numbers:- ", odd_numbers)
