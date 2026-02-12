# Program to find the first non-repeating element

nums = [2, 7, 0, 3, 9, 2, 7, 0, 3]

# Loop through the list
for n in nums:
    # Check if the number appears only once
    if nums.count(n) == 1:
        print("First Non-Repeating Element is:- ", n)
        # If found loop breaks
        break
else:
    print("No Non-Repeating Element Found")
