# Use a lambda function to extract the year, month, and day from a datetime object

# Import date and time from the directory
from datetime import datetime

# Store current date and time in a variable - today
today = datetime.now()

#Lambda function to extract year, month and day
get_date = lambda x: (x.year, x.month, x.day)
result = get_date(today)

print(result)
