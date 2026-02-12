# Program to find all the ways to make 10

count = 0

# try all possible combinations of 1, 2, 5 and 10 rupees
for a in range(11):
    for b in range(6):
        for c in range(3):
            for d in range(2):
                if a*1 + b*2 + c*5 + d*10 == 10:
                    count += 1

print("Total ways:", count)
