# Given a list of numbers, use the reduce function and a lambda expression
# to calculate the product of all the numbers in the list.

# import reduce from functools package

from functools  import reduce

nums = [2,3,4,1,2,3]

# Use reduce with lambda to multiply all elements in the list
product = reduce(lambda num1, num2: num1 * num2, nums)

# print the output
print(product)
