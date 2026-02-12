#  Find Happy Numbers in the given list

nums = [10, 501, 22, 37, 100, 999, 87, 351]

happy_numbers = []

for num in nums:
    n = num

    # Loop until the number becomes single digit
    while n > 9:
        total = 0
        # takes one digit at a time from the number
        for digit in str(n):
            total += int(digit) * int(digit)
        n = total

    # If it ends in 1 or 7, it is a happy number
    if n == 1 or n == 7:
        happy_numbers.append(num)

print("Happy numbers:", happy_numbers)
print("Count:", len(happy_numbers))
