# Q. Write a Python program to read an entire text file.

file = open("example.txt", "r")

# Read the entire contents of the file
content = file.read()

file.close()

print(content)
