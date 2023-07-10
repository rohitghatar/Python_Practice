# Q Write a Python program to read a file line by line store it into a variable.

file = open("example.txt", 'r')

# it'll store all lines in lines variable
lines = file.readlines()

no = 1

for i in lines:
    print(f"{no} line : {i}")
    no += 1