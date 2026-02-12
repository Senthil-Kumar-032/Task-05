# Program to find the triplet in the given list

numbers = [10, 20, 30, 9]
total = 59
# loops for the first element index
for a in range(len(numbers)):
    # loops for the second element index
    for b in range(a + 1, len(numbers)):
        # loops for the third element index
        for c in range(b + 1, len(numbers)):
            total_value = numbers[a] + numbers[b] + numbers[c]
            # compares the total_value with the required number
            if total_value == total:
                # Displays the matching triplet
                print(numbers[a], numbers[b], numbers[c])

