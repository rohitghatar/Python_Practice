'''Write a Python script to check if a given key already exists in a
dictionary. '''

my_dict = {'apple': 10, 'banana': 5, 'cherry': 20, 'date': 15}

key = 'banana'

if key in my_dict:
    print(f"Key '{key}' exists in the dictionary.")
else:
    print("Key '{}' does not exist in the dictionary.".format(key))
