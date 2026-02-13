# Create a lambda function to generate a Fibonacci series up to n terms

# Import reduce from the functools Package
from functools import reduce

# # Lambda function to create a Fibonacci series with n terms
fib_series = lambda n: reduce(lambda a, _: a + [a[-1] + a[-2]], range(n - 2), [0,1] )

print(fib_series(10))