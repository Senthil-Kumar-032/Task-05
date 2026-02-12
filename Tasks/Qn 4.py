# Program to sum first and last number in the Integer

# Asking the user for number
num = int(input("Enter number: "))

# Extracting the first and last digit
first_digit = int(str(num)[0])
last_digit = num % 10

print("Output:- ", first_digit+last_digit)
