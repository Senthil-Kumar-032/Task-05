# Write a list comprehension that creates a new list of squares of even numbers from a given list,
# using a lambda function to check for even numbers

# List of numbers
nums = [1,2,3,4,5,6,7,8,9,10]

# Lambda function to check whether the number is even or not
is_even = lambda num: num % 2 == 0

# Create a list with even numbers squared
squared_num = [x ** 2 for x in nums if is_even(x)]

# Print the squared list
print(squared_num)