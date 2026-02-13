# Write a lambda function to check if a given string is a number

# Lambda function to check if a string is a number
is_number = lambda s: s.isdigit()

# Enter the Input
input_value =input("Enter a number: ")

# Checks the entered value
if is_number(input_value):
    print("It is a number")
else:
    print("It is not a number")

