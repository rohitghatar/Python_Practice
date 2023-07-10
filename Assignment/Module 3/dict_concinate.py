'''Write a Python script to concatenate following dictionaries to create a
new one. '''

# 1st method

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

new_dict = {}

for d in (dict1, dict2, dict3):
    new_dict.update(d)

print("Concatenated Dictionary:", new_dict)


# 2nd method

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

new_dict = {**dict1, **dict2, **dict3}

print("Concatenated Dictionary:", new_dict)
