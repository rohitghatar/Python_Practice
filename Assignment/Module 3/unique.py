# Write a Python program to get unique values from a list 

my_list = [5, 2, 9, 1, 7, 3, 6, 5, 2, 9, 1, 7, 3, 6, 4, 8]

unique_list=[]

for i in my_list:
    if i not in unique_list:
        unique_list.append(i)

print(unique_list)