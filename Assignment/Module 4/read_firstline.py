# Q. Write a Python program to read first n lines of a file. 

file = open("example.txt", 'r')

n=int(input("How many lines you want to read : "))

for i in range(1, n+1):
    lines = file.readline()
    print(f"{i} line : {lines}")