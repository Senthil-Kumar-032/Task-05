# Program to check whether there exists a sub-list whose sum is equal to 0

# List to check the numbers
numbers = [4, 2, -3, 1, 6]

# Checks if a sub-list is found
sublist_found = False
# Select an element fom the list
for i in range(len(numbers)):
    total = 0
    # add numbers one by one
    for j in range(i, len(numbers)):
        total += numbers[j]
        # if sums become zero
        if total == 0:
            sublist_found = True
            print("Sub-list found:", numbers[i:j+1])
# if no sub-list is found
if not sublist_found:
    print("No sub-list Found")
