# To find the duplicate number in the given list

# Given List
list1 = [2,7,0,3,1,9,9,9]
list2 = [2,8,0,5,1,8,8,9]
list3 = [2,9,0,6,1,5,3,9]

# Convert lists to sets to remove duplicates and use the & operator to find common elements
duplicate_inlist = list(set(list1) & set(list2) & set(list3))

print("Duplicates in the given list are:- ",duplicate_inlist)
