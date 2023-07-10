# Write a Python program to find the highest 3 values in a dictionary

# 1st method

my_dict = {'a': 10, 'b': 20, 'c': 15, 'd': 5, 'e': 25}
highest_values = sorted(my_dict.values(), reverse=True)[:3]
print("Highest three values:", highest_values)



# 2nd method

values = list(my_dict.values())

sorted_values = sorted(values, reverse=True)

highest_three = sorted_values[:3]

print("Highest three values:", highest_three)
