# Write a Python program to find the repeated items of a tuple. 

my_tuple = (1, 2, 3, 2, 4, 5, 1, 2)

repeated_items = []
unique_items = set()
    
for item in my_tuple:
    if item in unique_items:
        repeated_items.append(item)
    else:
        unique_items.add(item)
    
print("Repeated items:", repeated_items)
print("Unique items:", unique_items)
