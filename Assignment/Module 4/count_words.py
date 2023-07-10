# Q. Write a Python program to count the number of lines in a text file.

file = open('example.txt', 'r')

words = file.read().split()
count = 0

for word in words:
    count += 1

print(f"total no. of words : {count}")