# Write a Python program to print all unique values in a dictionary. 

my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

unique_values = list(set(my_dict.values()))

print("Unique Values:", unique_values)
