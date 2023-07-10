# Q. Write a Python program to read last n lines of a file

file = open('example.txt','r')

n = int(input("Enter no. of last lines you want to read : "))

# it'll give last no of lines user want
lines = file.readlines()[-n:]

# it'll reverse the lines means last line will be first then so on
line = lines[::-1]

for i in line:
    print(i)
    
