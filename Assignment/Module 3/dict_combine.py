'''Write a Python program to combine two dictionary adding values for
common keys.
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}
Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).'''

#   1st method

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined_dict = {}

for key, value in d1.items():
    combined_dict[key] = value

for key, value in d2.items():
    if key in combined_dict:
        combined_dict[key] += value
    else:
        combined_dict[key] = value

print("Combined Dictionary:", combined_dict)

# 2nd method

combined_dict2 = {key: d1.get(key, 0) + d2.get(key, 0) for key in set(d1) | set(d2)}

print("Combined Dictionary:", combined_dict2)

