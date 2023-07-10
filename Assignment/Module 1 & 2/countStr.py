# Q. Write a Python program to count occurrences of a substring in a string.

string = input("Enter a string: ")    # as an example if you enter hi hello hi
substring = input("Enter a substring: ") # as an example if you enter h

x = string.count(substring)  # it'll count h from string and gives you 3 as an output
print("Occurrences of the substring:", x)
