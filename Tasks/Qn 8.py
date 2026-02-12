# Program to find minimum element in a sorted rotated list

def find_minimum_element(arr):
    # Initialize minimum with first element
    minimum = arr[0]

    # Goes through the list
    for i in range(1,len(arr)):
        if arr[i] < minimum:
            # Update minimum if smaller value is found
            minimum = arr[i]
    # Returns the smallest element
    return minimum

arr = [100, 501, 22, 37, 10, 999, 87, 351]
print("Minimum element is:- ", find_minimum_element(arr))

