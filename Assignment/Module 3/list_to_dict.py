# Write a Python program to map two lists into a dictionary 

keys = ['a', 'b', 'c']
values = [1, 2, 3]

#---- 1st method -----------------

mapped_dict = {keys[i]: values[i] for i in range(min(len(keys), len(values)))}
# this loop will stop at min len of any list to avoid error

print("Mapped Dictionary:", mapped_dict)


#---------- 2nd method ------------------------

dict1={}
dict2={}

for i in range(len(keys)):
    dict1[keys[i]] = values[i]

print(dict1)


#---------- 3rd method ---------------------

'''mapped_dict = dict(zip(keys, values))

print("Mapped Dictionary:", mapped_dict)
'''