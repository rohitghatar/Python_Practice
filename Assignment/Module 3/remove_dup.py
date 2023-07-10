# Write a Python program to remove duplicates from a list. 

list1=['1','2','3','4','5','1','6','2']

unique_list=[]

for item in list1:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)