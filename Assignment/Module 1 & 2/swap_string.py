''' Q. Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.'''


string1 = input("Enter the first string: ")


string2 = input("Enter the second string: ")

string3 = string2[:2] + string1[2:]

string4 = string1[:2] + string2[2:]

result = string3 + " " + string4

print("Result:", result)

