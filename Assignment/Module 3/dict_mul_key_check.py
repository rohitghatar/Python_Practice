# Write a Python program to check multiple keys exists in a dictionary

my_dict = {'apple': 10, 'banana': 5, 'cherry': 20, 'date': 15}

keys = ['banana', 'date', 'grape']

# 1st method 

for key in keys:
    if key in my_dict:
        print(f"key {key} exists in dictionary")
    else:
        print(f"key {key} does not exists in dictionary")

# 2nd method "ADVANCE METHOD"

all_exist = all(key in my_dict for key in keys)
any_exist = any(key in my_dict for key in keys)

print("All keys exist:", all_exist)
print("Any key exists:", any_exist)