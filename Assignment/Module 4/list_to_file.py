# Q. Write a Python program to write a list to a file

file = open('example.txt','w')

temp = [1,2,3,4,5,6,7]

file.write(str(temp) + "\n") # write argument supports only string so we typecasted list in to string

file.close()