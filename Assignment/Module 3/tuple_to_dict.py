# Write a Python program to convert a list of tuples into a dictionary. 

# 1st method

list_of_tuples = [("a", 1), ("b", 2), ("c", 3)]

dictionary = dict(list_of_tuples)

print("Dictionary:", dictionary)


# 2nd method

list_of_tuples1 = [("a", 1), ("b", 2), ("c", 3)]

dictionary1 = {}
for key, value in list_of_tuples1:
    dictionary1[key] = value

print("Dictionary:", dictionary1)

