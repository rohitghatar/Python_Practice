# Q Write a Python program to read a file line by line and store it into a list

file = open("example.txt", 'r')

lines = file.readlines()
store_line = []
no = 1

for i in lines:
    print(f"{no} line : {i}")
    store_line.append(i)
    no +=1

print(store_line)