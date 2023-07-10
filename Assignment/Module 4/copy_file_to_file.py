# Q. Write a Python program to copy the contents of a file to another file.

file1 = open('example.txt','r')

file2 = open('copy.txt', 'w')

copy_data = file1.read()

file2.write(copy_data)