# Given a list of dictionaries, each representing a person with 'name' and 'age' keys,
# use lambda functions to filter out people under 18 and
# then map the remaining people's names to a new list

# List with person name and age
person = [
    {"name": "Senthil", "age": 25},
    {"name": "Siva", "age": 21},
    {"name": "Raja", "age": 28},
    {"name": "Jasmine", "age": 16}
]

# Create a list of names for people age 18 and above
result = list(map(lambda people: people["name"], filter(lambda people: people["age"] >= 18, person)))

# Displays the result
print(result)