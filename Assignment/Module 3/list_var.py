# Write a Python program to split a list into different variables. 

#-------- method 1 -------------

'''my_list = [1, 2, 3, 4, 5]

var1, var2, var3, var4, var5 = my_list

print("var1:", var1)
print("var2:", var2)
print("var3:", var3)
print("var4:", var4)
print("var5:", var5)
'''

#------- method 2 ---------------


my_list = [5, 6, 3, 4, 5]
variables = []

for item in my_list:
    variables.append(item)

i = 1
for var in variables:
    print(f"var {i}: {var}")
    i += 1

#----- 3rd Method ----------------------------


my_list2 = [5, 6, 7, 4, 3]
variables2 = []

for item in my_list2:
    variables2.append(item)

for i, var in enumerate(variables2, 1):
    print(f"var{i}: {var}")
