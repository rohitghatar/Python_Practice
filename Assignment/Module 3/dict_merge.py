# Write a Python script to merge two Python dictionaries 

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

#   1st method

merge_dict = {}

for i in dict1:
    merge_dict[i] = dict1[i]
    
for j in dict2:
    merge_dict[j] = dict2[j]

print("Merged Dictionary:", merge_dict)

# 2nd method

merged_dict = {**dict1, **dict2}

print("Merged Dictionary:", merged_dict)


