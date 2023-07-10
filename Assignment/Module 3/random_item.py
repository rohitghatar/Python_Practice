# Write a Python program to select an item randomly from a list. 

# for selecting randomly in python we have to import random

import random

list1 = ['1','2','3','4','5','6','7','8']

random_item = random.choice(list1)
print("rnadom item from list is : ", random_item)

for i in range(len(list1)):
    print(random.choice(list1))



